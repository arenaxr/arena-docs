---
title: Hello
layout: default
parent: Simple
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Hello World

The following source code was mirrored from the `arena-py` [hello.py](https://github.com/arenaxr/arena-py/blob/master/examples/simple/hello.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    scene.add_object(Box())

scene.run_tasks()
```
