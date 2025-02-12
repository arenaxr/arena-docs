---
title: Roundedbox
layout: default
parent: Objects
grand_parent: Python Library
---

# Rounded Box

Draw a Rounded Box primitive mesh geometry. Rounded Box is 6-sided polyhedron shape with rounded edges.

`arena-py` API Reference for [Roundedbox](/content/python-api/objects/roundedbox).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    my_box = Roundedbox(
        object_id="my_box",
        position=(0, 2, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(50, 60, 200)),
        radius=0.25,
    )
    scene.add_object(my_box)

scene.run_tasks()
```
