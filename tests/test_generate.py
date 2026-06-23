"""Golden + behavior tests for scripts/generate.py."""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import generate  # noqa: E402
import harvest  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def docs():
    community = generate.load_yaml(FIXTURES / "community.yml")
    categories = generate.load_yaml(FIXTURES / "categories.yml")
    repos = json.loads((FIXTURES / "sample_repos.json").read_text())
    ecosystem = {"repos": harvest.filter_ecosystem(repos)}
    return community, ecosystem, categories


def test_render_matches_golden(docs):
    community, ecosystem, categories = docs
    expected = (FIXTURES / "expected_readme.md").read_text()
    assert generate.render(community, ecosystem, categories) == expected


def test_slug():
    assert generate._slug("Web, networking & protocols") == "web-networking--protocols"
    assert generate._slug("Math, numeric & scientific") == "math-numeric--scientific"
    assert generate._slug("sjqtentacles ecosystem") == "sjqtentacles-ecosystem"
    assert (
        generate._slug("Developer tooling (SML self-tooling)")
        == "developer-tooling-sml-self-tooling"
    )


def _parse_toc_and_headings(text):
    """Split rendered output into (toc_top, toc_nested, h2s, h3s).

    toc_top/toc_nested are the link texts in the Contents list; h2s/h3s are the
    body headings (excluding 'Contents'), in document order.
    """
    import re

    lines = text.splitlines()
    toc_top, toc_nested = [], []
    h2s, h3s = [], []
    in_toc = False
    link_re = re.compile(r"\[(?P<text>[^\]]+)\]\(#(?P<anchor>[^)]+)\)")
    for line in lines:
        if line.strip() == "## Contents":
            in_toc = True
            continue
        if line.startswith("## ") and line.strip() != "## Contents":
            in_toc = False
            h2s.append(line[3:].strip())
            continue
        if line.startswith("### "):
            h3s.append(line[4:].strip())
            continue
        if in_toc:
            m = link_re.search(line)
            if not m:
                continue
            if line.startswith("  - "):
                toc_nested.append((m.group("text"), m.group("anchor")))
            elif line.startswith("- "):
                toc_top.append((m.group("text"), m.group("anchor")))
    return toc_top, toc_nested, h2s, h3s


def test_toc_matches_headings(docs):
    community, ecosystem, categories = docs
    out = generate.render(community, ecosystem, categories)
    toc_top, toc_nested, h2s, h3s = _parse_toc_and_headings(out)

    # Contents is first heading.
    assert out.lstrip().startswith("## Contents")

    # Top-level TOC text == every body ## heading (excluding Contents), in order.
    assert [t for t, _ in toc_top] == h2s
    # Nested TOC text == every body ### heading, in order.
    assert [t for t, _ in toc_nested] == h3s

    # Every TOC anchor equals _slug() of its target heading text.
    for text, anchor in toc_top + toc_nested:
        assert anchor == generate._slug(text)

    # No anchor is dangling: each points at a real heading.
    heading_slugs = {generate._slug(h) for h in (h2s + h3s)}
    for _text, anchor in toc_top + toc_nested:
        assert anchor in heading_slugs


def test_categorize_first_match_and_override(docs):
    _community, ecosystem, categories = docs
    buckets = generate.categorize(ecosystem["repos"], categories)
    placed = {}
    for cat, repos in buckets.items():
        for r in repos:
            placed[r["name"]] = cat
    # override wins: sml-script -> Blockchain, not Web/Crypto/Dev tooling
    assert placed["sml-script"] == "Blockchain & cryptocurrency"
    # topic-based placement
    assert placed["sml-sha256"] == "Cryptography & security"
    assert placed["sml-lsp"] == "Developer tooling"
    assert placed["sml-fenwick"] == "Data structures"
    assert placed["sml-http"] == "Web, networking & protocols"
    # safety net: no domain topic -> Misc
    assert placed["sml-mystery"] == "Misc"


def test_categorize_places_each_repo_exactly_once(docs):
    _community, ecosystem, categories = docs
    buckets = generate.categorize(ecosystem["repos"], categories)
    placements = [r["name"] for repos in buckets.values() for r in repos]
    assert sorted(placements) == sorted(r["name"] for r in ecosystem["repos"])
    assert len(placements) == len(set(placements))


def test_repos_within_category_sorted(docs):
    _community, ecosystem, categories = docs
    buckets = generate.categorize(ecosystem["repos"], categories)
    for repos in buckets.values():
        names = [r["name"] for r in repos]
        assert names == sorted(names)


def test_render_is_deterministic(docs):
    community, ecosystem, categories = docs
    a = generate.render(community, ecosystem, categories)
    b = generate.render(community, ecosystem, categories)
    assert a == b


def test_render_count_is_computed(docs):
    community, ecosystem, categories = docs
    out = generate.render(community, ecosystem, categories)
    assert "6 libraries" in out


def test_splice_replaces_between_markers():
    readme = (
        "# Title\n\nintro\n\n"
        f"{generate.BEGIN_MARKER}\n"
        "OLD CONTENT\n"
        f"{generate.END_MARKER}\n\n"
        "## License\n"
    )
    spliced = generate.splice(readme, "NEW CONTENT\n")
    assert "OLD CONTENT" not in spliced
    assert "NEW CONTENT" in spliced
    assert spliced.startswith("# Title")
    assert spliced.rstrip().endswith("## License")
    assert generate.BEGIN_MARKER in spliced
    assert generate.END_MARKER in spliced


def test_check_mode(tmp_path, docs, monkeypatch):
    community, ecosystem, categories = docs
    generated = generate.render(community, ecosystem, categories)

    readme = tmp_path / "README.md"
    readme.write_text(
        f"# X\n\n{generate.BEGIN_MARKER}\n{generated}{generate.END_MARKER}\n"
    )
    eco_path = tmp_path / "ecosystem.generated.json"
    eco_path.write_text(json.dumps(ecosystem))

    args = [
        "--readme", str(readme),
        "--community", str(FIXTURES / "community.yml"),
        "--categories", str(FIXTURES / "categories.yml"),
        "--ecosystem", str(eco_path),
    ]
    # in sync -> 0
    assert generate.main(args + ["--check"]) == 0
    # stale -> nonzero
    readme.write_text(
        f"# X\n\n{generate.BEGIN_MARKER}\nSTALE\n{generate.END_MARKER}\n"
    )
    assert generate.main(args + ["--check"]) != 0


def test_write_then_check_roundtrip(tmp_path, docs):
    community, ecosystem, categories = docs
    generated = generate.render(community, ecosystem, categories)
    readme = tmp_path / "README.md"
    readme.write_text(f"# X\n\n{generate.BEGIN_MARKER}\n{generate.END_MARKER}\n")
    eco_path = tmp_path / "ecosystem.generated.json"
    eco_path.write_text(json.dumps(ecosystem))
    args = [
        "--readme", str(readme),
        "--community", str(FIXTURES / "community.yml"),
        "--categories", str(FIXTURES / "categories.yml"),
        "--ecosystem", str(eco_path),
    ]
    assert generate.main(args) == 0
    assert generated in readme.read_text()
    assert generate.main(args + ["--check"]) == 0
