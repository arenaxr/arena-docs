---
title: Plane
layout: default
parent: Objects
grand_parent: Python Library
---

# Plane

Draw a Plane primitive mesh geometry. Plane is flat shape with 4 edges.

`arena-py` API Reference for [Plane](/content/python-api/objects/plane).

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
