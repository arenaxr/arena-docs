---
title: Tetrahedron
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Tetrahedron

Draw a Tetrahedron primitive mesh geometry. Tetrahedron is 4-sided polyhedron shape.

Additional Python properties are available in the [Tetrahedron API Reference](/content/python-api/objects/tetrahedron).

The following source code was mirrored from the `arena-py` [tetrahedron.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/tetrahedron.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_tetrahedron():
    my_tet = Tetrahedron(
        object_id="my_tet",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(255, 100, 255)),
    )
    scene.add_object(my_tet)

scene.run_tasks()
```
