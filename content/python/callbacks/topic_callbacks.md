---
title: TopicCallbacks
layout: default
parent: Callbacks
grand_parent: Python Library
---

# Add/Remove Topic

Demonstrate subscribing to a secondary topic on the same broker and monitor
messages from the secondary topic within the same program.

```python
import json

from arena import *

def objects_callback(_scene, _obj, msg):
    print("Object message: " + str(msg))

def secondary_callback(_scene, _obj, msg):
    print(f"Secondary message:\nTopic: {str(msg.topic)}\nPayload: {json.loads(msg.payload)}")

# subscribe to objects
scene = Scene(host="arenaxr.org", scene="example", on_msg_callback=objects_callback)

@scene.run_async
async def test():
    topic = f"realm/d/{scene.namespace}/#"
    # subscribe to secondary
    scene.message_callback_add(topic, secondary_callback)
    print(f"Subscribed to {topic}")

    # sleep for 5 seconds
    await scene.sleep(5000)

    # unsubscribe to secondary
    scene.message_callback_remove(topic)
    print(f"Unsubscribed to {topic}")

# our main event loop
scene.run_tasks()
```
