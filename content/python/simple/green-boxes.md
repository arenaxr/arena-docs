---
title: GreenBoxes
layout: default
parent: Simple
grand_parent: Python Library
---

# Green Boxes

```python
import random
import sys
import time

from arena import *

scene = Scene(host="arenaxr.org", scene="example")

color = (0, 255, 0)

# more complex case: Create many boxes

x = 1

@scene.run_forever(interval_ms=500)
def make_boxs():
    global x

    # Create a bunch of green boxes drawn directly to screen
    position = (random.randrange(10)-5,
                random.randrange(10),
                -random.randrange(10))
    box = Box(
            position=position,
            color=color
        )
    scene.add_object(box)
    x = x + 1

    print("object " + str(x-1) + " at " + str(position))

scene.run_tasks()
```
