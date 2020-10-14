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

### Program Message
```json
{ "object_id": "6aafedf3-e313-4785-a456-939de8677f07", "action": "update", "persist": true, "type": "program", "data": { "name": "wiselab/arb", "instantiate": "single", "filename": "arb.py", "filetype": "PY", "args": [ "${scene}", "-b", " ${mqtth}" ] }}
```

{% include alert type="warning" title="Arbitrary A-Frame Components" content="
Some A-Frame attributes and components we don't officially include in our JSON may be usable by following certain [patterns of use](../developer/aframe). We make no promises!
"%}

## ARENA MQTT Message Payload JSON Specification

### properties

|name/example|JSON type|description
|--|--|--
| object_id | string | A unique name within the scene (**required**).
| action | string | An action to perform: `create, delete, update, clientEvent` (**required**).
| type | string | Message type: `object, rig, program, mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup`.
| [persist](examples#persisted-objects) | boolean | Save to persistance database (*default: false*).
| [ttl](examples#temporary-objects-ttl) | integer | Time-to-live seconds to persist the object and automatically delete (*default: 0*).
| data | [`Object Data` object](#object-data-object) | The detailed properties of a program. Used by Message Type `object`.
| data | [`Program Data` object](#program-data-object) | The detailed properties of the object. Used by Message Type `program`.

## "Program Data" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| name | string | Name of the program in the format namespace/program-name. e.g. "wiselab/arb" (**required**)
| affinity | string | Indicates the module affinity (client=client's runtime; none or empty=any suitable/available runtime) (*default: "client"*)
| instantiate | string | Single instance of the program (=single), or let every client create a program instance (=client). Per client instance will create new uuid for each program. (*default: "client"*, **required**)
| filename | string | Filename of the entry binary. e.g. "arb.py" (**required**)
| filetype | string | Type of the program (WA=WASM or PY=Python) (*default: "PY"*, **required**)
| args | string array | Command-line arguments (passed in argv). Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} e.g. [ "${scene}", "-b", " ${mqtth}" ]
| env | string array | Environment variables. Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} (*default: [ "MID=${moduleid}", "SCENE=${scene}", "MQTTH=${mqtth}", "REALM=realm" ]*, **required**)
| channels | [`Channel` object](#channel-object) array | Channels describe files representing access to IO from pubsub and client sockets (possibly more in the future; currently only supported for WASM programs). 

## "channel" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| path | string | Folder visible by the program. (*default: "/ch/${scene}"*, **required**)
| type | string | Pubsub or client socket. [ "pubsub", "client" ] (*default: "pubsub"*, **required**)
| mode | string | Access mode. [ "r", "w", "rw" ] (*default: "rw"*, **required**)
| params | [`Params` object](#params-object) | Type (i.e. pubsub/client)-specific parameters.

## "params" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| topic | string | Pubsub topic (pubsub) (*default: "realm/s/${scene}"*)
| host | string | Destination host address (client socket; ignored for now)
| port | number | Destination port (client socket; ignored for now)

## "Object Data" object

### properties

|name/example|JSON type|description
|--|--|--
| object_type | string | An primitive type: `cube, sphere, circle, cone, cylinder, dodecahedron, icosahedron, tetrahedron, octahedron, plane, ring, torus, torusKnot, triangle`
| | | Also: `gltf_model, image, particle, text, line, light, thickline`
| [position](examples#move) | [`Position` object](#position-object)
| [rotation](examples#rotate) | [`Rotation` object](#rotation-object)
| scale | [`scale` object](#scale-object)
| [color](examples#color) | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| [text](examples#text) | string | Any string of [ASCII characters](https://aframe.io/docs/1.0.0/components/text.html#non-ascii-characters). e.g. "Hello world!"
| [click-listener](examples#events) | string | "
| [url](examples#images) | string | URI, relative or full path of a file. e.g. "https://arena.andrew.cmu.edu/models/Duck.glb"
| material | [`Material` object](#material-object)
| multisrc | [`Multisrc` object](#multisrc-object)
| [light](examples#lights) | [`Light` object](#light-object)
| [animation](examples#animate) | [`Animation` object](#animation-object)
| [animation-mixer](examples#animating-gltf-models) | [`Animation-Mixer` object](#animation-mixer-object)
| [start](examples#lines) | [`Position` object](#position-object) | Used by `object_type`: `line`.
| [end](examples#lines) | [`Position` object](#position-object) | Used by `object_type`: `line`.
| [meshline](examples#thicklines) | [`Meshline` object](#meshline-object) | Used by `object_type`: `thickline`.
| [sound](examples#sound) | [`Sound` object](#sound-object)
| [dynamic-body](examples#physics) | [`Dynamic-Body` object](#dynamic-body-object)
| [impulse](examples#physics) | [`Impulse` object](#impulse-object)
| [spe-particles](examples#particles) | [`SPE-Particles` object](#spe-particles-object)
| [environment](examples#background-themes) | [`Environment` object](#environment-object)

## "position" object
Follows A-Frame [position](https://aframe.io/docs/1.0.0/components/position.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | X-axis distance from origin, in meters (*default: 0*, **required**).
| y | float | Y-axis distance from origin, in meters (*default: 0*, **required**).
| z | float | Z-axis distance from origin, in meters (*default: 0*, **required**).

## "rotation" object
Follows A-Frame [rotation](https://aframe.io/docs/1.0.0/components/rotation.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | Quaternion rotation around the X-axis (*default: 0*, **required**).
| y | float | Quaternion rotation around the Y-axis (*default: 0*, **required**).
| z | float | Quaternion rotation around the Z-axis (*default: 0*, **required**).
| w | float | Quaternion value for theta (*default: 1*, **required**).

## "scale" object
Follows A-Frame [scale](https://aframe.io/docs/1.0.0/components/scale.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | X-axis length of object, in meters (*default: 1*, **required**).
| y | float | Y-axis length of object, in meters (*default: 1*, **required**).
| z | float | Z-axis length of object, in meters (*default: 1*, **required**).

## "material" object
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
| repeat | [`Repeat` object](#repeat-object) | Used by `material`: `repeat`.

## "repeat" object
Follows A-Frame [repeating-textures](https://aframe.io/docs/1.0.0/components/material.html#repeating-textures).

### properties

|name/example|JSON type|description
|--|--|--
| x | float | e.g. 4 (**required**).
| y | float | e.g. 4 (**required**).

## "multisrc" object

### properties

|name/example|JSON type|description
|--|--|--
| srcspath | string | URI, relative or full path of a directory containing `srcs`, e.g. "images/dice/" (**required**).
| srcs | string | A comma-delimited list if URIs, e.g. "side1.png, side2.png, side3.png, side4.png, side5.png, side6.png" (**required**).

## "light" object
Follows A-Frame [light](https://aframe.io/docs/1.0.0/components/light.html).

### properties

|name/example|JSON type|description
|--|--|--
| type | string | e.g. "directional" (**required**).

## "animation" object
Follows A-Frame [animation](https://aframe.io/docs/1.0.0/components/animation.html).

### properties

|name/example|JSON type|description
|--|--|--
| property | string | e.g. "rotation"
| to | string | e.g. "0 360 0"
| loop | boolean | e.g. true
| dur | integer | e.g. 10000

## "animation-mixer" object
Follows Don McCurdy’s [animation-mixer](https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation).

### properties

|name/example|JSON type|description
|--|--|--
| clip | string | e.g. "*"

## "meshline" object

### properties

|name/example|JSON type|description
|--|--|--
| lineWidth | integer | e.g. 11 (**required**).
| color | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*) (**required**).
| path | string | e.g. "0 0 0, 0 0 1" (**required**).

## "sound" object
Follows A-Frame [sound](https://aframe.io/docs/1.0.0/components/sound.html).

### properties

|name/example|JSON type|description
|--|--|--
| src | string | URI, relative or full path of a directory containing a sound file, e.g. "url(https://arena.andrew.cmu.edu/audio/toypiano/Asharp1.wav)" (**required**).
| on | string | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).

## "dynamic-body" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system#dynamic-body-and-static-body).

### properties

|name/example|JSON type|description
|--|--|--
| type | string | `none, static, dynamic` (**required**).

## "impulse" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system).

### properties

|name/example|JSON type|description
|--|--|--
| on | string | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).
| force | string | e.g. "1 50 1" (**required**).
| position | string | e.g. "1 1 1" (**required**).

## "spe-particles" object
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

## "environment" object

### properties

|name/example|JSON type|description
|--|--|--
| preset | string | e.g. `none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris`

