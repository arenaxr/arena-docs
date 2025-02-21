---
title: Delete
layout: default
parent: Basic
grand_parent: Python Library
---

# Remove

Remove the box.

The following source code was mirrored from the `arena-py` [delete.py](https://github.com/arenaxr/arena-py/blob/master/examples/basic/delete.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def remove_box():
    # make a box
    box = Box(object_id="my_box")
    # delete box
    scene.delete_object(box)

scene.run_tasks()
```
