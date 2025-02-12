---
title: Scenes
nav_order: 1
layout: default
parent: Python Library
---

# Scenes in arena-py

Scenes give arena-py programs access to an ARENA scene. It provides an interface to add/update objects, run animations, and many more!
There are 3 main ways to define which server, scene name, and other arguments you wish to use:

1. [Python Object Args](#python-object-args)
1. [Environment Variable Args](#environment-variable-args)
1. [Command Line Args](#command-line-args)

## Python Object Args

To get access to a scene in the ARENA, create a `Scene` object. Make sure you have proper permissions to access it!

```python
scene = Scene(host="arenaxr.org", scene="example")
# scene = Arena(host="arenaxr.org", scene="example") works too
```

### Scene Object Arguments

See [Scene API Spec](/content/python-api/scene).

- `host`: Hostname of the ARENA webserver (required).
- `realm`: Reserved topic fork for future use (optional).
- `namespace`: Username of authenticated user or other namespace (automatic).
- `scene`: The name of the scene, without namespace (required).
- `network_latency_interval`: Interval (in ms) to run network graph latency update. Default value is 10000 (10 secs). Ignore this parameter.
- `video`: If true, request permissions for video conference. Default = False.
- `debug`: If true, print a log of all publish messages from this client. Default = False.
- `cli_args`: If true, require CLI [standardized parameters](#command-line-args). Default = False.
- `headless`: If true, force limited input device auth flow. Default = False.

### Scene Object Callbacks

See [Scene Callbacks](callbacks/).

- `on_msg_callback`: See [Scene Callbacks](callbacks/msg_callbacks)
- `new_obj_callback`: See [Scene Callbacks](callbacks/object_callbacks)
- `user_join_callback`: See [Scene Callbacks](callbacks/user_callbacks)
- `user_left_callback`: See [Scene Callbacks](callbacks/user_callbacks)
- `delete_obj_callback`: See [Scene Callbacks](callbacks/object_callbacks)
- `end_program_callback`: See [Scene Callbacks](callbacks/program_callbacks)

## Environment Variable Args

It is also possible to override these args un `Scene()` using environmental variables at the command line as shown below. This allows a simple way to re-target applications for your own environment without having to change the parameters manually in the code.

```shell
export MQTTH=arenaxr.org # ARENA webserver main host
export SCENE=scene
export NAMESPACE=namespace
python3 program.py
```

Definitions of other [environment variables](/content/python-api/env) are available.

## Command Line Args

The `cli_args` parameter can be used to avoid defining many of these parameters in the `Scene()` object, and expect the user to supply them on the command line. Several have been standardized, and we make it simple to include custom args for your program.

### Simple CLI

If you have scene-dependant settings, like position, rogation, scale, which might change with each scene name change, you can supply them on the command line. Usage:

```shell
python program.py -s example -p -10 0 10 -r 0 45 0 -c 0.5 0.5 0.5
```

Then you can consume them in your program:

```python
scene = Scene(cli_args=True)
scene.add_object(Object(
    object_id="my-parent-object-name",
    position=scene.args["position"],
    rotation=scene.args["rotation"],
    scale=scene.args["scale"],
))
```

This is a list of the most common options available in this mode, (`python3 program.py -h` to view):

```
-h, --help            show this help message and exit
-mh HOST, --host HOST
                        ARENA webserver main host to connect to
-n NAMESPACE, --namespace NAMESPACE
                        Namespace of scene
-s SCENE, --scene SCENE
                        Scene to publish and listen to
-d DEVICE, --device DEVICE
                        Device to publish and listen to
-p POSITION POSITION POSITION, --position POSITION POSITION POSITION
                        App position as cartesian.x cartesian.y cartesian.z
-r ROTATION ROTATION ROTATION, --rotation ROTATION ROTATION ROTATION
                        App rotation as euler.x euler.y euler.z
-c SCALE SCALE SCALE, --scale SCALE SCALE SCALE
                        App scale as cartesian.x cartesian.y cartesian.z
-D, --debug           Debug mode.
```

### Advanced CLI

You can add arbitrary arguments to any arena program.

```shell
python program.py -s example --config ./configuration.json
```

You can specify the dictionary of help text, used in usage help, and the `config` will at least be `None` if unused.
Simply set `cli_args` to true, use `--config` on the CLI, and then reference, but it's a little unsafe if unused.

```python
scene = Scene(cli_args={"config": "The location of the config file to load."})
# scene = Scene(cli_args=True)  # works too!
file = open(scene.args["config"])
```

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
    obj = scene.all_objects[object_id]
    print(obj) # obj should be an object in persist with persist=True
```
