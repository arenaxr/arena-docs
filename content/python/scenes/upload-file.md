---
title: UploadFile
layout: default
parent: Scenes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Uploading Files

Upload some sample files to the ARENA filestore under the user's store folder and create objects to render them.

The following source code was mirrored from the `arena-py` [upload-file.py](https://github.com/arenaxr/arena-py/blob/master/examples/scenes/upload-file.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def upload_files():
    url_glb = scene.upload_store_file("/Users/username/Desktop/abox.glb")
    if url_glb:
        scene.add_object(GltfModel(persist=True, position=Position(0, 1, -3), url=url_glb))

    url_glb2 = scene.upload_store_file("/Users/username/Desktop/abox.glb", "second-level/abox.glb")
    if url_glb2:
        scene.add_object(GltfModel(persist=True, position=Position(2, 1, -3), url=url_glb2))

    url_mp4 = scene.upload_store_file("/Users/username/Desktop/qqd.mp4")
    if url_mp4:
        scene.add_object(Plane(persist=True, position=Position(0, 2, -4), material=Material(src=url_mp4)))

scene.run_tasks()
```
