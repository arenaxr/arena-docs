---
title: UserCallbacks
layout: default
parent: Callbacks
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# User Callbacks

`scene.user_join_callback` is called whenever the library detects/finds a new user that it hasn't seen before in a scene.
Note: this is not necessarily called when a user "joins" a scene, rather, it is called when the library first sees a `Camera` object/receives an "update" message from a user.

`scene.user_left_callback` is called whenever a user leaves a scene/sends a delete message.

The following source code was mirrored from the `arena-py` [user_callbacks.py](https://github.com/arenaxr/arena-py/blob/master/examples/callbacks/user_callbacks.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

def user_join_callback(scene, camera, msg):
    print(f"User found: {camera.displayName} [object_id={camera.object_id}]")
    ##Get access to user state
    # camera is a Camera class instance (see Objects)
    # etc.

def user_left_callback(scene, camera, msg):
    print(f"User left: {camera.displayName} [object_id={camera.object_id}]")
    # Get access to user state
    # camera is a Camera class instance (see Objects)
    # etc.

scene.user_join_callback = user_join_callback
scene.user_left_callback = user_left_callback
```
