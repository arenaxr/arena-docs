#!/usr/bin/env python3
import os
from pathlib import Path

from caseconverter import pascalcase

add_api = True


def create_python_markdown(folder, add_api=False):
    read_dir = f"../arena-py/examples/{folder}"
    write_dir = f"./content/python/{folder}"
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
                    wfile.write(f"parent: {pascalcase(folder)}\n")
                    wfile.write("grand_parent: Python Library\n")
                    wfile.write("---\n\n")
                    python_started = False
                    module_docstring = False
                    for line in rfile:
                        if line.startswith("'''") or line.startswith('"""'):
                            if not module_docstring:
                                wfile.write(f"# {line[3:]}")
                                module_docstring = True
                            else:
                                module_docstring = False
                                python_started = True
                        else:
                            if not python_started:
                                if add_api:
                                    wfile.write(f"\n`arena-py` API Reference for [{pascalcase(path.stem)}](/content/python-api/{folder}/{path.stem}).\n")
                                wfile.write("\n```python")
                                python_started = False

                            wfile.write(line)
                    wfile.write("```\n")
                    wfile.close()

    filename = f"{write_dir}/index.md"
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        wfile = open(filename, "w", encoding="utf8")
        wfile.write("---\n")
        wfile.write(f"title: {pascalcase(folder)}\n")
        wfile.write("has_children: true\n")
        wfile.write("parent: Python Library\n")
        wfile.write("---\n\n")
        wfile.write(f"# {pascalcase(folder)}\n\n")


create_python_markdown("basic")
create_python_markdown("objects", add_api)
create_python_markdown("attributes", add_api)
create_python_markdown("simple")
