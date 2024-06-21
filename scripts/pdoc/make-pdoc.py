#!/usr/bin/env python3
import fnmatch
import os
import shutil
from importlib.metadata import version
from pathlib import Path

from pdoc import pdoc, render


def grep_all_files(root_dir, str_find, str_replace, file_pattern):
    for path, _, files in os.walk(os.path.abspath(root_dir)):
        for filename in fnmatch.filter(files, file_pattern):
            filepath = os.path.join(path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                s = f.read()
            s = s.replace(str_find, str_replace)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(s)


lib = "arena"
dest_dir = "python-api"
here = Path(__file__).parent
out = here / Path("../../content")
os.environ["PDOC-ARENA-PI-VERSION"] = version('arena-py')

# https://pdoc.dev/docs/pdoc/render.html#configure
render.configure(
    docformat='restructuredtext',
    # include_undocumented=True,
    # edit_url_map={lib: f"https://github.com/arenaxr/arena-py/tree/v{version('arena-py')}/arena/"}, # TODO(mwfarb): fix clickable region
    # favicon=None,
    # footer_text=f"arena-py API v{version('arena-py')}",
    # logo=None,
    # logo_link=None,
    # math=False,
    # mermaid=False,
    search=False,
    show_source=False,
    template_directory=here / "pdoc-template"
)
pdoc(lib, output_directory=out)
shutil.rmtree(out / dest_dir)

grep_all_files(out, "/../arena.html", "/arena.html", "*.html")

# nest index files in api folder
shutil.move(out / "index.html", out / lib / "index.html")
shutil.move(out / f"{lib}.html", out / lib / f"{lib}.html")

# ...and rename the .html files to .md so that jekyll picks them up!
for f in out.glob("**/*.html"):
    f.rename(f.with_suffix(".md"))

# rename api folder
shutil.move(out / lib,  out / dest_dir)
