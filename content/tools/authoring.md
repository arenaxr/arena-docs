---
title: Authoring Program
nav_order: 1
layout: default
parent: Tools
---

# ARENA AR Builder

An AR/VR capable editing tool to create/manipulate/delete ARENA objects. See top-level Python documentation for [requirements](https://github.com/arenaxr/arena-py). This tool uses the [ARENA Persistence Database](https://github.com/arenaxr/arena-persist), so all changes are persisted.

## Quick Start

1. Clone our Python repo [https://github.com/arenaxr/arena-py](https://github.com/arenaxr/arena-py).
1. Usage: `arb` takes at minimum one argument, the first one, a scene name (`hello` in this example).
   ```shell
   python3 tools/arb/arb.py hello
   ```
1. Interact with the tool at https://arenaxr.org/[your username]/hello

## Demo Video

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bYantKzkTFk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

## Usage

```
usage: arb.py [-h] [-n NAMESPACE] [-b BROKER] [-p PORT] [-r REALM] [-m MODELS] [-d] scene

ARENA AR Builder.

positional arguments:
  scene                 ARENA scene name

optional arguments:
  -h, --help            show this help message and exit
  -n NAMESPACE, --namespace NAMESPACE
                        ARENA namespace
  -b BROKER, --broker BROKER
                        MQTT message broker hostname
  -p PORT, --port PORT  MQTT message broker port
  -r REALM, --realm REALM
                        ARENA realm name
  -m MODELS, --models MODELS
                        JSON GLTF manifest
  -d, --debug           Debug mode.
```

## EDIT Button
The `edit` button will update all objects in the scene with click-listeners, allowing you to target ARB commands to any object. Toggling the `edit` button **on**, updates the scene `scene-options` object and will remind you to reload the page for edit mode to fully activate. You may see an <span style="color: orange;">orange warning</span> in the upper left that [Events Publish Behavior is too high](/content/troubleshooting.html#warning-events-publish-behavior-is-too-high), which is expected and a reminder to toggle the `edit` button **off**, when finished editing the scene with ARB.

## Basic Object Manipulation
When you set the mode to None, Rotate, Nudge, Stretch, Scale, you can manipulate objects in various ways.

### AR One-Finger, VR Left-Click
- Tap 1 finger with reticle (AR) or cursor (VR) on the cones to activate one-direction granular manipulation.

### AR Two-Finger
- Tap and hold 2 thumbs with reticle (AR) on the cones to activate free manipulation along that axis.
- Move the device in AR to position, scale and rotate.

### AR Three-Finger
- Tap and hold 2 thumbs and tap 1 more finger to toggle modes: None, Rotate, Nudge, Stretch, Scale.

## Control Panel

![AR Builder Panel](/assets/img/arb-panel.png)

- **VR Mode**: Click and hold your mouse to move your camera relative to the panel.
- **AR Mode**: Move your AR device to move your camera relative to the panel.
- **All Modes**: Use the **lock** button to reposition the panel relative to your camera's rotation.

| Button      | Type     | Description                                                                                                                                                                                                                                                   |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **color**   | _action_ | Allows color select; tap object to color it _(default=#ffffff)_.                                                                                                                                                                                              |
| **create**  | _action_ | Allows shape select; tap clipboard object to create it in place _(default=sphere)_.                                                                                                                                                                           |
| **delete**  | _action_ | Tap object to delete it.                                                                                                                                                                                                                                      |
| **edit**    | _toggle_ | Turns on click-listeners for every object in the scene via changing the scene-options object. Requires page reload _(default=off)_.                                                                                                                           |
| **lamp**    | _toggle_ | Turn a headlamp on/off _(default=off)_.                                                                                                                                                                                                                      |
| **lock**    | _toggle_ | Off=panel maintains relative world position; On=panel follows camera rotation _(default=off)_.                                                                                                                                                                |
| **model**   | _action_ | Allows GLTF model select; tap clipboard object to create it in place _(default=duck.glb)_. Models may be imported via the **-m** argument _(see below)_.                                                                                                      |
| **move**    | _action_ | Tap an object to show it in the clipboard, tap clipboard object to move it to that place.                                                                                                                                                                     |
| **nudge**   | _action_ | Tap an object to show yellow nudge-lines, then tap a cone to nudge the object in that direction according to selected granularity _(default=mm)_ Allows mm, cm, dm, m granularity.                                                                            |
| **occlude** | _action_ | Allows occlusion on/off select; tap object to occlude it _(default=on)_.                                                                                                                                                                                      |
| **parent**  | _action_ | Allows setting of parent object; first tap the parent object, then tap the child object.                                                                                                                                                                      |
| **redpill** | _toggle_ | Reveals useful debug data: **_gridlines_** on the floor (y=0) can be seen from above and below, **_occlusion mask_** will show all occluded objects, **_object data_** mouse hover on an object will show its position, rotation, and scale _(default=off)_. |
| **rename**  | _action_ | Allows typing a new name; start typing or just tap an object to load the old name into the editor, then tap the object to apply the new name to.                                                                                                              |
| **rotate**  | _action_ | Tap an object to show orange rotate-lines, then tap a cone to change object rotation according to selected granularity _(default=1°)_. Allows 1°, 5°, 10°, 45°, 90° Euler angle granularity; Additional 6Dof lines will show degree of rotation.              |
| **scale**   | _action_ | Tap an object to show blue scale-lines, then tap a cone to increase or decrease object scale according to selected granularity _(default=mm)_.                                                                                                                |
| **slider**  | _toggle_ | Off=Object manipulation via two-finger hold and move camera, On=Object manipulation via two-finger swipe _(default=off)_.                                                                                                                                     |
| **stretch** | _action_ | Allows altering scale in one of 6Dof.                                                                                                                                                                                                                         |
| **wall**    | _action_ | Allows creation of a basic wall 0.1m thick; tap clipboard brick once with your AR device flush with one corner of the wall, and tap the second time at the opposing corner. Three alignment markers will appear for 2 minutes.                                |

## Clipboard

The clipboard is a temporary see-through object floating in front of the user used to show the relative position of placing a future object. It's also used in AR to have something to fire an event at where no object currently exists.

## Construction Cone

There is a small temporary object resting on position 0,0,0 in the shape of a construction cone to mark the origin of the scene. It will be removed when `arb` stops running.

## Run Options

### Importing Models

You can import a json-formatted manifest of GLTF models using the command argument **-m** to use on the **model** control panel option. You can write your own, or use the example, [arb-manifest.json](https://github.com/arenaxr/arena-py/blob/master/tools/arb/arb-manifest.json).

```shell
python3 tools/arb/arb.py hello -m arb-manifest.json
```

Scale varies widely between individual models, so experiment with the best scale to start with.

`arb-manifest.json`

```json
{
  "models": [
    {
      "name": "avocado",
      "url_gltf": "store/models/Avocado.glb",
      "scale": 1
    },
    {
      "name": "shuttle",
      "url_gltf": "store/models/Shuttle.glb",
      "scale": 5
    },
    {
      "name": "duck",
      "url_gltf": "store/models/Duck.glb",
      "scale": 0.2
    },
    {
      "name": "earth",
      "url_gltf": "store/models/Earth.glb",
      "scale": 2
    },
    {
      "name": "lantern",
      "url_gltf": "store/models/Lantern.glb",
      "scale": 0.015
    },
    {
      "name": "camera",
      "url_gltf": "store/models/AntiqueCamera.glb",
      "scale": 0.05
    }
  ]
}
```

### MQTT Host and Realm

By default all `arb` MQTT messages are published to the default message broker and topic (realm and scene you specify) using this scheme:

- _default broker_: `oz.andrew.cmu.edu`
- _default topic_: `realm/s/[your namespace]/hello`

To use your own MQTT message broker (**-b**) and/or realm (**-r**):

- _custom broker_: `arena-west1.conix.io`
- _custom topic_: `foo/s/[your namespace]/hello`

```shell
python tools/arb/arb.py hello -b arena-west1.conix.io -r foo
```
