#!/usr/bin/env python3
"""Harvest the sjqtentacles Standard ML ecosystem from GitHub.

Shells out to `gh repo list` to fetch every public repo in the org, filters
down to the SML ecosystem, normalizes the records, and writes
`data/ecosystem.generated.json`.

The network step (`fetch_repos`) is isolated; the filtering/normalization
(`filter_ecosystem`, `normalize`) is pure and unit-tested without `gh`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ORG = "sjqtentacles"

# gh JSON fields we request. Keep in sync with normalize().
GH_FIELDS = [
    "name",
    "description",
    "repositoryTopics",
    "stargazerCount",
    "primaryLanguage",
    "isArchived",
    "isFork",
]

# A repo with one of these topics (or an `sml-` name prefix) is considered part
# of the Standard ML ecosystem.
SML_TOPICS = {"standard-ml", "sml"}

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT = DATA_DIR / "ecosystem.generated.json"


def _topics(repo: dict) -> list[str]:
    """Extract the flat list of topic names from a gh repo record."""
    raw = repo.get("repositoryTopics") or []
    out = []
    for t in raw:
        if isinstance(t, dict) and "name" in t:
            out.append(t["name"])
        elif isinstance(t, str):
            out.append(t)
    return out


def _language(repo: dict) -> str | None:
    lang = repo.get("primaryLanguage")
    if isinstance(lang, dict):
        return lang.get("name")
    if isinstance(lang, str):
        return lang
    return None


def is_ecosystem(repo: dict) -> bool:
    """True if a repo belongs to the SML ecosystem (pure)."""
    if repo.get("isArchived") or repo.get("isFork"):
        return False
    name = repo.get("name", "")
    if name.startswith("sml-"):
        return True
    return any(t in SML_TOPICS for t in _topics(repo))


def normalize(repo: dict) -> dict:
    """Reduce a gh repo record to the stable shape generate.py consumes (pure)."""
    name = repo["name"]
    return {
        "name": name,
        "url": f"https://github.com/{ORG}/{name}",
        "description": (repo.get("description") or "").strip(),
        "topics": sorted(_topics(repo)),
        "stars": repo.get("stargazerCount", 0) or 0,
        "language": _language(repo),
    }


def filter_ecosystem(repos: list[dict]) -> list[dict]:
    """Filter to SML ecosystem repos, normalize, and sort by name (pure)."""
    eco = [normalize(r) for r in repos if is_ecosystem(r)]
    eco.sort(key=lambda r: r["name"])
    return eco


def fetch_repos() -> list[dict]:
    """Fetch all org repos via `gh` (impure: network + subprocess)."""
    cmd = [
        "gh",
        "repo",
        "list",
        ORG,
        "--limit",
        "1000",
        "--json",
        ",".join(GH_FIELDS),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(f"gh failed with exit code {proc.returncode}")
    return json.loads(proc.stdout)


def harvest() -> dict:
    """Fetch + filter, returning the serializable ecosystem document."""
    repos = fetch_repos()
    eco = filter_ecosystem(repos)
    return {"org": ORG, "count": len(eco), "repos": eco}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        help="Read raw gh JSON from a file instead of calling gh (for testing).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT,
        help=f"Where to write the ecosystem JSON (default: {OUTPUT}).",
    )
    args = parser.parse_args(argv)

    if args.input:
        repos = json.loads(args.input.read_text())
        eco = filter_ecosystem(repos)
        doc = {"org": ORG, "count": len(eco), "repos": eco}
    else:
        doc = harvest()

    args.output.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {doc['count']} ecosystem repos to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
