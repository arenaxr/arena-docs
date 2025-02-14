---
title: GltfMorph
layout: default
parent: Attributes
grand_parent: Python Library
---

# GLTF Morph

Allows you to target and control a gltf model's morphTargets created in Blender.

More properties at <a href='https://github.com/elbobo/aframe-gltf-morph-component'>A-Frame GLTF Morph</a> component.

Additional Python properties are available in the [GltfMorph API Reference](/content/python-api/attributes/gltf_morph).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

close_eye_morphs = (
    Morph(
        morphtarget="eyeBottom",
        value=0.8,
    ),
    Morph(
        morphtarget="eyeTop",
        value=0.8,
    ),
)
open_eye_morphs = (
    Morph(
        morphtarget="eyeTop",
        value=0.0,
    ),
    Morph(
        morphtarget="eyeBottom",
        value=0.0,
    ),
)

t = 0
xr_logo = GLTF(
    object_id="xr-logo",
    position=(0, 0, -5),
    scale=(1.0, 1.0, 1.0),
    url="store/users/wiselab/models/XR-logo.glb",
    persist=True,
)

@scene.run_forever(interval_ms=1000)
def close_xr_eyes():
    global t

    if t % 2 == 0:
        # list of morphs
        xr_logo.update_morph(close_eye_morphs)
        scene.update_object(xr_logo)
        print("Morph Target Close Eye")
    else:
        xr_logo.update_morph(open_eye_morphs)
        scene.update_object(xr_logo)
        print("Morph Target Open Eye")

    t += 1

scene.run_tasks()
```
