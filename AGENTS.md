# Agent Guide

Orientation for agents (and humans) working in this repo. Detailed docs live in the files below — this file is just the index.

## Start here
- [README.md](README.md) — what arena-docs is and its primary components.

## Conventions & development rules
- [CONTRIBUTING.md](CONTRIBUTING.md) — mandatory rules for all contributors, including dependency version pinning and CI standards.

## Verifying a change
- **Nothing runs on pull requests** — the Jekyll build and the HTMLProofer link check are triggered only by a push to `master` (or a manual `workflow_dispatch`), after merge. Run `make build` and `LC_ALL=C.UTF-8 make check` locally first; `make check` needs the UTF-8 locale or it aborts on non-ASCII characters. See "Checks Before You Open a Pull Request" in [CONTRIBUTING.md](CONTRIBUTING.md).

## Generated content — do not hand-edit
- [scripts/README.md](https://github.com/arenaxr/arena-docs/blob/master/scripts/README.md) — `content/python/` and `content/python-api/` are generated from `arena-py` examples and docstrings. Edits to a generated page are overwritten on the next regeneration; change the source in `arena-py` instead. Generated files carry an `<!-- This file is auto-generated ... -->` comment.
