---
title: Landmark
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Landmark

Creates a landmark that can be teleported to from the UI list, or is one of the random starting positions for the scene.

Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is constrained by a navmesh (when it exists).

Additional Python properties are available in the [Landmark API Reference](/content/python-api/attributes/landmark).

The following source code was mirrored from the `arena-py` [landmark.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/landmark.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

landmark = Landmark(
    label="Box 1",
    randomRadiusMin=1,
    randomRadiusMax=2,
    lookAtLandmark=True,
)

@scene.run_once
def make_box_landmark():
    scene.add_object(
        Box(
            object_id="box_1",
            position=(1, 1, -1),
            landmark=landmark,
        )
    )

scene.run_tasks()
```
