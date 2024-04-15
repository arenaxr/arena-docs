---
title: Atmosphere
nav_order: 9.5
layout: tutorial
parent: Tutorial
---

# Atmosphere

## Environment Presets

```json
{
  "object_id": "scene-options",
  "type": "scene-options",
  "data": {
    "env-presets": {
      "active": true,
      "preset": "forest"
    }
  }
}
```

## Sky, Ground, Fog

```json
{
  "object_id": "scene-options",
  "type": "scene-options",
  "data": {
    "env-presets": {
      "active": true,
      "preset": "none",
      "dressing": "mushrooms",
      "fog": 0.5,
      "ground": "hills",
      "groundTexture": "walkernoise",
      "lighting": "distant",
      "skyType": "atmosphere"
    }
  }
}
```


## Weather

Sounds...

### Rain

```json
{
  "object_id": "rain",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "rotation": 3.14,
      "particleCount": 1000,
      "texture": "static/images/textures/raindrop.png",
      "positionSpread": { "x": 100, "y": 100, "z": 100 },
      "acceleration": { "x": 0, "y": 3, "z": 0 },
      "accelerationSpread": { "x": 2, "y": 1, "z": 2 },
      "velocitySpread": { "x": 10, "y": 50, "z": 10 },
      "velocity": { "x": 0, "y": 75, "z": 0 },
      "blending": "additive",
      "color": ["#ffffff"],
      "maxAge": 1,
      "size": [0.4]
    }
  }
}
```

### Snow

```json
{
  "object_id": "snow",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "rotation": 3.14,
      "texture": "static/images/textures/smokeparticle.png",
      "particleCount": 200,
      "positionSpread": { "x": 100, "y": 100, "z": 100 },
      "acceleration": { "x": 0, "y": 0, "z": 0 },
      "accelerationSpread": { "x": 0.2, "y": 0, "z": 0.2 },
      "velocitySpread": { "x": 2, "y": 0, "z": 2 },
      "blending": "additive",
      "color": ["#ffffff"],
      "velocity": { "x": 0, "y": 8, "z": 0 },
      "maxAge": 20
    }
  }
}
```

### Dust

```json
{
  "object_id": "dust",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "rotation": 3.14,
      "texture": "static/images/textures/smokeparticle.png",
      "particleCount": 100,
      "positionSpread": { "x": 100, "y": 100, "z": 100 },
      "acceleration": { "x": 0, "y": 0, "z": 0 },
      "accelerationSpread": { "x": 0, "y": 0, "z": 0 },
      "velocitySpread": { "x": 0.5, "y": 1, "z": 0.5 },
      "velocity": { "x": 1, "y": 0.3, "z": 1 },
      "color": ["#ffffff"],
      "blending": "additive",
      "maxAge": 20
    }
  }
}
```

### Fire

Multiple...

```json
{
  "object_id": "smoke",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "texture": "static/images/textures/fog.png",
      "velocity": { "x": 0.4, "y": 2, "z": 0 },
      "velocitySpread": { "x": 1.4, "y": 0, "z": 1.4 },
      "particleCount": 50,
      "maxAge": 4,
      "size": [8, 16],
      "opacity": [0, 1, 0],
      "color": ["#666", "#222"]
    }
  }
}
```

```json
{
  "object_id": "sparks",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "texture": "static/images/textures/square.png",
      "color": ["yellow", "red"],
      "particleCount": 10,
      "maxAge": 0.5,
      "maxAgeSpread": 0.4,
      "velocity": { "x": 0, "y": 5, "z": 0 },
      "velocitySpread": { "x": 0, "y": 3, "z": 0 },
      "wiggle": 1,
      "wiggleSpread": 5,
      "emitterScale": 50,
      "sizeSpread": [0.5],
      "randomizeVelocity": true
    }
  }
}
```

```json
{
  "type": "object",
  "object_id": "flames",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "texture": "/static/images/textures/explosion_sheet.png",
      "textureFrames": { "x": 5, "y": 5 },
      "velocity": { "x": 0.4, "y": 0.1, "z": 0 },
      "acceleration": { "x": 0, "y": 2, "z": 0 },
      "accelerationSpread": { "x": 0, "y": 2, "z": 0 },
      "velocitySpread": { "x": 0.4, "y": 0, "z": 0.4 },
      "particleCount": 15,
      "maxAge": 1,
      "size": [4, 8],
      "sizeSpread": [2],
      "opacity": [1, 0],
      "wiggle": 0,
      "blending": "additive"
    }
  }
}
```
