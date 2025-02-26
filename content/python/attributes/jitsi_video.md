---
title: JitsiVideo
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Video Stream

Example to stream video from Jitsi onto a geometry. Change the user display name to `my-name`, reload the scene page, and click the camera on button.

Additional Python properties are available in the [JitsiVideo API Reference](/content/python-api/attributes/jitsi_video).

The following source code was mirrored from the `arena-py` [jitsi_video.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/jitsi_video.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

jitsi_video = JitsiVideo(
    displayName="my-name",
)

@scene.run_once
def make_video_stream():
    video_stream = Box(
        object_id="video_stream",
        position=Position(0, 1, -3),
        persist=True,
        jitsi_video=jitsi_video,
    )
    scene.add_object(video_stream)

scene.run_tasks()
```
