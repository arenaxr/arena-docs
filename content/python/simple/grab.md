---
title: Grab
layout: default
parent: Simple
grand_parent: Python Library
---

# Grab Simple

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

grabbing = False

orig_position = (0,1.5,-2)

def box_click(scene, evt, msg):
    global orig_position
    global grabbing

    if evt.type == "mousedown":
        clicker = scene.users[evt.object_id]
        hand = clicker.hands.get('handRight', None)

        if hand is not None and not grabbing:
            print("grabbed")
            grabbing = True
            grab_dist = hand.data.position.distance_to(my_box.data.position)
            my_box.update_attributes(parent='rightHand', position=(0,0,-grab_dist))
            scene.update_object(my_box)

    elif evt.type == "mouseup":
        if grabbing:
            print("released")
            grabbing = False
            my_box.update_attributes(parent=None, position=orig_position)
            scene.update_object(my_box)

my_box = Box(
    object_id="my_box",
    position=orig_position,
    scale=(0.5,0.5,0.5),
    color=(50,60,200),
    patent=None,
    clickable=True,
    evt_handler=box_click
)

@scene.run_once
def main():
    scene.add_object(my_box)

scene.run_tasks()
```
