---
title: Scenes
nav_order: 1
layout: default
parent: Python Library
---

# Scenes in ARENA-py

Scenes give ARENA-py access to an ARENA scene. Provides an interface to add/update objects, run animations, and many more!

## Scene Access
To get access to a scene on the ARENA, create a `Scene` object. Make sure you have proper permissions to access it!
```python
scene = Scene(host="arena.andrew.cmu.edu", realm="realm", scene="example")
```
Note: `Scene` can also be called `Arena`, if you perfer that.

## Callbacks
See [Scene Callbacks](callbacks.md).

## Access to Persisted Objects
To get access to objects in the persist database, you can use `get_persisted_obj`.
```python
@scene.run_once
def main():
    obj = scene.get_persisted_obj(object_id)
    print(obj) # obj will be an object in persist with persist=True
```
