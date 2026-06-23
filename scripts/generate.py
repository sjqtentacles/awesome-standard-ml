#!/usr/bin/env python3
"""Render README.md for awesome-standard-ml from the data manifest.

Merges the hand-curated community resources (`data/community.yml`), the
harvested sjqtentacles ecosystem (`data/ecosystem.generated.json`), and the
category rules (`data/categories.yml`) into the generated section of
`README.md` (between the BEGIN/END markers).

The render is a pure function of its inputs, so regeneration produces a clean,
deterministic diff. `--check` re-renders in memory and exits nonzero if the
on-disk README is stale; CI uses this as a "README in sync" gate.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

DEFAULT_README = ROOT / "README.md"
DEFAULT_COMMUNITY = DATA / "community.yml"
DEFAULT_CATEGORIES = DATA / "categories.yml"
DEFAULT_ECOSYSTEM = DATA / "ecosystem.generated.json"

BEGIN_MARKER = "<!-- BEGIN GENERATED -->"
END_MARKER = "<!-- END GENERATED -->"

ORG = "sjqtentacles"
MISC_TITLE = "Misc"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(Path(path).read_text()) or {}


def load_json(path: Path) -> dict:
    import json

    return json.loads(Path(path).read_text())


def _period(text: str) -> str:
    """Ensure a one-line description ends with sentence punctuation."""
    text = (text or "").strip()
    if not text:
        return ""
    if text[-1] in ".!?":
        return text
    return text + "."


def _escape_md(text: str) -> str:
    """Escape characters that Markdown/awesome-lint would mis-parse.

    Square brackets in descriptions (e.g. `Keccak-f[1600]`, `[classes]`) are
    otherwise read as link references; backslash-escape them.
    """
    return text.replace("[", "\\[").replace("]", "\\]")


def categorize(repos: list[dict], categories_doc: dict) -> dict[str, list[dict]]:
    """Bucket repos into categories.

    First match wins by category order. Per-repo `overrides` take precedence.
    `ignore_topics` are never used for matching. Repos with no matching topic
    fall into `Misc`. Each repo lands in exactly one category. Repos within a
    category are sorted by name.
    """
    categories = categories_doc.get("categories", [])
    overrides = categories_doc.get("overrides", {}) or {}
    ignore = set(categories_doc.get("ignore_topics", []) or [])

    titles = [c["title"] for c in categories]
    title_set = set(titles)
    buckets: dict[str, list[dict]] = {t: [] for t in titles}
    if MISC_TITLE not in buckets:
        buckets[MISC_TITLE] = []

    # topic -> first category title that claims it
    topic_to_cat: dict[str, str] = {}
    for cat in categories:
        for topic in cat.get("topics", []) or []:
            topic_to_cat.setdefault(topic, cat["title"])

    for repo in repos:
        name = repo["name"]
        placed: str | None = None

        override = overrides.get(name)
        if override:
            if override not in title_set and override != MISC_TITLE:
                raise ValueError(
                    f"override for {name} -> unknown category {override!r}"
                )
            placed = override
        else:
            topics = [t for t in repo.get("topics", []) if t not in ignore]
            # Respect category order, then topic order within the repo.
            best_index = None
            for topic in topics:
                cat = topic_to_cat.get(topic)
                if cat is None:
                    continue
                idx = titles.index(cat)
                if best_index is None or idx < best_index:
                    best_index = idx
                    placed = cat
            if placed is None:
                placed = MISC_TITLE

        buckets[placed].append(repo)

    for repos_in in buckets.values():
        repos_in.sort(key=lambda r: r["name"])
    return buckets


def _render_entry(name: str, url: str, description: str) -> str:
    return f"- [{name}]({url}) - {_escape_md(_period(description))}"


def render(community: dict, ecosystem: dict, categories_doc: dict) -> str:
    """Render the generated section (between markers) as a string (pure)."""
    lines: list[str] = []

    # Community sections (hand-curated).
    for section in community.get("sections", []) or []:
        lines.append(f"## {section['title']}")
        lines.append("")
        blurb = (section.get("blurb") or "").strip()
        if blurb:
            lines.append(blurb)
            lines.append("")
        for entry in section.get("entries", []) or []:
            lines.append(
                _render_entry(entry["name"], entry["url"], entry.get("description", ""))
            )
        lines.append("")

    # Ecosystem catalog (auto-generated).
    repos = ecosystem.get("repos", [])
    buckets = categorize(repos, categories_doc)

    lines.append(f"## {ORG} ecosystem")
    lines.append("")
    lines.append(
        f"The [{ORG}](https://github.com/{ORG}) Standard ML ecosystem: "
        f"{len(repos)} libraries."
    )
    lines.append("")

    cat_meta = {c["title"]: c for c in categories_doc.get("categories", [])}
    ordered_titles = [c["title"] for c in categories_doc.get("categories", [])]
    if MISC_TITLE not in ordered_titles:
        ordered_titles.append(MISC_TITLE)

    for title in ordered_titles:
        repos_in = buckets.get(title, [])
        if not repos_in:
            continue
        lines.append(f"### {title}")
        lines.append("")
        blurb = (cat_meta.get(title, {}).get("blurb") or "").strip()
        if blurb:
            lines.append(blurb)
            lines.append("")
        for repo in repos_in:
            lines.append(
                _render_entry(repo["name"], repo["url"], repo.get("description", ""))
            )
        lines.append("")

    # Single trailing newline (strip the extra blank we always append last).
    text = "\n".join(lines).rstrip("\n") + "\n"
    return text


def splice(readme_text: str, generated: str) -> str:
    """Replace the content between BEGIN/END markers with `generated`."""
    if BEGIN_MARKER not in readme_text or END_MARKER not in readme_text:
        raise ValueError("README is missing the BEGIN/END GENERATED markers")
    pre, rest = readme_text.split(BEGIN_MARKER, 1)
    _old, post = rest.split(END_MARKER, 1)
    return f"{pre}{BEGIN_MARKER}\n{generated}{END_MARKER}{post}"


def build(
    readme_path: Path,
    community_path: Path,
    categories_path: Path,
    ecosystem_path: Path,
) -> str:
    community = load_yaml(community_path)
    categories_doc = load_yaml(categories_path)
    ecosystem = load_json(ecosystem_path)
    generated = render(community, ecosystem, categories_doc)
    return splice(readme_path.read_text(), generated)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--community", type=Path, default=DEFAULT_COMMUNITY)
    parser.add_argument("--categories", type=Path, default=DEFAULT_CATEGORIES)
    parser.add_argument("--ecosystem", type=Path, default=DEFAULT_ECOSYSTEM)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero if README.md is out of sync with the data.",
    )
    args = parser.parse_args(argv)

    new_text = build(args.readme, args.community, args.categories, args.ecosystem)

    if args.check:
        current = args.readme.read_text()
        if current != new_text:
            sys.stderr.write(
                "README.md is out of date. Run scripts/generate.py to regenerate.\n"
            )
            return 1
        print("README.md is in sync.")
        return 0

    args.readme.write_text(new_text)
    print(f"Wrote {args.readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
