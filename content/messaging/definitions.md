---
title: Function Definitions
nav_order: 3
layout: default
parent: Messaging Format
---

# Messaging Format Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

{% include alert type="warning" title="Coming Soon" content="Writing in progress..."%}

## Examples

### Object Message
```json
{"object_id" : "cube_1", "action": "create", "type": "object", "data": {"object_type": "cube", "position": {"x": 1, "y": 1, "z": -1}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}, "color": "#FF0000"}}
```

### Event Message
```json
{"object_id":"fallBox2", "action":"clientEvent", "type":"mousedown", "data":{"position":{"x":-0.993, "y":0.342, "z":-1.797}, "source":"camera_8715_er"}}
```

### Environment Message
```json
{"object_id" : "env", "action": "update", "type": "object", "data": {"environment": {"preset": "arches"}}}
```

## ARENA MQTT Message Payload JSON Specification

### properties

|name/example|JSON type|description
|--|--|--
| object_id | string | A unique name within the scene (**required**).
| action | string | An action to perform: `create, delete, update, clientEvent` (**required**).
| type | string | Message type: `object, rig, mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup`.
| [persist](examples#persisted-objects) | boolean | Save to persistance database (*default: false*).
| [ttl](examples#temporary-objects-ttl) | integer | Time-to-live seconds to persist the object and automatically delete (*default: 0*).
| data | [`Data` element](#data-element) | The detailed properties of the object.

## "Data" element

### properties

|name/example|JSON type|description
|--|--|--
| object_type | string  | An object type: `cube, sphere, circle, cone, cylinder, dodecahedron, icosahedron, tetrahedron, octahedron, plane, ring, torus, torusKnot, triangle, gltf_model, image, particle, text, line, light, thickline`.
| [position](examples#move) | [`Position` element](#position-element)
| [rotation](examples#rotate) | [`Rotation` element](#rotation-element)
| scale | [`scale` element](#scale-element)
| [color](examples#color) | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| [text](examples#text) | string | Any string of [ASCII characters](https://aframe.io/docs/1.0.0/components/text.html#non-ascii-characters). e.g. "Hello world!"
| [click-listener](examples#events) | string | ""
| [url](examples#images) | string | URI, relative or full path of a file. e.g. "https://arena.andrew.cmu.edu/models/Duck.glb"
| material | [`Material` element](#material-element)
| multisrc | [`Multisrc` element](#multisrc-element)
| [light](examples#lights) | [`Light` element](#light-element)
| [animation](examples#animate) | [`Animation` element](#animation-element)
| [animation-mixer](examples#animating-gltf-models) | [`Animation-Mixer` element](#animation-mixer-element)
| [start](examples#lines) | [`Position` element](#position-element) | Used by `object_type`: `line`.
| [end](examples#lines) | [`Position` element](#position-element) | Used by `object_type`: `line`.
| [meshline](examples#thicklines) | [`Meshline` element](#meshline-element) | Used by `object_type`: `thickline`.
| [sound](examples#sound) | [`Sound` element](#sound-element)
| [dynamic-body](examples#physics) | [`Dynamic-Body` element](#dynamic-body-element)
| [impulse](examples#physics) | [`Impulse` element](#impulse-element)
| [spe-particles](examples#particles) | [`SPE-Particles` element](#spe-particles-element)
| [environment](examples#background-themes) | [`Environment` element](#environment-element)

## "position" element
Follows A-Frame [position](https://aframe.io/docs/1.0.0/components/position.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | X-axis distance from origin, in meters (*default: 0*, **required**).
| y | float | Y-axis distance from origin, in meters (*default: 0*, **required**).
| z | float | Z-axis distance from origin, in meters (*default: 0*, **required**).

## "rotation" element
Follows A-Frame [rotation](https://aframe.io/docs/1.0.0/components/rotation.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | Quaternion rotation around the X-axis (*default: 0*, **required**).
| y | float | Quaternion rotation around the Y-axis (*default: 0*, **required**).
| z | float | Quaternion rotation around the Z-axis (*default: 0*, **required**).
| w | float | Quaternion value for theta (*default: 1*, **required**).

## "scale" element
Follows A-Frame [scale](https://aframe.io/docs/1.0.0/components/scale.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | X-axis length of object, in meters (*default: 1*, **required**).
| y | float | Y-axis length of object, in meters (*default: 1*, **required**).
| z | float | Z-axis length of object, in meters (*default: 1*, **required**).

## "material" element
Follows A-Frame [material](https://aframe.io/docs/1.0.0/components/material.html).

### properties

|name/example|JSON type|description
|--|--|--
| src | string | URI, relative or full path of an image/video file. e.g. "images/360falls.mp4"
| transparent | boolean | e.g. true
| opacity | float | e.g. 0.5
| colorWrite | boolean | e.g. false
| render-order | string | e.g. "0"
| side | string | e.g. "back"
| color | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| repeat | [`Repeat` element](#repeat-element) | Used by `material`: `repeat`.

## "repeat" element
Follows A-Frame [repeating-textures](https://aframe.io/docs/1.0.0/components/material.html#repeating-textures).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | e.g. 4 (**required**).
| y | float | e.g. 4 (**required**).

## "multisrc" element

### properties

|name/example|JSON type|description
|--|--|--
| srcspath | string | URI, relative or full path of a directory containing `srcs`, e.g. "images/dice/" (**required**).
| srcs | string | A comma-delimited list if URIs, e.g. "side1.png, side2.png, side3.png, side4.png, side5.png, side6.png" (**required**).

## "light" element
Follows A-Frame [light](https://aframe.io/docs/1.0.0/components/light.html).

### properties

|name/example|JSON type|description
|--|--|--
| type | string | e.g. "directional" (**required**).

## "animation" element
Follows A-Frame [animation](https://aframe.io/docs/1.0.0/components/animation.html).

### properties

|name/example|JSON type|description
|--|--|--
| property | string | e.g. "rotation"
| to | string | e.g. "0 360 0"
| loop | boolean | e.g. true
| dur | integer | e.g. 10000

## "animation-mixer" element
Follows Don McCurdy’s [animation-mixer](https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation).

### properties

|name/example|JSON type|description
|--|--|--
| clip | string | e.g. "*"

## "meshline" element

### properties

|name/example|JSON type|description
|--|--|--
| lineWidth | integer | e.g. 11 (**required**).
| color | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*) (**required**).
| path | string | e.g. "0 0 0, 0 0 1" (**required**).

## "sound" element
Follows A-Frame [sound](https://aframe.io/docs/1.0.0/components/sound.html).

### properties

|name/example|JSON type|description
|--|--|--
| src | string | URI, relative or full path of a directory containing a sound file, e.g. "url(https://arena.andrew.cmu.edu/audio/toypiano/Asharp1.wav)" (**required**).
| on | string | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).

## "dynamic-body" element
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system#dynamic-body-and-static-body).

### properties

|name/example|JSON type|description
|--|--|--
| type | string | `none, static, dynamic` (**required**).

## "impulse" element
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system).

### properties

|name/example|JSON type|description
|--|--|--
| on | string | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).
| force | string | e.g. "1 50 1" (**required**).
| position | string | e.g. "1 1 1" (**required**).

## "spe-particles" element
Follows [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component#aframe-spe-particles-component).

### properties

|name/example|JSON type|description
|--|--|--
| texture | string | e.g. "textures/square.png"
| color | string | e.g. "yellow, red"
| particleCount | integer | e.g. 3
| maxAge | float | e.g. 0.5
| maxAgeSpread | integer | e.g. 1
| velocity | string | e.g. "40 200 40"
| velocitySpread | string | e.g. "10 3 10"
| wiggle | string | e.g. "50 0 50"
| wiggleSpread | string | e.g. "15 0 15"
| emitterScale | float | e.g. 8
| sizeSpread | float | e.g. 10
| randomizeVelocity | boolean | e.g. true

## "environment" element

### properties

|name/example|JSON type|description
|--|--|--
| preset | string | e.g. `none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris`

