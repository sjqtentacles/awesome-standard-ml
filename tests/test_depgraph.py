"""Unit tests for scripts/depgraph.py (pure sml.pkg parsing + edge building)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import depgraph  # noqa: E402


def test_parse_pkg_package_and_requires():
    text = (
        "package github.com/sjqtentacles/sml-lsp\n"
        "\n"
        "require {\n"
        "  github.com/sjqtentacles/sml-mlast\n"
        "  github.com/sjqtentacles/sml-fmt\n"
        "  github.com/sjqtentacles/sml-json\n"
        "}\n"
    )
    pkg, reqs = depgraph.parse_pkg(text)
    assert pkg == "github.com/sjqtentacles/sml-lsp"
    assert reqs == [
        "github.com/sjqtentacles/sml-mlast",
        "github.com/sjqtentacles/sml-fmt",
        "github.com/sjqtentacles/sml-json",
    ]


def test_parse_pkg_no_requires():
    pkg, reqs = depgraph.parse_pkg("package github.com/sjqtentacles/sml-foo\n")
    assert pkg == "github.com/sjqtentacles/sml-foo"
    assert reqs == []


def test_build_edges_filters_to_known_repos(tmp_path):
    (tmp_path / "sml-a").mkdir()
    (tmp_path / "sml-b").mkdir()
    (tmp_path / "sml-a" / "sml.pkg").write_text(
        "package github.com/sjqtentacles/sml-a\n"
        "require {\n"
        "  github.com/sjqtentacles/sml-b\n"
        "  github.com/other/not-in-ecosystem\n"
        "}\n"
    )
    (tmp_path / "sml-b" / "sml.pkg").write_text(
        "package github.com/sjqtentacles/sml-b\nrequire {\n}\n"
    )
    edges, missing = depgraph.build_edges(["sml-a", "sml-b", "sml-c"], tmp_path)
    assert edges == [("sml-a", "sml-b")]
    assert missing == ["sml-c"]


def test_render_is_deterministic():
    edges = [("sml-a", "sml-b"), ("sml-c", "sml-a")]
    a = depgraph.render(edges, 3, [])
    b = depgraph.render(edges, 3, [])
    assert a == b
    assert "graph LR" in a
    assert "2 edges across 3 libraries" in a
