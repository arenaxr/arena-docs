---
title: Circle
layout: default
parent: Objects
grand_parent: Python Library
---

# Circle

Draw a Circle primitive mesh geometry.

`arena-py` API Reference for [Circle](/content/python-api/objects/circle).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_circle():
    my_circle = Circle(
        object_id="my_circle",
        position=(0, 2, -3),
        rotation=(-45, 0, 0),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(70, 0, 100)),
    )
    scene.add_object(my_circle)

scene.run_tasks()
```
