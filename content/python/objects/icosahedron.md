---
title: Icosahedron
layout: default
parent: Objects
grand_parent: Python Library
---

# Icosahedron

Draw a Icosahedron primitive mesh geometry. Icosahedron is 20-sided polyhedron shape.

Additional Python properties are available in the [Icosahedron API Reference](/content/python-api/objects/icosahedron).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_iso():
    iso = Icosahedron(
        object_id="iso",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(10, 60, 255)),
    )
    scene.add_object(iso)

scene.run_tasks()
```
