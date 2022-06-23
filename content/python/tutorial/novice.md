---
title: Novice Example
nav_order: 2
layout: default
parent: Python Tutorial
---

# Novice Example - Exploring EVEN more functionality!

## Event Handlers
See [events](https://arena.conix.io/content/python/events.html)
```python
def mouse_handler(scene, evt, msg):
    print(evt.type)
    # do amazing stuff here

# pro tip: you can actually update an object directly in the arena update_object function
scene.update_object(box, clickable=True, evt_handler=mouse_handler)
# scene.update_object(box, click_listener=True, evt_handler=mouse_handler) # also works
```

## Deleting Attributes
```python
box.update_attributes(click_listener=None)
# box.update_attributes(click_listener=False) # also works
```

## Deleting Objects
```python
scene.delete_object(box)
```

# Appendix
```python
from arena import *

# setup library
scene = Scene(host="mqtt.arenaxr.org", scene="example")

@scene.run_async
async def func():
    # make a box
    box = Box(object_id="my_box", position=Position(0,4,-2), scale=Scale(2,2,2))
    scene.add_object(box)

    def mouse_handler(scene, evt, msg):
        if evt.type == "mousedown":
            box.data.position.x += 0.5
            scene.update_object(box)

    # add click_listener
    scene.update_object(box, click_listener=True, evt_handler=mouse_handler)

    # sleep for 10 seconds
    await scene.sleep(10000)

    # delete box
    scene.delete_object(box)

# start tasks
scene.run_tasks()
```
