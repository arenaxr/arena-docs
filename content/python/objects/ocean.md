---
title: Ocean
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Ocean

Draw an Ocean primitive. Ocean is flat shape with 4 edges, in which the inner triangles are animated to mimic ocean waves.

Additional Python properties are available in the [Ocean API Reference](/content/python-api/objects/ocean).

The following source code was mirrored from the `arena-py` [ocean.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/ocean.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_ocean():
    my_ocean = Ocean(
        object_id="my_ocean",
        position=(0, 0.5, -3),
        rotation=(-90, 0, 0),
        width=10,
        depth=10,
    )
    scene.add_object(my_ocean)

scene.run_tasks()
```
