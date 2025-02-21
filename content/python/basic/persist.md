---
title: Persist
layout: default
parent: Basic
grand_parent: Python Library
---

# Persisted Objects

If we want our objects to return to the scene when we next open or reload our browser, we can commit them on creation to the ARENA Persistence DB by setting `"persist": true`.

The following source code was mirrored from the `arena-py` [persist.py](https://github.com/arenaxr/arena-py/blob/master/examples/basic/persist.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_persisted_sphere():
    my_ball = Sphere(
        object_id="Ball2",
        position=(-1, 1, -1),
        persist=True,
    )
    scene.add_object(my_ball)

scene.run_tasks()
```
