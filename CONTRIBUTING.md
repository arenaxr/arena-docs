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

## Local Development

To develop `arena-docs` locally:
1. Ensure Ruby and `bundler` are installed.
2. Run `bundle install` to install dependencies.
3. Serve the site locally with `bundle exec jekyll serve --livereload`.

## Code Style
- Use standard Markdown formatting.
- Guarantee that all front-matter contains the appropriate `title` and `nav_order`.

The `arena-docs` uses [Release Please](https://github.com/googleapis/release-please) to automate CHANGELOG generation and semantic versioning. Your PR titles *must* follow Conventional Commit standards (e.g., `feat:`, `fix:`, `chore:`).


## CI & Dependency Management Conventions
- **GitHub Actions Tag SHA Pinning**: All GitHub Action references in `.github/workflows/` MUST be pinned to the exact commit SHA of the official release tag (e.g., `uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4.4.0`).
- **Inline Version Comments**: The inline comment next to the SHA MUST specify the exact tag version used. This enables Dependabot to recognize the release version, generate human-readable SemVer PR titles (`from X.Y.Z to A.B.C`), and automatically update version comments during upgrades.