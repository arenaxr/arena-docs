---
title: Videosphere
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Videosphere

Draw a sphere geometry, set the texture src to be an equirectangular video, on the 'back' (inside).

Additional Python properties are available in the [Videosphere API Reference](/content/python-api/objects/videosphere).

The following source code was mirrored from the `arena-py` [videosphere.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/videosphere.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_videosphere():
    my_videosphere = Videosphere(
        object_id="my_videosphere",
        position=(0, 0, 0),
        radius=150,
        src="store/users/wiselab/images/360falls.mp4",
    )
    scene.add_object(my_videosphere)

scene.run_tasks()
```
