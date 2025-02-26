---
title: ObjectId
layout: default
parent: Basic
grand_parent: Python Library
---

# Object Naming


The following source code was mirrored from the `arena-py` [object_id.py](https://github.com/arenaxr/arena-py/blob/master/examples/basic/object_id.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_timed_sphere():
    # create a box with a uuid generated name
    box_named_id = Box()
    scene.add_object(box_named_id)

    # create a box with the name "box1"
    box_named_uuid = Box(
        object_id="box1",
    )
    scene.add_object(box_named_uuid)

scene.run_tasks()
```
