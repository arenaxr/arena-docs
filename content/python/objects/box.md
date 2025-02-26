---
title: Box
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Box

Draw a Box primitive mesh geometry. Box is 6-sided polyhedron shape.

Instantiate a box and set all of it's basic parameters.

Additional Python properties are available in the [Box API Reference](/content/python-api/objects/box).

The following source code was mirrored from the `arena-py` [box.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/box.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    my_box = Box(
        object_id="my_box",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(50, 60, 200)),
    )
    scene.add_object(my_box)

scene.run_tasks()
```
