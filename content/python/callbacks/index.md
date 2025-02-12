---
title: Callbacks
nav_order: 1.6
layout: default
has_children: true
parent: Python Library
---

# ARENA Library Scene Callbacks

Library supported callback functions.

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

## Scene callbacks

There are a number of scene callbacks you can use in the table of contents below.
