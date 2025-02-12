---
title: Torus
layout: default
parent: Objects
grand_parent: Python Library
---

# Torus

Draw a Torus primitive mesh geometry. Torus is a tube shaped into a circle.

`arena-py` API Reference for [Torus](/content/python-api/objects/torus).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_torus():
    my_torus = Torus(
        object_id="my_torus",
        position=(0, 5, -3),
        scale=(1.5, 1.5, 1.5),
        material=Material(color=(100, 70, 40)),
    )
    scene.add_object(my_torus)

scene.run_tasks()
```
