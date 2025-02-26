---
title: ChatCallbacks
layout: default
parent: Callbacks
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Chat Callback

Extremely basic example of setting a chat message handler to echo
chat messages typed in the scene.

Note that currently all chat messages terminate with `\n` (newline) that should
probably be stripped.

The following source code was mirrored from the `arena-py` [chat_callbacks.py](https://github.com/arenaxr/arena-py/blob/master/examples/callbacks/chat_callbacks.py) example.

```python
import arena

def chat_handler(_scene, chatmsg, _rawmsg):
    print(f"Chat message from {chatmsg.dn} ({chatmsg.object_id}): {chatmsg.text.strip()}")

scene = arena.Scene(host="arenaxr.org", scene="example", on_chat_callback=chat_handler)

scene.run_tasks()
```
