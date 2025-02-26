---
title: BoxCollisionListener
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Box Collision Listener

Listen for bounding-box collisions with user camera and hands. Must be applied to an object or model with geometric mesh. Collisions are determined by course bounding-box overlaps.

Additional Python properties are available in the [BoxCollisionListener API Reference](/content/python-api/attributes/box_collision_listener).

The following source code was mirrored from the `arena-py` [box_collision_listener.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/box_collision_listener.py) example.

```python
from arena import *

scene = Scene(host="arena-dev1.conix.io", scene="example")

box_collision_listener = BoxCollisionListener(
    dynamic=False,
    enabled=True,
)

def box_event(scene, evt, msg):
    print(f"Event {evt.type} received on object {evt.object_id}!")
    if evt.type == "collision-start":
        # show green ball at point of collision start, center grey
        add_temp_ball(scene, evt["data"]["position"], "#00ff00")
        add_temp_ball(scene, evt["data"]["targetPosition"], "#777777")
    elif evt.type == "collision-end":
        # show red ball at point of collision end, center grey
        add_temp_ball(scene, evt["data"]["position"], "#ff0000")
        add_temp_ball(scene, evt["data"]["targetPosition"], "#777777")

def add_temp_ball(scene, position, color):
    scene.add_object(
        Sphere(
            ttl=1,
            position=position,
            scale=(0.05, 0.05, 0.05),
            material=Material(color=Color(color)),
        )
    )

@scene.run_once
def make_box_collider():
    box_collision = Box(
        object_id="box1",
        depth=1,
        height=1,
        width=3,
        position=(-3, 1, -2),
        material=Material(color="#b8ea2e", transparent=True, opacity=0.3),
        clickable=True,
        evt_handler=box_event,
        box_collision_listener=box_collision_listener,
    )
    scene.add_object(box_collision)

scene.run_tasks()
```
