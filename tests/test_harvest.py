"""Unit tests for scripts/harvest.py (pure filtering/normalization)."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import harvest  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_sample():
    return json.loads((FIXTURES / "sample_repos.json").read_text())


def test_is_ecosystem_keeps_sml_prefix_and_topic():
    repos = {r["name"]: r for r in load_sample()}
    assert harvest.is_ecosystem(repos["sml-sha256"])
    assert harvest.is_ecosystem(repos["sml-fenwick"])


def test_is_ecosystem_drops_non_sml():
    repos = {r["name"]: r for r in load_sample()}
    assert not harvest.is_ecosystem(repos["chinalang"])


def test_is_ecosystem_drops_archived_and_forks():
    repos = {r["name"]: r for r in load_sample()}
    assert not harvest.is_ecosystem(repos["sml-archived-thing"])
    assert not harvest.is_ecosystem(repos["sml-forked-thing"])


def test_filter_ecosystem_count_and_sorting():
    eco = harvest.filter_ecosystem(load_sample())
    names = [r["name"] for r in eco]
    # 6 real ecosystem repos; chinalang/archived/fork dropped.
    assert names == sorted(names)
    assert names == [
        "sml-fenwick",
        "sml-http",
        "sml-lsp",
        "sml-mystery",
        "sml-script",
        "sml-sha256",
    ]


def test_normalize_shape():
    eco = {r["name"]: r for r in harvest.filter_ecosystem(load_sample())}
    sha = eco["sml-sha256"]
    assert sha["url"] == "https://github.com/sjqtentacles/sml-sha256"
    assert sha["description"] == "SHA-256 hashing in pure Standard ML."
    assert sha["stars"] == 5
    assert sha["language"] == "Standard ML"
    # topics normalized to a sorted flat list of strings
    assert sha["topics"] == sorted(sha["topics"])
    assert "sha256" in sha["topics"]
