---
title: Ttl
layout: default
parent: Basic
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Temporary Objects: TTL

It's desirable to have objects that don't last forever and pile up. For that there is the 'ttl' parameter that gives objects a lifetime, in seconds. This is an example usage for a sphere that disappears after 5 seconds.

The following source code was mirrored from the `arena-py` [ttl.py](https://github.com/arenaxr/arena-py/blob/master/examples/basic/ttl.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_timed_sphere():
    my_ball = Sphere(
        object_id="Ball2",
        position=(-1, 1, -1),
        ttl=5,
    )
    scene.add_object(my_ball)

scene.run_tasks()
```
