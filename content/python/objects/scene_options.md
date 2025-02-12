---
title: SceneOptions
layout: default
parent: Objects
grand_parent: Python Library
---

# Background Themes

ARENA Scene Options.

Adds one of many predefined backgrounds ( one of: **none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris**) to the scene.

`arena-py` API Reference for [SceneOptions](/content/python-api/objects/scene_options).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")


@scene.run_once
def update_environment():
    opt_obj = Object(
        object_id="scene-options",
        type="scene-options",
        persist=True,
    )
    opt_obj.data["env-presets"] = {"preset": "arches"}
    del opt_obj.data.object_type
    scene.add_object(opt_obj)


scene.run_tasks()
```
