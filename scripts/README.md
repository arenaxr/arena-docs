# Documentation Generation Scripts

We have a few scripts to auto-generate some documentation for `arena-docs`. At any point after running these scripts you
can view the changes from the root of this repo:

- Run `make serve` to compile and run a localhost docs site (takes a few minutes).
- Run `make check` to run a link checker (also runs as a CI action).

## Python Examples from Docstrings

This script reads the `arena-py` examples in `arena-py/examples` and produces Markdown for those examples in
`arena-docs/content/python`, mimicking library folders.

1. Git pull latest `arena-py`, or git checkout by release tag.
1. Run `python3 ./scripts/pexamples/make-py_examples.py`
1. Git commit updated files in `arena-docs/content/python`.

## Python API from Docstrings

This script reads the Python main library docstrings in `arena-py/arena` and produces HTML/Markdown for API calls in
`arena-docs/content/python-api`, mimicking library folders.

This uses `pdoc` with [jekyll](https://jekyllrb.com) to generate our `arena-py` API docs.
This is derived from a [pdoc/mkdocs example](https://github.com/mitmproxy/pdoc/tree/main/examples/mkdocs).

1. Pip install the version of `arena-py` you want to generate api docs for.
1. Run `python3 ./scripts/pdoc/make-pdoc.py`
1. Git commit updated files in `arena-docs/content/python-api`.

### Implementation

The main trick is that we define a custom `frame.html.jinja2` template to
remove pdoc's usual HTML code around the main documentation contents.
We then invoke pdoc normally and rename the output files to `.md` so that they are picked up by jekyll.

### Limitations

- If you want to link between different pages in your documentation,
  pdoc requires `use_directory_urls: false` for linking to work.
- The `just-the-docs` theme, only renders 3 levels, so more nested Python will need another theme.

## JSON Message Schema

We do have scripts that also generate Markdown for JSON message schemas in `arena-docs/schemas/message`. See https://github.com/arenaxr/arena-schemas.
