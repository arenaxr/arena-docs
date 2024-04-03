---
title: Scene Callbacks
nav_order: 6
layout: default
parent: Python Library
---

# ARENA Library Scene Callbacks

Library supported callback functions.

## Scene callbacks

### on_msg_callback

This is called whenever there is a new message sent to the client. Use this whenever you want to sniff out **all** incoming messages.

#### Usage:

```python
# [scene] is the Scene that called the callback
# [obj] will be an Object instance
# [msg] is the raw JSON message as a dict
def on_msg_callback(scene, obj, msg):
    ## do stuff with obj here
    obj.object_id
    obj.data.position.x
    obj.data.scale.y
    # etc.
    # could also do obj["object_id"] or msg["object_id"]

scene.on_msg_callback = on_msg_callback
```

### new_obj_callback

This is called whenever there is a new object that has been created in the scene,
one that the user does not have a reference to. Use this to make references to any
new objects that may appear during a programs lifetime. Also a good way to find camera ID's.

#### Usage:

```python
# [scene] is the Scene that called the callback
# [obj] will be an Object instance
# [msg] is the raw JSON message as a dict
def new_obj_callback(scene, obj, msg):
    ## do stuff with obj here
    obj.object_id
    obj.data.position.x
    obj.data.scale.y
    # etc.
    # could also do obj["object_id"] or msg["object_id"]

scene.new_obj_callback = new_obj_callback
```

### delete_obj_callback

This is called whenever there is an object has been deleted in the scene.
arena-py will look for all "action" = "delete" messages and call this callback.
Use this to delete references and to be notified when an object is removed by
another user or program.

#### Usage:

```python
# [scene] is the Scene that called the callback
# [obj] will be an Object instance
# [msg] is the raw JSON message as a dict
def delete_obj_callback(scene, obj, msg):
    ## do stuff with obj here
    obj.object_id
    obj.data.position.x
    obj.data.scale.y
    # etc.
    # could also do obj["object_id"] or msg["object_id"]

scene.delete_obj_callback = delete_obj_callback
```

### end_program_callback

This is called whenever the program is ending from the SIGINT, Crtl-C, or other kill process.
Use this to cleanup resources you don't want in the scene when the program ends.
This is especially useful for persisted objects use created that you want to be removed.

#### Usage:

```python
# [scene] is the Scene that called the callback
def end_program_callback(scene):
    ## do stuff with scene root objects here
    scene.delete_object(appParentObject)
    scene.delete_object(otherAppParentObject)
    print("App Terminated.")
    # etc.

scene.end_program_callback = end_program_callback
```

## User callbacks

### user_join_callback

This is called whenever the library detects/finds a new user that it hasn't seen before in a scene.
Note: this is not neccesarily called when a user "joins" a scene, rather, it is called when the library first sees a `Camera` object/receives an "update" message from a user.

#### Usage:

```python
def user_join_callback(camera):
    ## Get access to user state
    # camera is a Camera class instance (see Objects)
    camera.object_id
    camera.displayName
    camera.hasVideo
    camera.displayName
    # etc.

scene.user_join_callback = user_join_callback
```

### user_left_callback

This is called whenever a user leaves a scene/sends a delete message.

#### Usage:

```python
def user_left_callback(camera):
    ## Get access to user state
    # camera is a Camera class instance (see Objects)
    camera.object_id
    camera.displayName
    camera.hasVideo
    camera.displayName
    # etc.

scene.user_left_callback = user_left_callback
```

### Adding callbacks when you instantiate the class

You can also add callbacks like so:

```python
from arena import *

def on_msg_callback(scene, obj, msg):
    pass

def new_obj_callback(scene, obj, msg):
    pass

def delete_obj_callback(scene, obj, msg):
    pass

scene = Scene(..., on_msg_callback=on_msg_callback, new_obj_callback=new_obj_callback, delete_obj_callback=delete_obj_callback)
```

## Custom Message Callbacks

If you need to use an MQTT client, the `Scene` object exposes a way to use its MQTT client to subscribe to custom topics.

```python
def led_toggle(client, userdata, msg):
    # do stuff here

scene.message_callback_add("custom/control/light", led_toggle)
```
