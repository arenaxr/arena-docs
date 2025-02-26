---
title: Triangle
layout: default
parent: Objects
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Triangle

Draw a Triangle primitive mesh geometry. Triangle is flat shape with 3 edges.

Additional Python properties are available in the [Triangle API Reference](/content/python-api/objects/triangle).

The following source code was mirrored from the `arena-py` [triangle.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/triangle.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_triangle():
    my_triangle = Triangle(
        object_id="my_triangle",
        position=(0, 5, -3),
        scale=(1, 1, 1),
        material=Material(color=(10, 70, 200)),
    )
    scene.add_object(my_triangle)

scene.run_tasks()
```
