#!/usr/bin/env python3
from pathlib import Path
import shutil
import os

from pdoc import pdoc
from pdoc import render

import arena

lib = "arena"
here = Path(__file__).parent
out = here / Path("../../content")
os.environ["PDOC-ARENA-PI-VERSION"] = arena.__version__

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

shutil.move(out / "index.html", out / lib / "index.html")
shutil.move(out / f"{lib}.html", out / lib / f"{lib}.html")

# ...and rename the .html files to .md so that jekyll picks them up!
for f in out.glob("**/*.html"):
    f.rename(f.with_suffix(".md"))
