---
title: GotoLandmark
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Goto Landmark

Teleports user to the landmark with the given name. Requires click-listener.

Additional Python properties are available in the [GotoLandmark API Reference](/content/python-api/attributes/goto_landmark).

The following source code was mirrored from the `arena-py` [goto_landmark.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_landmark.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

landmark_sky_object_id = "landmark_sky"
landmark_teleport_object_id = "landmark_teleport"
goto_landmark = GotoLandmark(
    landmark=landmark_sky_object_id,
    on="mousedown",
)

@scene.run_once
def make_landmark_teleport():
    landmark_sky = Object(
        object_id=landmark_sky_object_id,
        position=Position(0, 100, 0),
        landmark=Landmark(label="Sky High Location"),
    )
    scene.add_object(landmark_sky)

    landmark_teleport = Box(
        object_id=landmark_teleport_object_id,
        position=Position(0, 1, -3),
        material=Material(color="#0084ff", opacity=0.5, transparent=True),
        clickable=True,
        goto_landmark=goto_landmark,
    )
    scene.add_object(landmark_teleport)

scene.run_tasks()
```
