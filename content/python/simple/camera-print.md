---
title: CameraPrint
layout: default
parent: Simple
grand_parent: Python Library
---

# Camera Tracer

Camera tracing program. Draws a path that follows the user.

```python
import random

from arena import *

MIN_DISPLACEMENT = 0.5
LINE_TTL = 5

class CameraState(Object):
    def __init__(self, camera):
        self.camera = camera
        self.prev_pos = None
        self.line_color = Color(
                random.randint(0,255),
                random.randint(0,255)
            )

    @property
    def curr_pos(self):
        return self.camera.data.position

    @property
    def id(self):
        return self.camera.object_id

    @property
    def curr_rot(self):
        return self.camera.data.rotation

    @property
    def displacement(self):
        if self.prev_pos:
            return self.prev_pos.distance_to(self.curr_pos)
        else:
            return 0

cam_states = []

def user_join_callback(scene, cam, msg):
    global cam_states

    cam_state = CameraState(cam)
    cam_states += [cam_state]

scene = Scene(host="arenaxr.org", scene="example")
scene.user_join_callback = user_join_callback

@scene.run_forever(interval_ms=200)
def line_follow():
    for cam_state in cam_states:
        print(cam_state.id, cam_state.curr_pos, cam_state.curr_rot)

scene.run_tasks() # will block
```
