#!/usr/bin/env python3
import os
from pathlib import Path

from caseconverter import pascalcase

add_api = True


def create_python_markdown(folder, add_api=False):
    # clear for updated markdown
    write_dir = f"./content/python/{folder}"
    for subdir, dirs, files in os.walk(write_dir):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                os.remove(f"{write_dir}/{file}")

    # read python and then write updated markdown
    read_dir = f"../arena-py/examples/{folder}"
    for subdir, dirs, files in os.walk(read_dir):
        for file in files:
            if file.endswith((".py")):
                with open(f"{read_dir}/{file}", "r", encoding="utf8") as rfile:
                    path = Path(file)
                    filename = f"{write_dir}/{path.stem}.md"
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    wfile = open(filename, "w", encoding="utf8")
                    wfile.write("---\n")
                    wfile.write(f"title: {pascalcase(path.stem)}\n")
                    wfile.write("layout: default\n")
                    wfile.write(f"parent: {pascalcase(folder)}\n")
                    wfile.write("grand_parent: Python Library\n")
                    wfile.write("---\n\n")
                    wfile.write("<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->\n\n")
                    module_docstring = True
                    last_line = None
                    for line in rfile:
                        if line.startswith("'''") or line.startswith('"""'):
                            if module_docstring:
                                wfile.write(f"# {line[3:]}")
                                module_docstring = False
                            else:
                                if add_api:
                                    wfile.write(
                                        f"\nAdditional Python properties are available in the [{pascalcase(path.stem)} API Reference](/content/python-api/{folder}/{path.stem}).\n"
                                    )
                                wfile.write(
                                    f"\nThe following source code was mirrored from the `arena-py` [{file}](https://github.com/arenaxr/arena-py/blob/master/examples/{folder}/{file}) example.\n"
                                )
                                wfile.write("\n```python")
                        elif line != last_line:
                            wfile.write(line)
                        last_line = line
                    wfile.write("```\n")
                    wfile.close()

    filename = f"{write_dir}/index.md"
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        wfile = open(filename, "w", encoding="utf8")
        wfile.write("---\n")
        wfile.write(f"title: {pascalcase(folder)}\n")
        wfile.write("layout: default\n")
        wfile.write("has_children: true\n")
        wfile.write("parent: Python Library\n")
        wfile.write("---\n\n")
        wfile.write(f"# {pascalcase(folder)}\n\n")


create_python_markdown("basic")
create_python_markdown("scenes")
create_python_markdown("callbacks")
create_python_markdown("objects", add_api)
create_python_markdown("attributes", add_api)
create_python_markdown("simple")
