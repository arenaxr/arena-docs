---
title: Atmosphere
nav_order: 9.5
layout: tutorial
parent: Tutorial
---

# Atmosphere

You can provide your scenes with a sense of atmosphere by adding features that enhance your scene, such as: **terrain, water, weather, background sounds, and other particle effects**.

**VR-only effects** will render in VR (desktop or headset), but not in AR, since the real world environment should take precedence to provide terrain and sky:

- [Environment Presets](#environment--presets)
- [Water](#water)

**AR/VR (full XR)** effects are useful in any scene:

- [Weather and Particle Effects](#particle-effects)
- [Sounds](#sounds)

## Environment & Presets

ARENA provides the [aframe-environment-component](https://github.com/supermedium/aframe-environment-component) to render VR scene terrain by default, and it includes dozens of parameters. Some `preset` parameters are included as recipes, see the `forest` preset below.

<img src="/assets/img/overview/atmosphere/forest.png" width="50%"/>

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

Many of these parameters can be individually adjusted to your needs, see the [env-presets](/content/schemas/message/env-presets) section of our `scene-options` schema.

<img src="/assets/img/overview/atmosphere/mushroom.png" width="50%"/>

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

## Particle Effects

We include the [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component) to generate particle effects for weather, fire, fireworks, and more. Many of these effects from that component's examples are on display in our [particles demo scene](https://arenaxr.org/public/particles).

<img src="/assets/img/overview/atmosphere/particles.png" width="50%"/>

Some examples of rain, snow, dust, water, and ambient sounds can be experienced in our [weather demo scene](https://arenaxr.org/public/weather).

### Rain

This rain example is translated from the `rain` preset of [aframe-particle-system-component](https://github.com/IdeaSpaceVR/aframe-particle-system-component).

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

This snow example is translated from the `snow` preset of [aframe-particle-system-component](https://github.com/IdeaSpaceVR/aframe-particle-system-component).

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

This dust example is translated from the `dust` preset of [aframe-particle-system-component](https://github.com/IdeaSpaceVR/aframe-particle-system-component).

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

Multiple particle effects can be combined to create an effect like fire, as in this smoke, sparks, and flames example from our [classic render demo scene](https://arenaxr.org/public/render).

<img src="/assets/img/overview/atmosphere/render.png" width="50%"/>

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
  "object_id": "flames",
  "type": "object",
  "data": {
    "object_type": "entity",
    "spe-particles": {
      "texture": "static/images/textures/explosion_sheet.png",
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

## Water

We include the [aframe-extras](https://github.com/c-frame/aframe-extras) library, so you can make use of the `ocean` primitive to create water.

<img src="/assets/img/overview/atmosphere/ocean.png" width="50%"/>

```json
{
  "object_id": "ocean",
  "type": "object",
  "data": {
    "object_type": "ocean",
    "width": 100,
    "depth": 100,
    "color": "#7ad2f7",
    "rotation": { "w": -0.70711, "x": 0.70711, "y": 0, "z": 0 },
    "amplitude": 1,
    "opacity": 1
  }
}
```

## Sounds

The [a-frame sound component](https://aframe.io/docs/1.5.0/components/sound.html) is a great way to create an ambient sound atmosphere for your scene.

```json
{
  "object_id": "ambiance",
  "type": "object",
  "data": {
    "object_type": "entity",
    "sound": {
      "src": "store/users/wiselab/audio/ocean.mp3",
      "positional": false,
      "loop": true,
      "autoplay": true,
      "volume": 0.1
    }
  }
}
```
