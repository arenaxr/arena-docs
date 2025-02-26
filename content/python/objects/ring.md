---
title: Ring
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Ring

Draw a Ring primitive mesh geometry. Ring is flat rounded shape with 2 edges, inner and outer.

Additional Python properties are available in the [Ring API Reference](/content/python-api/objects/ring).

The following source code was mirrored from the `arena-py` [ring.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/ring.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_ring():
    my_ring = Ring(
        object_id="my_ring",
        position=(0, 2, -3),
        scale=(1, 1, 1),
        material=Material(color=(255, 0, 255)),
    )
    scene.add_object(my_ring)

scene.run_tasks()
```
