---
title: Plane
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Plane

Draw a Plane primitive mesh geometry. Plane is flat shape with 4 edges.

Additional Python properties are available in the [Plane API Reference](/content/python-api/objects/plane).

The following source code was mirrored from the `arena-py` [plane.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/plane.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_plane():
    my_plane = Plane(
        object_id="my_plane",
        position=(0, 5, -3),
        scale=(5, 5, 5),
        material=Material(color=(200, 200, 40)),
    )
    scene.add_object(my_plane)

scene.run_tasks()
```
