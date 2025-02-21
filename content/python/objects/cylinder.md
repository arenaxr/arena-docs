---
title: Cylinder
layout: default
parent: Objects
grand_parent: Python Library
---

# Cylinder

Draw a Cylinder primitive mesh geometry. Cylinder is a tube shape with flat ends.

Additional Python properties are available in the [Cylinder API Reference](/content/python-api/objects/cylinder).

The following source code was mirrored from the `arena-py` [cylinder.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/cylinder.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_cylinder():
    my_cylinder = Cylinder(
        object_id="my_cylinder",
        position=(0, 2, -3),
        scale=(1, 2, 1),
        material=Material(color=(255, 100, 16)),
    )
    scene.add_object(my_cylinder)

scene.run_tasks()
```
