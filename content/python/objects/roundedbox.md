---
title: Roundedbox
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Rounded Box

Draw a Rounded Box primitive mesh geometry. Rounded Box is 6-sided polyhedron shape with rounded edges.

Additional Python properties are available in the [Roundedbox API Reference](/content/python-api/objects/roundedbox).

The following source code was mirrored from the `arena-py` [roundedbox.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/roundedbox.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_rounded_box():
    my_box = Roundedbox(
        object_id="my_box",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(50, 60, 200)),
        radius=0.25,
    )
    scene.add_object(my_box)

scene.run_tasks()
```
