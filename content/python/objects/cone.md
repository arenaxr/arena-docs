---
title: Cone
layout: default
parent: Objects
grand_parent: Python Library
---

# Cone

Draw a Cone primitive mesh geometry. Cone is a tube shape with one flat end and one joined (point) end.

Additional Python properties are available in the [Cone API Reference](/content/python-api/objects/cone).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_cone():
    my_cone = Cone(
        object_id="my_cone",
        position=(0, 2, -3),
        scale=(1, 2, 1),
        material=Material(color=(60, 200, 104)),
    )
    scene.add_object(my_cone)

scene.run_tasks()
```
