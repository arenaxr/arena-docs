---
title: TorusKnot
layout: default
parent: Objects
grand_parent: Python Library
---

# Torus Knot

Draw a Torus Knot primitive mesh geometry. Torus Knot is tube shaped into a knot shape.

Instantiate a wacky torusKnot, then turn it blue. Other primitive types are available in the in [A-Frame docs](https://aframe.io/docs/1.5.0/components/geometry.html#built-in-geometries). Here is a brief list: **box circle cone cylinder dodecahedron icosahedron tetrahedron octahedron plane ring sphere torus torusKnot triangle**.

Additional Python properties are available in the [TorusKnot API Reference](/content/python-api/objects/torus_knot).

The following source code was mirrored from the `arena-py` [torus_knot.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus_knot.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_torus_knot():
    my_torusknot = TorusKnot(
        object_id="my_torusknot",
        position=(0, 5, -3),
        scale=(0.5, 0.5, 0.5),
        material=Material(color=(0, 100, 40)),
    )
    scene.add_object(my_torusknot)

scene.run_tasks()
```
