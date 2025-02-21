---
title: ObjModel
layout: default
parent: Objects
grand_parent: Python Library
---

# OBJ Model

Loads a 3D model and material using a Wavefront (.OBJ) file and a .MTL file.

See guidance to store paths under <a href='https://docs.arenaxr.org/content/interface/filestore.html'>ARENA File Store, CDN, or DropBox</a>.

Additional Python properties are available in the [ObjModel API Reference](/content/python-api/objects/obj_model).

The following source code was mirrored from the `arena-py` [obj_model.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/obj_model.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_obj_model():
    vr_controller_vive = ObjModel(
        object_id="vr_controller_vive",
        position=(0, 2, -3),
        scale=(7, 7, 7),
        obj="store/models/vr_controller_vive.obj",
        mtl="store/models/vr_controller_vive.mtl",
    )
    scene.add_object(vr_controller_vive)

scene.run_tasks()
```
