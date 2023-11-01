# jekyll with pdoc

This is an example showing how to use pdoc with [jekyll](https://jekyllrb.com) to generate our `arena-py` API docs.
This is derived from a [pdoc/mkdocs example](https://github.com/mitmproxy/pdoc/tree/main/examples/mkdocs).
Run `./scripts/pdoc/make-pdoc.py` to generate the API documentation and then `make serve` to view this website!

## Implementation

The main trick is that we define a custom `frame.html.jinja2` template to
remove pdoc's usual HTML code around the main documentation contents.
We then invoke pdoc normally and rename the output files to `.md` so that they are picked up by jekyll.

## Limitations

 - If you want to link between different pages in your documentation,
   pdoc requires `use_directory_urls: false` for linking to work.
 - The `just-the-docs` theme, only renders 3 levels, so more nested Python will need another theme.
