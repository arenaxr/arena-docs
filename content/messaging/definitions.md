---
title: Function Definitions
nav_order: 3
layout: default
parent: Messaging Format
---

# Messaging Format Function Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

{% include alert type="warning" title="Coming Soon" content="Writing in progress..."%}

## Examples

The following example shows the current full suite of object parameters possible:

```json
{
    "object_id": "cube_1",
    "action": "create",
    "type": "object",
    "persist": false,
    "ttl": 5,
    "data": {
        "object_type": "cube",
        "position": {
            "x": 0,                    
            "y": 0,
            "z": 0
        },
        "rotation": {
            "x": 0,
            "y": 0,
            "z": 0,
            "w": 1
        },
        "scale": {
            "x": 1,
            "y": 1,
            "z": 1
        },
        "color": "#ffffff",
        "text": "Hello world!", 
        "click-listener": "",
        "url": "https://arena.andrew.cmu.edu/models/Duck.glb",
        "material": {
            "src": "images/360falls.mp4",
            "transparent": true, 
            "opacity": 0.5,
            "colorWrite": false, 
            "render-order": "0",
            "side": "back",
            "color": "blue",
            "repeat": {
                "x": 4,
                "y": 4
            }
        },
        "multisrc": {
            "srcspath": "images/dice/",
            "srcs": "side1.png, side2.png, side3.png, side4.png, side5.png, side6.png"
        },
        "light": {
            "type": "directional"
        },
        "animation": {
            "property": "rotation",
            "to": "0 360 0",
            "loop": true,
            "dur": 10000
        },
        "animation-mixer": {
            "clip": "*"
        },
        "start": {
            "x": 2,
            "y": 2,
            "z": 2
        },
        "end": {
            "x": 3,
            "y": 3,
            "z": 3
        },
        "meshline": {
            "lineWidth": 11,
            "color": "#FFFFFF",
            "path": "0 0 0, 0 0 1"
        },
        "sound": {
            "src": "url(https://arena.andrew.cmu.edu/audio/toypiano/Asharp1.wav)",
            "on": "mousedown"
        },
        "dynamic-body": {
            "type": "dynamic"
        },
        "impulse": {
            "on": "mouseup",
            "force": "1 50 1",
            "position": "1 1 1"
        },
        "spe-particles": {
            "texture": "textures/square.png",
            "color": "yellow, red",
            "particleCount": 3,
            "maxAge": 0.5,
            "maxAgeSpread": 1,
            "velocity": "40 200 40",
            "velocitySpread": "10 3 10",
            "wiggle": "50 0 50",
            "wiggleSpread": "15 0 15",
            "emitterScale": 8,
            "sizeSpread": 10,
            "randomizeVelocity": true
        },
    }
}
```

## Object Message

### properties

|name/example|JSON type|description|
|--|--|--|
| object_id          | string  | A unique name within the scene (**required**). |
| action             | string  | An action to perform: `create, delete, update, clientEvent` (**required**). |
| type               | string  | Message type: `object, rig, mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown,  gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup`. |
| [persist](examples#persisted-objects) | boolean | Save to persistance database (*default: false*). |
| [ttl](examples#temporary-objects-ttl) | integer | Time-to-live seconds to persist the object and automatically delete (*default: 0*). |
| data               | [`Data` element](#data-element) | The detailed properties of the object. | 

## "Data" element

### properties

|name/example|JSON type|description|
|--|--|--|
| object_type | string  | An object type: `cube, sphere, circle, cone, cylinder, dodecahedron, icosahedron, tetrahedron, octahedron, plane, ring, torus, torusKnot, triangle, gltf_model, image, particle, text, line, light, thickline`. |
| [position](examples#move) | [`Position` element](#position-element) |  |
| [rotation](examples#rotate) | [`Rotation` element](#rotation-element) |  |
| scale | [`scale` element](#scale-element) |  |
| [color](examples#color) | string | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#ffffff"*). |
| [text](examples#text) | string | Any string of [ASCII characters](https://aframe.io/docs/1.0.0/components/text.html#non-ascii-characters). |
| [click-listener](examples#events) | string | "" |
| [url](examples#images) | string | URI, relative or full path. |  
| material | [`Material` element](#material-element) |  |
| multisrc | [`Multisrc` element](#multisrc-element) |  |
| [light](examples#lights) | [`Light` element](#light-element) |  |
| [animation](examples#animate) | [`Animation` element](#animation-element) |  |
| [animation-mixer](examples#animating-gltf-models) | [`Animation-Mixer` element](#animation-mixer-element) |  |
| [start](examples#lines) | [`Start` element](#start-element) | Used by `object_type`: `line`.  |
| [end](examples#lines) | [`End` element](#end-element) | Used by `object_type`: `line`.  |
| [meshline](examples#meshline) | [`Meshline` element](#meshline-element) | Used by `object_type`: `thickline`. |
| [sound](examples#sound) | [`Sound` element](#sound-element) |  |
| [dynamic-body](examples#physics) | [`Dynamic-Body` element](#dynamic-body-element) |  |
| [impulse](examples#physics) | [`Impulse` element](#impulse-element) |  |
| [spe-particles](examples#particles) | [`SPE-Particles` element](#spe-particles-element) |  |

## "position" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "rotation" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "scale" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "color" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "text" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "click-listener" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "url" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "material" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "multisrc" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "light" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "animation" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "animation-mixer" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "start" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "end" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "meshline" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "sound" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "dynamic-body" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "impulse" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||

## "spe-particles" element

### properties

|name/example|JSON type|description|
|--|--|--|
||||
