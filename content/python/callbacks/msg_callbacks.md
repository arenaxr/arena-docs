---
title: MsgCallbacks
layout: default
parent: Callbacks
grand_parent: Python Library
---

# All Messages Callback

`scene.on_msg_callback` is called whenever there is a new message sent to the client. Use this whenever you want to sniff out **all** incoming messages.

The following source code was mirrored from the `arena-py` [msg_callbacks.py](https://github.com/arenaxr/arena-py/blob/master/examples/callbacks/msg_callbacks.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

# [scene] is the Scene that called the callback
# [obj] will be an Object instance
# [msg] is the raw JSON message as a dict
def on_msg_callback(_scene, obj, _msg):
    # do stuff with obj here
    print("msg", obj, obj.data.position)
    # etc.
    # could also do obj["object_id"] or msg["object_id"]

scene.on_msg_callback = on_msg_callback
```
