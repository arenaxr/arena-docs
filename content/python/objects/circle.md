---
title: Circle
layout: default
parent: Objects
grand_parent: Python Library
---

# Circle

Draw a Circle primitive mesh geometry.

Additional Python properties are available in the [Circle API Reference](/content/python-api/objects/circle).

The following source code was mirrored from the `arena-py` [circle.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/circle.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_circle():
    my_circle = Circle(
        object_id="my_circle",
        position=(0, 2, -3),
        rotation=(-45, 0, 0),
        scale=(1, 1, 1),
        material=Material(color=(70, 0, 100)),
    )
    scene.add_object(my_circle)

scene.run_tasks()
```
