---
title: Scene Callbacks
nav_order: 6
layout: default
parent: Python Library
---

# Arena Library Message Callbacks

Library supported callback functions.

## Scene callbacks

### on_msg_callback
This is called whenever there is a new message sent to the client. Use this whenever you want to sniff out all incoming messages.

#### Usage:
```python
def on_msg_callback(msg):
    # msg will be a python dictionary not an ARENA-py object (for now)
    # do stuff with msg here
    # msg["object_id"], msg["data"], etc

scene.on_msg_callback = on_msg_callback
```

### new_obj_callback
This is called whenever there is a new object that has been created in the scene,
one that the user does not have a reference to. Use this to make references to any
new objects that may appear during a programs lifetime. Also a good way to find camera ID's.

#### Usage:
```python
def new_obj_callback(msg):
    # msg will be a python dictionary not an ARENA-py object (for now)
    # do stuff with msg here
    # msg["object_id"], msg["data"], etc

scene.new_obj_callback = new_obj_callback
```

### delete_obj_callback
This is called whenever there is an object has been deleted in the scene.
ARENA-py will look for all "action" = "delete" messages and call this callback.
Use this to delete references and to be notified when an object is removed by
another user or program.

#### Usage:
```python
def delete_obj_callback(msg):
    # msg will be a python dictionary not an ARENA-py object (for now)
    # do stuff with msg here
    # msg["object_id"], etc
    #
    # usually, msg will be:
    # {
    #   "object_id": "[deleted object id here]",
    #   "action": "delete"
    # }

scene.delete_obj_callback = delete_obj_callback
```

## User callbacks

### user_join_callback
This is called whenever the library detects/finds a new user that it hasn't seen before in a scene.

#### Usage:
```python
def user_join_callback(camera):
    # camera is a Camera class instance (see Objects)
    # camera.object_id
    # camera.displayName
    # etc.

scene.user_join_callback = user_join_callback
```

### user_left_callback
This is called whenever a user leaves a scene/sends a delete message.

#### Usage:
```python
def user_left_callback(camera):
    # camera is a Camera class instance (see Objects)
    # camera.object_id
    # camera.displayName
    # etc.

scene.user_left_callback = user_left_callback
```

### Adding callbacks when you instantiate the class
You can also add callbacks like so:
```python
from arena import *

def on_msg_callback(msg):
    pass

def new_obj_callback(msg):
    pass

def delete_obj_callback(msg):
    pass

scene = Scene(..., on_msg_callback=on_msg_callback, new_obj_callback=new_obj_callback, delete_obj_callback=delete_obj_callback)
```
