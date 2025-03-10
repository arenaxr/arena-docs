---
title: PcdModel
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# PCD Model

Load a PCD model.

Format: <a href='https://pointclouds.org/documentation/tutorials/index.html'>Point Clouds</a>. See guidance to store paths under <a href='https://docs.arenaxr.org/content/interface/filestore.html'>ARENA File Store, CDN, or DropBox</a>.

Additional Python properties are available in the [PcdModel API Reference](/content/python-api/objects/pcd_model).

The following source code was mirrored from the `arena-py` [pcd_model.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/pcd_model.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_bunny_pcd():
    bunny_pcd = PcdModel(
        object_id="bunny_pcd",
        position=(0, 1, -3),
        scale=(5, 5, 5),
        pointSize=0.01,
        pointColor="#7f7f7f",
        url="/store/users/wiselab/pcd-models/bunny.pcd",
    )
    scene.add_object(bunny_pcd)

scene.run_tasks()
```
