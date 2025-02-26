---
title: Color
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Color

Change only the color of the already-drawn box.

Additional Python properties are available in the [Color API Reference](/content/python-api/attributes/color).

The following source code was mirrored from the `arena-py` [color.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/color.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

color = (100, 200, 100)  # Color(100,200,100) works too

@scene.run_once
def make_colored_icosahedron():
    my_iso = Icosahedron(
        object_id="my_iso",
        position=(0, 2, -5),
        material=Material(color=color),
    )
    scene.add_object(my_iso)

scene.run_tasks()
```
