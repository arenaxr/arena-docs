---
title: ModelContainer
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Model Container

Overrides absolute size for a 3D model. The model can be a glTF, glb, obj, or any other supported format. The model will be rescaled to fit to the sizes specified for each axes.

This example scales the Duck model into a 10 x 10 x 10 box.

Additional Python properties are available in the [ModelContainer API Reference](/content/python-api/attributes/model_container).

The following source code was mirrored from the `arena-py` [model_container.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/model_container.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

model_container = ModelContainer(
    x=2,
    y=2,
    z=2,
)

@scene.run_once
def make_model_container():
    scene.add_object(
        GltfModel(
            object_id="gltf-model-duck",
            url="store/models/Duck.glb",
            position=(0, 1, -5),
            model_container=model_container,
            persist=True,
        )
    )

scene.run_tasks()
```
