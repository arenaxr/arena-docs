---
title: Box
layout: default
parent: Objects
grand_parent: Python Library
---

# Box

Draw a Box primitive mesh geometry. Box is 6-sided polyhedron shape.

Instantiate a box and set all of it's basic parameters.

`arena-py` API Reference for [Box](/content/python-api/objects/box).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    my_box = Box(
        object_id="my_box",
        position=(0, 2, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(50, 60, 200)),
    )
    scene.add_object(my_box)

scene.run_tasks()
```
