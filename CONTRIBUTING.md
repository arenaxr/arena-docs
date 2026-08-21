# Contributing to ARENA Docs

The general Contribution Guide for all ARENA projects can be found [here](https://docs.arenaxr.org/content/contributing.html).

This document covers **development rules and conventions** specific to this repository. These rules are mandatory for all contributors, including automated/agentic coding tools.

## Development Rules

### 1. MQTT Topics — Always Use the `TOPICS` Constructor

**Never hardcode MQTT topic strings.** All topic paths must be constructed using the local `TOPICS` string constructor for ease of future topics modulation. This enables future topic format refactoring without scattered string updates.

### 2. Dependencies — Pin All Versions

**All dependencies must use exact, pegged versions** (no `^`, `~`, or `*` ranges). This prevents version drift across environments and ensures reproducible builds for security.

## Content Creation Directives

ARENA Documentation pages are written in markdown and placed in the `content` directory, except for `./index.md`.

Each `.md` file inside `content` must have [YAML Front Matter](https://jekyllrb.com/docs/front-matter) for navigation. The navigation details are determined by our theme. See the [just-the-docs](https://github.com/just-the-docs/just-the-docs/blob/main/docs/navigation-structure.md) theme for more details about site navigation.

### Generated Pages — Do Not Hand-Edit

The pages under `content/python/` and `content/python-api/` are **generated from `arena-py`** by the scripts in [`scripts/`](scripts/README.md) — from its `examples/` sources and its library docstrings respectively. An edit made directly to one of these files is silently lost the next time a maintainer regenerates them, so fix the example or docstring in `arena-py` instead and ask for a regeneration. Generated files carry one of these markers near the top, naming the script that produced them — `pexample` under `content/python/`, `pdoc` under `content/python-api/`:

```markdown
<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->
<!-- This file is auto-generated from github.com/arena-docs/scripts/pdoc, changes here may be overwritten. -->
```

The hand-written exceptions in these directories are the `index.md` navigation pages, the `content/python/tutorial/` pages, and `content/python/animations.md`, `content/python/events.md` and `content/python/tasks.md`.

## Local Development

To develop `arena-docs` locally:
1. Ensure Ruby (the version in `.ruby-version`) and `bundler` are installed.
2. Run `make install` to install dependencies into `_vendor/bundle`.
3. Run `make serve` and preview the site at [http://localhost:4000/](http://localhost:4000/).

## Checks Before You Open a Pull Request

**Nothing runs on pull requests in this repository.** The [Pages workflow](.github/workflows/github-pages.yml) is triggered only by a `push` to `master` (or a manual `workflow_dispatch`), so the Jekyll build and the HTMLProofer link check run *after* your change is merged and live. Running them yourself is the only pre-merge signal:

```bash
# Full site build — the same `jekyll build` CI runs after merge (takes a few minutes)
make build

# jekyll doctor plus the HTMLProofer link check
LC_ALL=C.UTF-8 make check
```

`make check` requires a UTF-8 locale. With `LANG`/`LC_ALL` unset — common in containers and minimal shells — HTMLProofer aborts with `Encoding::InvalidByteSequenceError: "\xE2" on US-ASCII` as soon as it parses a page containing a smart quote or em dash. Setting `LC_ALL=C.UTF-8` for the command is enough.

## Code Style
- Use standard Markdown formatting.
- Guarantee that all front-matter contains the appropriate `title` and `nav_order`.

The `arena-docs` uses [Release Please](https://github.com/googleapis/release-please) to automate CHANGELOG generation and semantic versioning. Your PR titles *must* follow Conventional Commit standards (e.g., `feat:`, `fix:`, `chore:`).

> [!CAUTION]
> **Never use `BREAKING CHANGE` in commit/PR bodies or the `!` suffix on commit/PR types (e.g., `feat!:`, `fix!:`).** These tokens cause release-please to automatically bump the major version. Major version increments are reserved for the maintainer's explicit decision — contributors and agents do not decide what constitutes a breaking change for semver purposes.

> [!IMPORTANT]
> **Issue and PR References in Commit & PR Messages:**
> Only use `#NN` notation in commit messages, PR titles, and PR descriptions if they correspond to actual GitHub issues or pull requests. Do **not** use `#NN` notation for internal enumerations of planning docs or triage items (e.g., use `Task NN` or plain text instead), as this creates erroneous links and may result in unintended automatic actions.


## CI & Dependency Management Conventions
- **GitHub Actions Tag SHA Pinning**: All GitHub Action references in `.github/workflows/` MUST be pinned to the exact commit SHA of the official release tag (e.g., `uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4.4.0`).
- **Inline Version Comments**: The inline comment next to the SHA MUST specify the exact tag version used. This enables Dependabot to recognize the release version, generate human-readable SemVer PR titles (`from X.Y.Z to A.B.C`), and automatically update version comments during upgrades.