---
title: Python Library
nav_order: 4
layout: default
has_children: true
---

# Python Library Overview
Draw objects and run programs in the ARENA using Python!
- [**ARENA-py**](https://github.com/conix-center/ARENA-py) Python repository


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

scene = Scene(host="arena.andrew.cmu.edu", realm="realm", scene="example")

@scene.run_once
def make_box():
    scene.add_object(Box())

scene.run_tasks()
```

## ARENA-py Library
The above is the simplest example of an ARENA Python program. This library sits above the ARENA pub/sub MQTT
message protocol: JSON messages described in more detail [here](https://arena.conix.io/content/messaging/definitions.html) which runs in a browser.
That forms a layer, in turn, on top of [A-Frame](https://aframe.io/) and [THREE.js](http://threejs.org/) javascript libraries.


## Examples
Examples of ARENA-py programs can be found [here](https://github.com/conix-center/ARENA-py/tree/master/examples) and [here](https://github.com/conix-center/ARENA-py/tree/master/system-tests).


## Authentication
We are adding protection to the ARENA MQTT broker, eventually to host an ACL list to limit access to change your scenes. As a first step, we are requiring Python programs to supply authentication through a Google account.

### Sign-In Desktop OS
If you have a web browser available, the ARENA library `Scene(host="myhost.com")` will launch a web browser the first time and ask you for an account to authenticate you with, before opening a client MQTT connection.

### Sign-In Server/Headless OS
For headless environments, the ARENA library `Scene(host="myhost.com")` will provide you with a url to cut and paste in a browser anywhere, ask you for an account to authenticate you with, and show you a code you can enter on the command line, before opening a client MQTT connection.

### Sign-Out
```bash
python3 -c "from arena import auth; auth.signout()"
```

### Show Permissions
```bash
python3 -c "from arena import auth; auth.permissions()"
```


## Python Interactive Robot Demo
<figure class="video_container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/E7YkqZ5Hkas" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
