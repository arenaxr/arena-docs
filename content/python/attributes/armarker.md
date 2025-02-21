---
title: Armarker
layout: default
parent: Attributes
grand_parent: Python Library
---

# AR Marker

A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.

Additional Python properties are available in the [Armarker API Reference](/content/python-api/attributes/armarker).

The following source code was mirrored from the `arena-py` [armarker.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/armarker.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

armarker = Armarker(
    markerid="1",
    markertype="apriltag_36h11",
    size=50,
    buildable=False,
    dynamic=True,
)

@scene.run_once
def make_dynamic_box():
    dynamic_box = Box(
        object_id="dynamic_box",
        depth=0.05,
        height=0.05,
        width=0.05,
        position=Position(0, 1, 0),
        material=Material(color="#0084ff", opacity=0.5, transparent=True),
        armarker=armarker,
    )
    scene.add_object(dynamic_box)

scene.run_tasks()
```
