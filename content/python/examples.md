---
title: Examples
nav_order: 2
layout: default
parent: Python Library
---

# Python Examples

- [**ARENA-py**](https://github.com/conix-center/ARENA-py) Python repository

{% include alert type="warning" title="Warning" content="Writing in progress...." %}

## Viewer

For all these standalone examples, open your browser first at this address: [https://arena.andrew.cmu.edu/?scene=example](https://arena.andrew.cmu.edu/?scene=example)

Use this template for all of these examples, import arena, init, handle events.

## Python Structure

```python
import arena
# [Callback functions may go before/after arena.init()]
arena.init("arena.andrew.cmu.edu", "realm", "example")
# [All other arena.py functions must be call after arena.init()]
arena.handle_events()
```

## Debug Messages

```python
arena.debug()
```

## Add Subtopic

```python
def secondary_callback(msg):
    print(msg.payload)

arena.add_topic("$SYS/#", secondary_callback)
```

## Remove Subtopic

```python
arena.remove_topic("$SYS/#")
```

## Create a cube

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
cube = arena.Object(objType=arena.Shape.cube)
arena.handle_events()
```

## Object Names

```python

```

## Objects with no names

```python

```

## Observe name collisions

```python

```

## Colors, 3 kinds!

```python
cube.update(color=(0, 255, 0))
cube.update(data='{"color":"#00ff00"}')
cube.update(data='{"color":"green"}')
```

## Transparency

```python
cube.update(transparency=arena.Transparency(True, 0.5))
```

## Move

```python
cube.update(location=(2, 2, -1))
```

## Rotate

```python
cube.update(rotation=(0.4, 0.4, 0.4, 0.4))
```

## Animate

```python
cube.update(data='{"animation": {"property":"rotation", "to":"0 360 0", "loop":"true", "dur":10000}}')
```

## Delete

```python
cube.delete()
```

## Images

```python
floor = arena.Object(
    objName="my_image_floor",
    objType=arena.Shape.image,
    location=(0, 0, 0.4),
    rotation=(-0.7, 0, 0, 0.7),
    scale=(12, 12, 12),
    data='{"url": "images/floor.png", "material": {"repeat": {"x":4, "y":4}}}',
)
```

## Images on Objects

```python
floor.update(
    data='{"material": {"src": "https://arena.andrew.cmu.edu/abstract/downtown.png"}}'
)
```

## Models

```python
duck = arena.Object(
    objName="model1",
    objType=arena.Shape.gltf_model,
    location=(0, 0, -4),
    url="models/Duck.glb",
)

cow = arena.Object(
    objName="model2",
    objType=arena.Shape.gltf_model,
    location=(-21, 1.8, -8),
    scale=(0.02, 0.02, 0.02),
    url="models/cow2/scene.gltf",
)
cow.update(data='{"animation-mixer": {"clip": "*"}}')
```

## Animation

```python

```

## Relocalize Camera

```python
# (dangerous) technique to update everyone's camera rig without knowing name
rig = arena.Object(objName="cameraRig")
rig.update(location=(1, 1, 1))
```

## Text

```python
text = arena.Object(
    objName="text_3",
    objType=arena.Shape.text,
    color=(255, 0, 0),
    location=(0, 3, -4),
    text="Hello world!",
)
text.update(color=(0, 255, 0))
```

## Lights

```python
light = arena.Object(
    objName="myLight",
    objType=arena.Shape.light,
    location=(1, 1, 1),
    rotation=(0.25, 0.25, 0.25, 1),
    color=(255, 0, 0),
)
```

## Sound

```python

```

## 360 Video

```python

```

## Lines

```python
arena.Object(
    objName="line1",
    objType=arena.Shape.line,
    line=arena.Line(start=(3, 2, -4), end=(3, 3, -4), color=(206, 0, 255)),
)
```

## Thicklines

```python
arena.Object(
    objName="line2",
    objType=arena.Shape.thickline,
    thickline=arena.Thickline(line_width=11, color=(255, 136, 238), path=[
        (3, 4, -4), (4, 4, -4), (4, 5, -4), (4, 5, -5)]),
)
```

## All Scene Messages Callback

```python
import arena

def scene_callback(msg):
    print("scene_callback: ", msg)

arena.init("arena.andrew.cmu.edu", "realm", "example", scene_callback)
cube = arena.Object(objType=arena.Shape.cube, clickable=True)
arena.handle_events()
```

## Single-Object Events Callback

```python
import arena

def cube_callback(msg):
    print("cube_callback: ", msg)

arena.init("arena.andrew.cmu.edu", "realm", "example")
cube = arena.Object(objType=arena.Shape.cube, clickable=True, cube_callback)
arena.handle_events()
```

## persist

```python

```

## ttl

```python

```

## Occlusion

```python

```

## themes

```python

```

## Physics

```python
torus = arena.Object(
    objName="", objType=arena.Shape.torusKnot, color=(255, 0, 0), location=(0, 3, -6)
)
torus.update(color=(0, 0, 255))
torus.update(physics=arena.Physics.dynamic)
torus.update(ttl=2)
```

## Parent/Child

```python

```

## goto-url

```python

```

## Particles

```python

```

## Events

```python

```
