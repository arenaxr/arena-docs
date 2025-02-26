---
title: Dodecahedron
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Dodecahedron

Draw a Dodecahedron primitive mesh geometry. Dodecahedron is 12-sided polyhedron shape.

Additional Python properties are available in the [Dodecahedron API Reference](/content/python-api/objects/dodecahedron).

The following source code was mirrored from the `arena-py` [dodecahedron.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/dodecahedron.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_dodecahedron():
    dod = Dodecahedron(
        object_id="dod",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(30, 255, 80)),
    )
    scene.add_object(dod)

scene.run_tasks()
```
