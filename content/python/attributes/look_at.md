---
title: LookAt
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Look At

The look-at component defines the behavior for an entity to dynamically rotate or face towards another entity or position. Use `#my-camera` to face the user camera, otherwise can take either a vec3 position or a query selector to another entity.

Make object `look-at` the camera:
```python
look_at="#my-camera"
```
or make object `look-at` at a position
```python
look_at="0 0 0"
```

Additional Python properties are available in the [LookAt API Reference](/content/python-api/attributes/look_at).

The following source code was mirrored from the `arena-py` [look_at.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/look_at.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_rotating_image():
    rotating_image = Image(
        object_id="rotating_image",
        url="store/users/wiselab/images/conix-face-white.jpg",
        position=Position(1, 2, -2),
        look_at="#my-camera",
    )
    scene.add_object(rotating_image)

scene.run_tasks()
```
