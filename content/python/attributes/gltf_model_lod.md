---
title: GltfModelLod
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# GLTF Model Level of Detail

Simple switch between the default gltf-model and a detailed one when a user camera is within specified distance.


Additional Python properties are available in the [GltfModelLod API Reference](/content/python-api/attributes/gltf_model_lod).

The following source code was mirrored from the `arena-py` [gltf_model_lod.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/gltf_model_lod.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

gltf_model_lod = GltfModelLod(
    detailedUrl="store/models/BrainStem.glb",
    detailedDistance=6,
    updateRate=333,
    retainCache=False,
)

@scene.run_once
def make_lod_gltf():
    lod_gltf = GLTF(
        object_id="lod_gltf",
        url="store/models/Head2.glb",
        position=(0, 2, -3),
        gltf_model_lod=gltf_model_lod,
    )
    scene.add_object(lod_gltf)

scene.run_tasks()
```
