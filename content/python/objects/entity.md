---
title: Entity
layout: default
parent: Objects
grand_parent: Python Library
---

# Entity (generic object)

Entities are the base of all objects in the scene. Entities are containers into which components can be attached.

Additional Python properties are available in the [Entity API Reference](/content/python-api/objects/entity).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    my_ent = Entity(
        object_id="invisible_object",
        position=(0, 2, -3),
    )
    scene.add_object(my_ent)

scene.run_tasks()
```
