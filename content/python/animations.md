---
title: Animations and Morphs
nav_order: 7
layout: default
parent: Python Library
---

# Animations and GLTF Morphs in ARENA-py

Dispatching and running animations and GLTF 3D Morphs.

##  Animations

### Dispatching Animations
You can add animations to objects that will run when `scene.run_animations(...)` is called:
```python
obj = Box()
obj.dispatch_animation(
        Animation(
            property="rotation",
            start=(0,0,0),
            end=(0,180,0),
            easing="linear",
            dur=1000
        )
    )
scene.run_animations(obj) # this will cause the animation to be run
```
You can also dispatch multiple `Animation`s:
```python
obj = Box()
obj.dispatch_animation(
        [
            Animation(
                property="rotation",
                start=(0,0,0),
                end=(0,180,0),
                easing="linear",
                dur=1000
            ),
            Animation(
                property="position",
                start=(0,0,-5),
                end=(0,0,-10),
                easing="linear",
                dur=1000
            )
        ]
    )
scene.run_animations(obj) # this will cause all the dispatched animations to be run
```

### Animation vs AnimationMixer
`AnimationMixer`s are special animations specific to a 3D model. These can be run the same way as regular `Animation`s.
See [here](https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation).
```python
xr_logo.dispatch_animation(
    AnimationMixer(clip="*", loop="repeat")
)
scene.run_animations(xr_logo) # this will cause the 3D model to play its animations
```

### Permanent Animations
Sometimes you want `Animation`s to be associated with the object. You can do this by adding the `Animation` as an `Attribute` to the `Object`:
```python
# this makes it such that xr_logo will ALWAYS play the animation when someone joins
# your ARENA scene, since the animation is now associated with that object:
xr_logo.update_attributes(
    animation_mixer=AnimationMixer(
            clip="*", loop="repeat"
        )
)
```

## GLTF Morphs

### Morph and update_morph
GLTF morphs can be created with the `Morph` class, and can be added to an object with the `update_morph` method:
```python
# create list of Morphs
open_eye_morph = [Morph(morphtarget="eyeTop",value=0.0), Morph(morphtarget="eyeBottom",value=0.0)]

xr_logo.update_morph(open_eye_morph) # accepts Morphs and lists of Morph
```
