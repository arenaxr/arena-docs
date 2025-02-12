---
title: Hello
layout: default
parent: Simple
grand_parent: Python Library
---

# Hello World

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    scene.add_object(Box())

scene.run_tasks()
```
