---
title: Object Definitions Reference
nav_order: 1
layout: default
parent: ARENA Objects
---

# ARENA Object

ARENA objects follow the structure of [`Scene Message object`](#scene-message-object), with general object properties, paired with a more granular detailed `data` sub-object which varies in form and follow the examples below.

ARENA 3D Environment is built on top of [A-Frame](https://aframe.io/), and it supports the majority of A-Frame's primitives (e.g., geometries like boxes, circles, spheres) and components (that can be attached to objects, such as position, rotation, material, sound). See our [clarification of the relationship](/content/schemas/#arena-objects-and-a-frame) between ARENA and A-Frame properties.

{% include alert type="tip" title="Tip" content="
In most cases, arbitrary A-Frame properties which are applied in HTML as attributes can be applied to ARENA Objects. We link the corresponding A-Frame object definition for completeness in the tables below.
"%}

## Over-the-Wire Message Examples

ARENA object schemas are the basis for the over-the-wire message format. Below you can find some additional message examples and links to the respective object definitions.

### Object Message

[`Scene Message object`](#scene-message-object) with a `data` property of the `Object Data` object.

```json
{
  "object_id": "cube_1",
  "action": "create",
  "type": "object",
  "data": {
    "object_type": "box",
    "position": { "x": 1, "y": 1, "z": -1 },
    "rotation": { "x": 0, "y": 0, "z": 0, "w": 1 },
    "scale": { "x": 1, "y": 1, "z": 1 },
    "material": { "color": "#FF0000" }
  }
}
```

### Event Message

[`Scene Message object`](#scene-message-object) with a `data` property of the `Event Data` object.

```json
{
  "object_id": "fallBox2",
  "action": "clientEvent",
  "type": "mousedown",
  "data": {
    "position": { "x": -0.993, "y": 0.342, "z": -1.797 },
    "source": "camera_8715_er"
  }
}
```

### Program Message

[`Scene Message object`](#scene-message-object) with a `data` property of the `Program Data` object.

```json
{
  "object_id": "6aafedf3-e313-4785-a456-939de8677f07",
  "action": "update",
  "persist": true,
  "type": "program",
  "data": {
    "name": "wiselab/arb",
    "instantiate": "single",
    "filename": "arb.py",
    "filetype": "PY",
    "args": ["${scene}", "-b", " ${mqtth}"]
  }
}
```

### Scene Options Message

[`Scene Message object`](#scene-message-object) with a `data` property of the `Scene Options Data` object.

```json
{
  "object_id": "e9a16478-2606-4cd0-bb9f-b03879bc8baa",
  "action": "update",
  "persist": true,
  "type": "scene-options",
  "data": {
    "env-presets": {
      "active": true,
      "lighting": "distant",
      "lightPosition": { "x": 0, "y": 1, "z": -10 },
      "ground": "hills",
      "groundTexture": "squares",
      "groundColor": "#444241",
      "groundYScale": 0.5
    },
    "scene-options": {
      "jitsiServer": "jitsi1.andrew.cmu.edu",
      "clickableOnlyEvents": true,
      "privateScene": true
    }
  }
}
```

---

## "Scene Message" object

This is the primary payload body of every MQTT scene topic in the ARENA.

**See our [reference of ARENA supported objects and their properties](/content/schemas/message).**

---

## Actions

The `create`, `update`, and `delete` actions are similar to typical C\(R\)UD operations.

- `create` - _Upserts_ an object. If the object already does exist, `data` fields will be _merged_.
- `update` - Merges the `data` attributes with a currently existing object. To **remove** an attribute, set the value
  to `null`.
- `delete` - Delete an object. No data field required.
