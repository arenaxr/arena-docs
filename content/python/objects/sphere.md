---
title: Sphere
layout: default
parent: Objects
grand_parent: Python Library
---

# Sphere

Draw a Sphere primitive mesh geometry. Sphere is completely round shape.

`arena-py` API Reference for [Sphere](/content/python-api/objects/sphere).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")


@scene.run_once
def make_sphere():
    my_sphere = Sphere(
        object_id="my_sphere",
        position=(0, 2, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(0, 255, 255)),
    )
    scene.add_object(my_sphere)


scene.run_tasks()
```
