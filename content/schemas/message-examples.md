---
title: PubSub Messages
nav_order: 3
layout: default
parent: ARENA Objects
---

# Formatting PubSub Messages

For debugging purposes, or to create your own ARENA client software, it can be helpful to interact with ARENA's PubSub messaging directly. Here we describe some examples of doing this.

## Messaging Format Overview

All ARENA objects have similar well-defined schemas, and these are the basis for the over-the-wire message format shown below. This is the message format transmitted over the PubSub to create/update/delete objects. If you leave out required fields, defaults will be used.

```json
{
  "object_id": "dinosaur",
  "persist": true,
  "type": "object",
  "action": "update",
  "data": {
    "object_type": "gltf-model",
    "url": "https://www.dropbox.com/s/pgytn552kzukm8f/blumbach.glb?dl=0",
    "position": { "x": 0, "y": 1.7, "z": -5 },
    "rotation": { "x": 0, "y": 0.38268, "z": 0, "w": 0.92388 },
    "scale": { "x": 1, "y": 1, "z": 1 },
    "shadow": { "cast": true, "receive": true }
  }
}
```

## Sample Publish/Subscribe

To run the commands below, you may need to install the [ARENA Python client](/content/python) which includes these scripts.

### Subscribe to Scene Object Messages

```bash
arena-py-sub -mh arenaxr.org -s example
```

### Publish a Scene Object Message

```bash
arena-py-pub -mh arenaxr.org -s example -m '{"object_id": "gltf-model_Earth", "action": "create", "type": "object", "data": {"object_type": "gltf-model", "position": {"x":0, "y": 0.1, "z": 0}, "url": "store/models/Earth.glb", "scale": {"x": 5, "y": 5, "z": 5}}}
```

## Sample scene: Earth and Moon with Markers

MQTT messages that define the scene:

### Create models

```json
{
  "object_id": "gltf-model_Earth",
  "action": "create",
  "type": "object",
  "data": {
    "object_type": "gltf-model",
    "position": { "x": 0, "y": 0.1, "z": 0 },
    "url": "store/models/Earth.glb",
    "scale": { "x": 5, "y": 5, "z": 5 }
  }
}
```

```json
{
  "object_id": "gltf-model_Moon",
  "action": "create",
  "type": "object",
  "data": {
    "parent": "gltf-model_Earth",
    "object_type": "gltf-model",
    "position": { "x": 0, "y": 0.05, "z": 0.6 },
    "scale": { "x": 0.05, "y": 0.05, "z": 0.05 },
    "url": "store/models/Moon.glb"
  }
}
```

### Define animation and movement

```json
{
  "object_id": "gltf-model_Earth",
  "action": "update",
  "type": "object",
  "data": {
    "animation": {
      "property": "rotation",
      "to": "0 360 0",
      "loop": true,
      "dur": 20000,
      "easing": "linear"
    }
  }
}
```

```json
{
  "object_id": "gltf-model_Earth",
  "action": "update",
  "type": "object",
  "data": {
    "startEvents": "click",
    "property": "scale",
    "dur": 1000,
    "from": "10 10 10",
    "to": "5 5 5",
    "easing": "easeInOutCirc",
    "loop": 5,
    "dir": "alternate"
  }
}
```

### Add a click-listener

```json
{
  "object_id": "gltf-model_Earth",
  "action": "update",
  "type": "object",
  "data": { "click-listener": "" }
}
```

### Create marker objects

```json
{
  "object_id": "box0",
  "action": "create",
  "type": "object",
  "data": {
    "object_type": "box",
    "scale": { "x": 0.2, "y": 0.2, "z": 0.2 },
    "position": { "x": 0, "y": 0, "z": 0 },
    "material": { "color": "blue" }
  }
}
```

```json
{
  "object_id": "box1",
  "action": "create",
  "type": "object",
  "data": {
    "material": { "color": "red" },
    "object_type": "box",
    "scale": { "x": 0.2, "y": 0.2, "z": 0.2 },
    "position": { "x": -0.7, "y": 1.67, "z": 2.11 }
  }
}
```

```json
{
  "object_id": "box2",
  "action": "create",
  "type": "object",
  "data": {
    "material": { "color": "red" },
    "object_type": "box",
    "scale": { "x": 0.2, "y": 0.2, "z": 0.2 },
    "position": { "x": -2.88, "y": 2.8, "z": -2.12 }
  }
}
```

```json
{
  "object_id": "box3",
  "action": "create",
  "type": "object",
  "data": {
    "material": { "color": "red" },
    "object_type": "box",
    "scale": { "x": 0.2, "y": 0.2, "z": 0.2 },
    "position": { "x": -0.09, "y": 1.3, "z": -3.66 }
  }
}
```

```json
{
  "object_id": "box4",
  "action": "create",
  "type": "object",
  "data": {
    "material": { "color": "red" },
    "object_type": "box",
    "scale": { "x": 0.2, "y": 0.2, "z": 0.2 },
    "position": { "x": 3.31, "y": 2.0, "z": -0.97 }
  }
}
```
