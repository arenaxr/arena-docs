---
title: Blip
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Blip Effect

When the object is created or deleted, it will animate in/out of the scene instead of appearing/disappearing instantly. Must have a geometric mesh.

Additional Python properties are available in the [Blip API Reference](/content/python-api/attributes/blip).

The following source code was mirrored from the `arena-py` [blip.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/blip.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

blip = Blip(
    blipin=True,
    blipout=True,
    geometry="disk",
    planes="top",
    duration=500,
)

@scene.run_once
def make_blip_robot():
    blip_robot = GLTF(
        object_id="blip_robot",
        url="/store/models/robot-draco.glb",
        position=Position(-2, 2, -2),
        rotation=Rotation(0.21644, 0, 0, 0.9763),
        material=Material(color="#0084ff", opacity=0.5, transparent=True),
        blip=blip,
    )
    scene.add_object(blip_robot)

scene.run_tasks()
```
