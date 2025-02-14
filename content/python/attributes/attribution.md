---
title: Attribution
layout: default
parent: Attributes
grand_parent: Python Library
---

# Attribution

Attribution Component. Saves attribution data in any entity.

Additional Python properties are available in the [Attribution API Reference](/content/python-api/attributes/attribution).

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

attribution = Attribution(
    author="The Smithsonian Institution",
    authorURL="https://3d.si.edu",
    license="CC0",
    licenseURL="https://creativecommons.org/publicdomain/zero/1.0/",
    source="The Smithsonian Institution",
    sourceURL="https://3d.si.edu/object/3d/mammuthus-primigenius-blumbach:341c96cd-f967-4540-8ed1-d3fc56d31f12",
    title="Mammuthus primigenius",
)

@scene.run_once
def make_gltf_model_blumbach():
    gltf_model_blumbach = GLTF(
        object_id="gltf-model-blumbach",
        url="store/users/wiselab/build/blumbach.glb",
        position=(0, 1.7, -5),
        rotation=(0, 0.38268, 0, 0.92388),
        attribution=attribution,
    )
    scene.add_object(gltf_model_blumbach)

scene.run_tasks()
```
