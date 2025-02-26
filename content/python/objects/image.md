---
title: Image
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Images

Display an image on a plane geometry.

See guidance to store paths under <a href='https://docs.arenaxr.org/content/interface/filestore.html'>ARENA File Store, CDN, or DropBox</a>.

Create an image on the floor.

URLs work in the URL parameter slot. Instead of `images/2.png` it would be e.g. `url(http://arenaxr.org/images/foo.jpg)`.
To update the image of a named image already in the scene, use this syntax.

Additional Python properties are available in the [Image API Reference](/content/python-api/objects/image).

The following source code was mirrored from the `arena-py` [image.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/image.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_image():
    image_floor = Image(
        object_id="image_floor",
        position=(0, 0, 0.4),
        rotation=(-0.7, 0, 0, 0.7),
        scale=(12, 12, 2),
        material=Material(repeat={"x": 4, "y": 4}),
        url="store/users/wiselab/images/floor.png",
    )
    scene.add_object(image_floor)
    scene.update_object(
        image_floor,
        material=Material(src="store/users/wiselab/images/abstract/downtown.png"),
    )

scene.run_tasks()
```
