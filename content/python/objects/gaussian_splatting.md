---
title: GaussianSplatting
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# 3D Gaussian Splat

Load a 3D Gaussian Splat for Real-Time Radiance Field Rendering.

More information: <a href='https://github.com/quadjr/aframe-gaussian-splatting'>A-Frame Gaussian Splatting</a>. See guidance to store paths under <a href='https://docs.arenaxr.org/content/interface/filestore.html'>ARENA File Store, CDN, or DropBox</a>.

Additional Python properties are available in the [GaussianSplatting API Reference](/content/python-api/objects/gaussian_splatting).

The following source code was mirrored from the `arena-py` [gaussian_splatting.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/gaussian_splatting.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_seal_splat():
    seal_splat = GaussianSplatting(
        object_id="seal_splat",
        position=(0, 0.5, -3),
        src="/store/splats/luma-seal.splat",
    )
    scene.add_object(seal_splat)

scene.run_tasks()
```
