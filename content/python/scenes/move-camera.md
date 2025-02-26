---
title: MoveCamera
layout: default
parent: Scenes
grand_parent: Python Library
---

# Move Camera

Move cameras to a random location.

The following source code was mirrored from the `arena-py` [move-camera.py](https://github.com/arenaxr/arena-py/blob/master/examples/scenes/move-camera.py) example.

```python
import random

from arena import *

def rando():
    return float(random.randint(-100000, 100000)) / 1000

def user_join_callback(camera):
    print(f"User found: {camera.displayName} [object_id={camera.object_id}]")

scene = Scene(host="arenaxr.org", scene="test")
scene.user_join_callback = user_join_callback

# box = Box(object_id="box")
# scene.add_object(box)

@scene.run_forever(interval_ms=500)
def move_cams():
    for c in scene.users:
        scene.manipulate_camera(
            c,
            position=(rando(),1.6,rando()),
            rotation=(0,0,0,1)
        )
        scene.look_at(
            c,
            target=(0,0,0)
        )

scene.run_tasks()
```
