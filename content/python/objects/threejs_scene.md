---
title: ThreejsScene
layout: default
parent: Objects
grand_parent: Python Library
---

# Three.js Scene

Load a Three.js Scene.

Could be THREE.js version-specific; you can see the THREE.js version in the JS console once you open ARENA; using glTF is preferred. Format: <a href='https://threejs.org/docs/#api/en/scenes/Scene'>THREE.js Scene</a>. See guidance to store paths under <a href='https://docs.arenaxr.org/content/interface/filestore.html'>ARENA File Store, CDN, or DropBox</a>.

Additional Python properties are available in the [ThreejsScene API Reference](/content/python-api/objects/threejs_scene).

The following source code was mirrored from the `arena-py` [threejs_scene.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/threejs_scene.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_threejs_scene():
    test_scene = ThreejsScene(
        object_id="test-scene",
        position=(0, 1, -3),
        url="/store/users/wiselab/threejs-scenes/simple_scene.json",
    )
    scene.add_object(test_scene)

scene.run_tasks()
```
