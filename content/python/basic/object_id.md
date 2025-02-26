---
title: ObjectId
layout: default
parent: Basic
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Object Naming


The following source code was mirrored from the `arena-py` [object_id.py](https://github.com/arenaxr/arena-py/blob/master/examples/basic/object_id.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_named_boxes():
    # create a box with a uuid generated name
    box_named_id = Box(
        object_id="box1",
    )
    scene.add_object(box_named_id)

    # create a box with the name "box1"
    box_named_uuid = Box()
    scene.add_object(box_named_uuid)

scene.run_tasks()
```
