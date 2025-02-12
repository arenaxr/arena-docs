---
title: Capsule
layout: default
parent: Objects
grand_parent: Python Library
---

# Capsule

Draw a Capsule primitive mesh geometry. Capsule is a tube shape with rounded ends.

`arena-py` API Reference for [Capsule](/content/python-api/objects/capsule).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")


@scene.run_once
def make_box():
    my_cap = Capsule(
        object_id="my_cap",
        position=(0, 2, -3),
        material=Material(color=(50, 60, 200)),
    )
    scene.add_object(my_cap)


scene.run_tasks()
```
