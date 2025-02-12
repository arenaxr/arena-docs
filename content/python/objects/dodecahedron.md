---
title: Dodecahedron
layout: default
parent: Objects
grand_parent: Python Library
---

# Dodecahedron

Draw a Dodecahedron primitive mesh geometry. Dodecahedron is 12-sided polyhedron shape.

`arena-py` API Reference for [Dodecahedron](/content/python-api/objects/dodecahedron).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_dod():
    dod = Dodecahedron(
        object_id="dod",
        position=(0, 2, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(30, 255, 80)),
    )
    scene.add_object(dod)

scene.run_tasks()
```
