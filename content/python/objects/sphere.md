---
title: Sphere
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Sphere

Draw a Sphere primitive mesh geometry. Sphere is completely round shape.

Additional Python properties are available in the [Sphere API Reference](/content/python-api/objects/sphere).

The following source code was mirrored from the `arena-py` [sphere.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/sphere.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_sphere():
    my_sphere = Sphere(
        object_id="my_sphere",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(0, 255, 255)),
    )
    scene.add_object(my_sphere)

scene.run_tasks()
```
