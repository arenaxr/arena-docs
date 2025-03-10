---
title: Octahedron
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Octahedron

Draw a Octahedron primitive mesh geometry. Octahedron is 8-sided polyhedron shape.

Additional Python properties are available in the [Octahedron API Reference](/content/python-api/objects/octahedron).

The following source code was mirrored from the `arena-py` [octahedron.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/octahedron.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_octahedron():
    my_oct = Octahedron(
        object_id="my_oct",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(30, 100, 40)),
    )
    scene.add_object(my_oct)

scene.run_tasks()
```
