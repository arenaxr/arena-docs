---
title: Events
nav_order: 4
layout: default
parent: Python Library
---

# Events in arena-py

Events are ways to interact with user input in the ARENA.

See [object definition reference](/content/schemas/definitions).

## Event handlers
To handle events in arena-py, you must set a function to the `evt_handler` parameter.
When you attach an `evt_handler` to an `Object`, you will receive `Event` objects in your handler.
Below is how you access attributes of the `Event` object.

```python
# [scene] is the Scene that called the callback
# [evt] will be an Event instance
# [msg] is the raw JSON message as a dict
def click_handler(scene, evt, msg):
    ## Get Event type
    evt.type # == "buttonClick", "mousedown", "mouseup", "mouseenter", "mouseleave", etc.

    ## Get Event data
    evt.data.clickPos
    evt.data.position
    evt.data.source
    evt.data.buttonName
    evt.data.buttonIndex
    # etc.

box = Box(..., evt_handler=click_handler) # note the use of "evt_handler=click_handler"
# could also do box.evt_handler = click_handler
# or box.update_attributes(evt_handler=click_handler)
```

## Generating events with arena-py Scenes
### Click Events
There are several types of click events that you can generate (`mousedown`, `mouseup`, `mouseenter`, `mouseleave`, `triggerdown`, `triggerup`):
```python
scene.generate_click_event(obj, type, ...)

# add a click listener to an object to be able to click it
obj.update_attributes(clickable=True)
# generate a "fake" click event from arena-py
scene.generate_click_event(
    obj,
    type="mouseup"
)
# arena-py will "click" obj with mouseup. In JSON, "source" will be defined as "arena_lib_[some random ID here]".
```

### Camera Manipulation Events
You can also move a user's camera and/or make it look at a specific location or object:
```python
scene.manipulate_camera(obj, type, ...)

# move camera:
scene.manipulate_camera(
    camera,
    position=(rando(),1.6,rando()),
    rotation=(0,0,0,1)
)

# make camera look at something/some position:
scene.look_at(
    camera,
    target=box # can also do a position: (0,0,0)
)
```

### Generic Events
If there is an event that does not exist yet, you can use this to have more freedom in the event type:
```python
# define custom event
evt = Event(type="my_custom_event", position=(3,4,5), target=sphere)
# generate custom event with arena-py client
scene.generate_custom_event(evt, action="clientEvent")
```

# Appendix
```python
Event(object_id, action, type, ...)
```
