---
title: Rotation
layout: default
parent: Attributes
grand_parent: Python Library
---

# Rotate

Rotate the already drawn box; these are in quaternions, not A-Frame degrees.

3D object rotation in quaternion representation; Right-handed coordinate system. Euler degrees are deprecated in wire message format.

The quaternion (native) representation of rotation is a bit more tricky. The 4 parameters are X, Y, Z, W. Here are some simple examples:

- `1, 0, 0, 0`: rotate 180 degrees around X axis
- `0, 0.7, 0, 0.7`: rotate 90 degrees around Y axis
- `0, 0, -0.7, 0.7`: rotate -90 degrees around Z axis

Additional Python properties are available in the [Rotation API Reference](/content/python-api/attributes/rotation).

The following source code was mirrored from the `arena-py` [rotation.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/rotation.py) example.

```python
import math

from arena import *

scene = Scene(host="arenaxr.org", scene="example")

rotation_euler = (0, 0, 0)  # Rotation(0,0,0) works
rotation_quaternion = (0, 0, 1, 1)  # Rotation(0,0,1,1) works too

my_box1 = Box(
    object_id="my_box1",
    position=(-2, 2, -5),
    rotation=rotation_euler,
)

my_box2 = Box(
    object_id="my_box2",
    position=(2, 2, -5),
    rotation=rotation_quaternion,
)

@scene.run_once
def make_rotatable_box():
    scene.add_object(my_box1)
    scene.add_object(my_box2)

@scene.run_forever(interval_ms=100)
def rotate_box():
    my_box1.data.rotation.x += 3
    my_box1.data.rotation.y += 3
    my_box1.data.rotation.z += 3

    # guard against over rotating
    if abs(my_box1.data.rotation.x) > 180:
        my_box1.data.rotation.x = 0
    if abs(my_box1.data.rotation.y) > 180:
        my_box1.data.rotation.y = 0
    if abs(my_box1.data.rotation.z) > 180:
        my_box1.data.rotation.z = 0

    scene.update_object(my_box1)

scene.run_tasks()
```
