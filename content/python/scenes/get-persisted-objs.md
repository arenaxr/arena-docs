---
title: GetPersistedObjs
layout: default
parent: Scenes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Get Persisted Objects

Tests scene `get_persisted_objs`.

The following source code was mirrored from the `arena-py` [get-persisted-objs.py](https://github.com/arenaxr/arena-py/blob/master/examples/scenes/get-persisted-objs.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="test")

@scene.run_once
def main():
    object_id = "the_box"
    for obj_id,obj in scene.get_persisted_objs().items():
        print(obj)
        print()

scene.run_tasks()
```
