---
title: Multisrc
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Images on Objects

Multi Source

Define multiple visual sources applied to an object.

Use the `multisrc` A-Frame Component to specify different bitmaps for sides of a box or other primitive shape.

Additional Python properties are available in the [Multisrc API Reference](/content/python-api/attributes/multisrc).

The following source code was mirrored from the `arena-py` [multisrc.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/multisrc.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

multisrc = Multisrc(
    srcspath="store/users/wiselab/images/dice/",
    srcs="side1.png,side2.png,side3.png,side4.png,side5.png,side6.png",
)

@scene.run_once
def make_die1():
    die1 = Box(
        object_id="die1",
        position=Position(0, 3, -2),
        material=Material(color="#ffffff"),
        multisrc=multisrc,
    )
    scene.add_object(die1)

scene.run_tasks()
```
