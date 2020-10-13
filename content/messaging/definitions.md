---
title: Function Definitions
nav_order: 3
layout: default
parent: Messaging Format
---

# Messaging Format Function Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

{% include alert type="warning" title="Coming Soon" content="Writing in progress..."%}

```json
{
    "object_id": "cube_1",          | str  | unique name within the scene (required)
    "action": "create",             | str  | create, delete, update, clientEvent (required)
    "type": "object",               | str  | object, rig, mousedown, mouseup, mouseenter, 
                                             mouseleave, triggerdown, triggerup, gripdown, 
                                             gripup, menudown, menuup, systemdown, systemup, 
                                             trackpaddown, trackpadup
    "persist": false,               | bool | true = save to persistance database
    "ttl": 5,                       | num  | ttl seconds to persist and automatically delete
    "data": {
        "object_type": "cube",      | str  | cube, sphere, circle, cone, cylinder, dodecahedron,
                                             icosahedron, tetrahedron, octahedron, plane, ring,
                                             torus, torusKnot, triangle, gltf_model, image,
                                             particle, text, line, light, thickline
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
