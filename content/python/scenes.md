---
title: Scenes
nav_order: 1
layout: default
parent: Python Library
---

# Scenes in ARENA-py

Scenes give ARENA-py programs access to an ARENA scene. It provides an interface to add/update objects, run animations, and many more!

## Scene Access
To get access to a scene in the ARENA, create a `Scene` object. Make sure you have proper permissions to access it!
```python
scene = Scene(host="arena.andrew.cmu.edu", realm="realm", scene="example")
# scene = Arena(host="arena.andrew.cmu.edu", realm="realm", scene="example") works too
```

## Arguments
`host`: Base ARENA URL.

`realm`: ARENA realm name.

`scene`: ARENA scene name.

`namespace`: ARENA namespace. Default value is ARENA username.

`debug`: If True, print authentication debug information and every published message. Ignore this parameter.

`network_latency_interval`: Interval (in ms) to run network graph latency update. Default value is 10000 (10 secs). Ignore this parameter.

## Callbacks
See [Scene Callbacks](callbacks.md).

## Access to Persisted Objects
To get access to Objects in the persist database, you can use `get_persisted_obj`.
```python
@scene.run_once
def main():
    obj = scene.get_persisted_obj(object_id)
    print(obj) # obj should be an object in persist with persist=True
```

You can also just do:
```python
@scene.run_once
def main():
    obj = scene.all_objects(object_id)
    print(obj) # obj should be an object in persist with persist=True
```
