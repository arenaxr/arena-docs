---
title: Scale
layout: default
parent: Attributes
grand_parent: Python Library
---

# Scale

3D object scale.

Additional Python properties are available in the [Scale API Reference](/content/python-api/attributes/scale).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

scale = (1, 2, 1)  # Scale(1,2,1) works too

@scene.run_once
def make_box():
    my_box = Box(
        object_id="my_box",
        position=(0, 2, -5),
        scale=scale,
    )
    scene.add_object(my_box)

scene.run_tasks()
```
