---
title: Python Library
nav_order: 6
layout: default
has_children: true
---

# Python Library Overview

The Python library provides a very accessible development option for ARENA applications. Our current API allows us to create and update objects in a scene, define animations, and setup callbacks on events and timers. The library provides a scheduler and a design pattern familiar to game developers, which includes decorators to create one-shot, periodic and delayed (start after a given time) tasks.Any entity represented in Python is automatically updated upon arrival of network messages and we provide calls to load any pre-existing scene content upon startup.

Draw objects and run programs in the ARENA using Python!
- [**arena-py**](https://github.com/arenaxr/arena-py) Python repository


## Setup
Install package using pip:
```shell
pip3 install arena-py
```


## Hello ARENA
Run the `hello.py` example:
```shell
cd examples
python hello.py
```

`hello.py`
```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_box():
    scene.add_object(Box())

scene.run_tasks()
```

## arena-py Library
The above is the simplest example of an ARENA Python program. This library sits above the ARENA pub/sub MQTT
message protocol. JSON messages are described in more detail in our [Wire Message Definition](/content/schemas/definitions) which runs in a browser.
That forms a layer, in turn, on top of [A-Frame](https://aframe.io/) and [THREE.js](http://threejs.org/) javascript libraries.

## Examples
Examples of arena-py programs can be found in our [Examples](https://github.com/arenaxr/arena-py/tree/master/examples) and [System Tests](https://github.com/arenaxr/arena-py/tree/master/system-tests).

## Running from the Command Line
ARENA python applications can be sandboxed in the WASM runtime (currently with limited library support due to the still immature support for Python in WASM toolchains) and managed by ARTS, or ran standalone from you computer.

To run a python program from the command line in your computer, specify the target of which server, user and scene are set by the `Scene(host="...",scene="...",namespace="...",debug=False)` function call.  It is also possible to override these using environmental variables at the command line as shown below.  This allows a simple way to re-target applications for your own environment without having to change the parameters manually in the code.
```shell
export MQTTH=arenaxr.org # ARENA webserver main host
export REALM=realm
export SCENE=scene
export NAMESPACE=namespace
python3 hello.py
...
=====
Loading: https://arenaxr.org/namespace/scene, realm=realm
Connecting to the ARENA...
Connected!
=====
...
```
If not specified the namespace is your current logged in user-id. The most common use-case is to simply update `SCENE` and `MQTTH`.


## Authentication
We have added protection to the ARENA MQTT broker to limit access to change your scenes, which requires Python programs to supply authentication through a Google account.

### Sign-In Desktop OS
If you have a web browser available, the arena-py library `Scene(host="myhost.com")` will launch a web browser the first time and ask you for an account to authenticate you with, before opening a client MQTT connection.

### Sign-In Server/Headless OS
For headless environments, the arena-py library `Scene(host="myhost.com")` will provide you with a url to cut and paste in a browser anywhere, ask you for an account to authenticate you with, and show you a code you can enter on the command line, before opening a client MQTT connection.

## Scripts
Some helper script aliases have been added in this library to help you manage authentication and quick command-line (CLI) publish and subscribe to the ARENA.

### Sign-Out
```bash
arena-py-signout
```
### Show Permissions
```bash
arena-py-permissions
```
### CLI Subscribe to Scene Messages
```bash
arena-py-sub -mh arenaxr.org -s example
```
### CLI Subscribe to Custom Topic
```bash
arena-py-sub -mh arenaxr.org -t realm/g/a
```
### CLI Publish a Scene Object Message
```bash
arena-py-pub -mh arenaxr.org -s example -m '{"object_id": "gltf-model_Earth", "action": "create", "type": "object", "data": {"object_type": "gltf-model", "position": {"x":0, "y": 0.1, "z": 0}, "url": "store/models/Earth.glb", "scale": {"x": 5, "y": 5, "z": 5}}}'
```
### CLI Help
```bash
arena-py-pub --help
arena-py-sub --help
```

## Python Interactive Robot Demo
<figure class="video_container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/E7YkqZ5Hkas" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
