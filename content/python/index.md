---
title: Python Library
nav_order: 4
layout: default
has_children: true
---

# Python Library Overview

Draw objects in the ARENA using our Python library.

This library sits above the ARENA pub/sub MQTT message protocol. JSON messages are used by a our [ARENA web client](https://github.com/conix-center/ARENA-core) running in a browser, and is and described in more detail in our [Messaging Format](../messaging/index.md). That forms a layer, in turn, on top of the [A-Frame](https://aframe.io/) and [THREE.js](http://threejs.org/) javascript libraries.

## Hello ARENA

This is the simplest example of an ARENA Python program.

`hello.py`

```
import arena
arena.init("oz.andrew.cmu.edu", "realm", "hello")
arena.Object(arena.Shape.cube)
arena.handle_events()
```

## Say Hello in the ARENA

1. Open the ARENA in your browser first: [https://xr.andrew.cmu.edu?scene=hello](https://xr.andrew.cmu.edu?scene=hello)
1. Install our package using pip:
    ```
    pip3 install arena-py
    cd examples
    python hello.py
    ```
1. Watch your 3d cube arrive in the ARENA.
1. Use your mouse and arrow keys to move around.
1. Create more awesomeness! And show us what you made!
