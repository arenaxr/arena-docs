---
title: EarthMoonSimple
layout: default
parent: Simple
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Earth Moon Simple

Simple program to animate the earth and moon.

The following source code was mirrored from the `arena-py` [earth-moon-simple.py](https://github.com/arenaxr/arena-py/blob/master/examples/simple/earth-moon-simple.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")
earth = GLTF(
    object_id="gltf-model_Earth",
    scale=(10, 10, 10),
    url="store/users/wiselab/models/Earth.glb",
    animation=Animation(
        property="rotation", end=(0, 360, 0), loop=True, dur=20000, easing="linear"
    ),
)
moon = GLTF(
    object_id="gltf-model_Moon",
    position=(0, 0.05, 0.6),
    scale=(0.05, 0.05, 0.05),
    url="store/users/wiselab/models/Moon.glb",
    parent="gltf-model_Earth",
    animation=Animation(
        property="scale",
        start=(0.05, 0.05, 0.05),
        end=(0.1, 0.1, 0.1),
        startEvents="click",
        loop=6,
        dur=1000,
        dir="alternate",
        easing="easeInOutCirc",
    ),
)
scene.add_object(earth)
scene.add_object(moon)
scene.run_tasks()
```
