---
title: Octahedron
layout: default
parent: Objects
grand_parent: Python Library
---

# Octahedron

Draw a Octahedron primitive mesh geometry. Octahedron is 8-sided polyhedron shape.

`arena-py` API Reference for [Octahedron](/content/python-api/objects/octahedron).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")


@scene.run_once
def make_oct():
    my_oct = Octahedron(
        object_id="my_oct",
        position=(0, 2, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(30, 100, 40)),
    )
    scene.add_object(my_oct)


scene.run_tasks()
```
