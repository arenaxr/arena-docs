---
title: Scale
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Scale

3D object scale.

Additional Python properties are available in the [Scale API Reference](/content/python-api/attributes/scale).

The following source code was mirrored from the `arena-py` [scale.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/scale.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

scale = (1, 2, 1)  # Scale(1,2,1) works too

@scene.run_once
def make_scaled_box():
    my_box = Box(
        object_id="my_box",
        position=(0, 2, -5),
        scale=scale,
    )
    scene.add_object(my_box)

scene.run_tasks()
```
