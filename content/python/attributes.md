---
title: Attributes
nav_order: 3
layout: default
parent: Python Library
---

# Attributes in arena-py

Attributes are used to specify parameters for ARENA Objects.

See [object definition reference](/content/schemas/definitions).

## Accessing Object Attributes
See Appendix for all types of Attributes.

Usually, attributes (except for `object_id`, `persist`, `ttl`, and `parent`) are under the `data` field:
```python
obj.object_id
obj.persist
...
obj.data.position
obj.data.rotation
...
obj.data.material
# etc etc
```

# All Attributes
## Position
The [position] of an object can be specified by:
```python
position=Position(x, y, z)
# or
position=(x, y, z)
```

## Rotation
The [rotation] (in euler coordinates) of an object can be specified by:
```python
rotation=Rotation(x, y, z)
# or
rotation=(x, y, z)
```

The [rotation] (in quaternions) of an object can be specified by:
```python
rotation=Rotation(x, y, z, w) # note the additional "w" field
# or
rotation=(x, y, z, w)
```
{% include alert type="warning" title="Warning" content="All units for euler rotation are in **degrees** and quaternion rotation are in **radians**!" %}

## Scale
The [scale] of an object can be specified by:
```python
scale=Scale(x, y, z)
# or
scale=(x, y, z)
```

## Color
The [color] of an object can be specified by:
```python
material=Material(color=Color(red, green, blue))
# or
material=Material(color=(red, green, blue))
```

## Material
The [material] (transparency and color) of an object can be set by:
```python
material=Material(color, transparent, opacity, ...)
```

## Animation
An [animation] and/or an [animation-mixer] can be added to an object:

See [Animations and Morphs](animations.md).

## Sound
A [sound] can be added to an object using:
```python
sound=Sound(positional, poolSize, autoplay, src, ...)
```

## GotoUrl
Goes to a [goto-url] on click.
```python
goto_url=GotoUrl(dest, on, url)
```
{% include alert type="warning" title="Warning" content="click-listener must be True for this to work!" %}

## Impulse
An [impulse] can be added by:
```python
impulse=Impulse(on, force, position)
```

## Physics
[dynamic-body] and [static-body] ("none", "static", or "dynamic") can be added with:
```python
physics=Physics(type)
```
or
```python
dynamic_body=Physics(type)
```

## Text Input
[textinput] can be added using a keyboard with:
```python
text_input=TextInput(on, title, label, placeholder)
```

## Particle
Add a [spe-particles] effect:
```python
Particle(...)
```

## Generic attribute
For attributes that are not specified by the library, you can use this (put anything you want in the "...")! Inherit from this class to create custom attributes.
```python
Attribute(...)
```

## Additional Attributes (which are just specified as numbers or strings) may include persist, ttl, [clickable], etc:
```python
persist=True
ttl=30  # seconds
clickable=True
# click_listener=True works too
# etc.
```

[animation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation.py
[animation-mixer]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation_mixer.py
[armarker]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/armarker.py
[attribution]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/attribution.py
[blip]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/blip.py
[box-collision]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/box_collision.py
[clickable]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/clickable.py
[collision]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/collision.py
[color]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/color.py
[dynamic-body]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[gltf-lod]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/model_lod.py
[gltf-morph]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/morph.py
[goto-landmark]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_landmark.py
[goto-url]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_url.py
[impulse]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[jitsi-video]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/jitsi_video.py
[landmark]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/landmark.py
[look-at]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/look_at.py
[material-ext]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/material_extras.py
[material]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/material.py
[modelUpdate]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/modelUpdate.py
[multisrc]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/multisrc.py
[parent]: https://github.com/arenaxr/arena-py/blob/master/examples/earth-moon.py
[position]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/position.py
[rotation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/rotation.py
[scale]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/scale.py
[screenshare]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/screenshare.py
[shadow]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/shadow.py
[sound]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/sound.py
[spe-particles]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/particles.py
[static-body]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[textinput]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/text_input.py
[video-control]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/video_control.py
