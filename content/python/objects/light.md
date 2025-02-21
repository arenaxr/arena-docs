---
title: Light
layout: default
parent: Objects
grand_parent: Python Library
---

# Lights

A light.

More properties at <a href='https://aframe.io/docs/1.5.0/components/light.html'>A-Frame Light</a>.

Create a red light in the scene.

Default is ambient light. To change type, or other light [A-Frame Light](https://aframe.io/docs/0.9.0/components/light.html) parameters, example: change to **directional**. Options: **ambient, directional, hemisphere, point, spot**.

Additional Python properties are available in the [Light API Reference](/content/python-api/objects/light).

The following source code was mirrored from the `arena-py` [light.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/light.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_light():
    light = Light(
        object_id="my_light",
        type="point",
        position=(0, 2, -3),
        rotation=(0.25, 0.25, 0, 1),
        scale=(1.5, 1.5, 1.5),
        color=(255, 0, 0),
    )
    scene.add_object(light)

scene.run_tasks()
```
