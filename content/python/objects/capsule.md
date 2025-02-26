---
title: Capsule
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Capsule

Draw a Capsule primitive mesh geometry. Capsule is a tube shape with rounded ends.

Additional Python properties are available in the [Capsule API Reference](/content/python-api/objects/capsule).

The following source code was mirrored from the `arena-py` [capsule.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/capsule.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_capsule():
    my_cap = Capsule(
        object_id="my_cap",
        position=(0, 2, -3),
        material=Material(color=(50, 60, 200)),
    )
    scene.add_object(my_cap)

scene.run_tasks()
```
