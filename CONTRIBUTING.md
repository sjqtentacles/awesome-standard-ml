# Contributing

Thanks for helping grow **awesome-standard-ml**!

## Important: do not edit `README.md` directly

`README.md` is **generated**. Everything between the markers

```
<!-- BEGIN GENERATED -->
...
<!-- END GENERATED -->
```

is produced by [`scripts/generate.py`](scripts/generate.py) from data files in
[`data/`](data/). Hand-edits inside that block will be overwritten on the next
regeneration (and CI will fail the "README in sync" check). Edit the data
instead.

## Adding or editing an entry

### A community resource (compiler, book, course, non-sjqtentacles tool)

Edit [`data/community.yml`](data/community.yml). Each section is a list of
entries with a `name`, `url`, and `description`.

### A sjqtentacles ecosystem library

You normally do **not** edit these by hand: they are harvested automatically
from the GitHub org by [`scripts/harvest.py`](scripts/harvest.py), which reads
each repo's description and topics. To change how a library appears:

- Fix the repo's **description** or **topics** on GitHub (preferred), then let
  the weekly job re-harvest; or
- Add a per-repo **override** in [`data/categories.yml`](data/categories.yml)
  under `overrides:` if a library is mis-categorized.

### Adding or reordering a category

Edit the `categories:` list in [`data/categories.yml`](data/categories.yml).
A library lands in the **first** category (by list order) whose topics match,
so order matters. The `Misc` category is a safety net only; if a library lands
there, add a topic mapping or an override rather than leaving it.

## Regenerating and testing locally

```sh
pip install -r requirements.txt
python scripts/harvest.py          # re-fetch ecosystem data (needs gh, network)
python scripts/generate.py         # rewrite README.md from data
python scripts/generate.py --check # verify README is in sync (exit 1 if stale)
pytest                             # run the generator/harvest unit tests
```

Open a PR with your change to `data/` (and the regenerated `README.md` if you
ran `generate.py`). CI will re-check sync, run the tests, and lint the list.
