#!/usr/bin/env python3
import os
import shutil
from importlib.metadata import version
from pathlib import Path

from pdoc import pdoc, render

lib = "arena"
dest_dir = "python-api"
here = Path(__file__).parent
out = here / Path("../../content")
os.environ["PDOC-ARENA-PI-VERSION"] = version('arena-py')

render.configure(
    docformat='restructuredtext',
    include_undocumented=True,
    edit_url_map=None,
    favicon=None,
    footer_text='',
    logo=None,
    logo_link=None,
    math=False,
    mermaid=False,
    search=False,
    show_source=False,
    template_directory=here / "pdoc-template"
)
pdoc(lib, output_directory=out)
shutil.rmtree(out / dest_dir)

# next index files in api folder
shutil.move(out / "index.html", out / lib / "index.html")
shutil.move(out / f"{lib}.html", out / lib / f"{lib}.html")

# ...and rename the .html files to .md so that jekyll picks them up!
for f in out.glob("**/*.html"):
    f.rename(f.with_suffix(".md"))

# rename api folder
shutil.move(out / lib,  out / dest_dir)
