---
title: Material
layout: default
parent: Attributes
grand_parent: Python Library
---

# Transparency

Say the box has already been drawn. In a second command, this sets 50% transparency.

To draw a shape that is transparent, but occludes other virtual objects behind it (to simulate virtual objects hidden by real world surfaces like a wall or table), include in the data section this JSON.

{ "material": { "colorWrite": false }, "render-order": "0" }

...or a shortcut for the same occlusion, you can use...

{ "material-extras": { "transparentOccluder": true } }

`colorWrite` is an attribute of the THREE.js Shader Material that, by exposing it, we make accessible like others belonging to the Material A-Frame Component, and is an alternative way of controlling visibility. `render-order` is a custom Component that controls which objects are drawn first (not necessarily the same as which are "in front of" others). All other ARENA objects are drawn with render-order of 1.

**This does not occlude the far background A-Frame layer (like environment component stars) but, in AR, that layer is not drawn anyway.**

The material properties of the object's surface.

More properties at <a href='https://aframe.io/docs/1.5.0/components/material.html'>A-Frame Material</a>.


Additional Python properties are available in the [Material API Reference](/content/python-api/attributes/material).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

material = Material(
    opacity=0.3,
    transparent=True,
)

@scene.run_once
def make_transparent_plane():
    my_plane = Plane(
        object_id="my_plane",
        position=(0, 2, -5),
        scale=(4.0, 4.0, 4.0),
        material=material,
    )
    scene.add_object(my_plane)

scene.run_tasks()
```
