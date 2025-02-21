---
title: LaserPointer
layout: default
parent: Simple
grand_parent: Python Library
---

# Laser Pointer

The following source code was mirrored from the `arena-py` [laser-pointer.py](https://github.com/arenaxr/arena-py/blob/master/examples/simple/laser-pointer.py) example.

```python
import random

from arena import *

scene = Scene(host="arenaxr.org", scene="example")

def click(scene, evt, msg):
    if evt.type == "mousedown":
        # print("Click!")
        start = evt.data.originPosition
        end = evt.data.targetPosition
        start.y=start.y-.1
        start.x=start.x-.1
        start.z=start.z-.1
        line = ThickLine(path=(start,end), color=(255,0,0), lineWidth=5, ttl=1)
        scene.add_object(line)
        ball = Sphere(
            position=end,
            scale = (0.06,0.06,0.06),
            color=(255,0,0),
            ttl=1)
        scene.add_object(ball)

@scene.run_once
def make_objects_laser_clickable():
    objs = scene.get_persisted_objs()
    for obj_id,obj in objs.items():
        # obj.update_attributes(clickable=True)
        try:
            if obj.clickable:
                obj.update_attributes(evt_handler=click)
                scene.update_object(obj)
                print("Clickable: ", obj_id)
        except AttributeError:
            print("Skipped: ", obj_id)
            pass

scene.run_tasks()
```
