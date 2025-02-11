---
title: Attributes
nav_order: 1.3
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
These attributes may be applied to any ARENA object.

## [Position](/content/python-api/attributes/position)
The [position] of an object can be specified by:
```python
position=Position(x, y, z)
# or
position=(x, y, z)
```

## [Rotation](/content/python-api/attributes/rotation)
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

## [Scale](/content/python-api/attributes/scale)
The [scale] of an object can be specified by:
```python
scale=Scale(x, y, z)
# or
scale=(x, y, z)
```

## [Animation](/content/python-api/attributes/animation)
An [animation] can be added to an object:

See [Animations and Morphs](animations.md).

## [AR Marker](/content/python-api/attributes/armarker)
Add a [armarker] attribute:
```python
armarker=Armarker(markerid, ...)
```

## [Attribution](/content/python-api/attributes/attribution)
Add a [attribution] attribute:
```python
attribution=Attribution(...)
```

## [Blip](/content/python-api/attributes/blip)
Add a [blip] attribute:
```python
blip=Blip(blipin, blipout, ...)
```

## [Box Collision](/content/python-api/attributes/box_collision_listener)
Add a [box-collision] attribute:
```python
box_collision_listener=BoxCollisionListener(dynamic, ...)
```

## [Goto Landmark](/content/python-api/attributes/goto_landmark)
Add a [goto-landmark] attribute:
```python
goto_landmark=GotoLandmark(landmark, on)
```

## [Goto Url](/content/python-api/attributes/goto_url)
Goes to a [goto-url] on click.
```python
goto_url=GotoUrl(dest, on, url)
```
{% include alert type="warning" title="Warning" content="click-listener must be True for this to work!" %}

## [Impulse](/content/python-api/attributes/impulse)
An [impulse] can be added by:
```python
impulse=Impulse(on, force, position)
```

## [Landmark](/content/python-api/attributes/landmark)
Add a [landmark] attribute:
```python
landmark=Landmark(label, ...)
```

## Look At
Make object [look-at] the camera:
```python
look_at="#my-camera"
```
or make object [look-at] at a position
```python
look_at="0 0 0"
```

## [Particles](/content/python-api/attributes/spe_particles)
Add a [spe-particles] effect:
```python
spe_particles=Particles(texture, color, velocity, ...)
```

## [Physics](/content/python-api/attributes/dynamic_body)
[dynamic-body] and [static-body] can be added with:
```python
physics=Physics(type, ...)
```
or
```python
dynamic_body=DynamicBody(type, ...)
```
or
```python
static_body=StaticBody(type, ...)
```

## [Shadow](/content/python-api/attributes/shadow)
Add a [shadow] attribute:
```python
shadow=Shadow(cast, receive)
```

## [Sound](/content/python-api/attributes/sound)
A [sound] can be added to an object using:
```python
sound=Sound(src, positional, poolSize, autoplay, ...)
```

## [Text Input](/content/python-api/attributes/textinput)
[textinput] can be added using a keyboard with:
```python
text_input=TextInput(on, title, label, placeholder)
```

# Primitive Geometry Mesh Only Attributes
These attributes may be applied only to primitive geometric mesh ARENA objects.

## [Color](/content/python-api/attributes/material)
The [color] of an object can be specified by:
```python
material=Material(color=Color(red, green, blue))
# or
material=Material(color=(red, green, blue))
```

## [Material](/content/python-api/attributes/material)
The [material] (transparency and color) of an object can be set by:
```python
material=Material(color, transparent, opacity, ...)
```

## [Jitsi Video](/content/python-api/attributes/jitsi_video)
Add a [jitsi-video] attribute:
```python
jitsi_video=JitsiVideo(displayName, ...)
```

## [Multi-Source](/content/python-api/attributes/multisrc)
Add a [multisrc] attribute:
```python
multisrc=Multisrc(srcs, srcspath)
```

## [Video Control](/content/python-api/attributes/video_control)
Add a [video-control] attribute:
```python
video_control=VideoControl(video_path, video_object, autoplay, ...)
```

# Model Only Attributes
These attributes may be applied only to model ARENA objects like GLTF, PCD, Three Scene, Gaussian Splat.

## [Animation Mixer](/content/python-api/attributes/animation_mixer)
An [animation-mixer] can be added to an object:

See [Animations and Morphs](animations).

## [GLTF Load On Demand (LOD)](/content/python-api/attributes/gltf_model_lod)
Add a [gltf-lod] attribute:
```python
gltf_model_lod=GltfModelLod(detailedUrl, detailedDistance, ...)
```

## [GLTF Model Update](/content/python-api/attributes/model_update)
Add a [model-update] attribute:
```python
modelUpdate={"mixamorigLeftShoulder": {...}}
```

## [GLTF Morph](/content/python-api/attributes/gltf_morph)
Add a [gltf-morph] attribute:

See [Animations and Morphs](animations).

## [Material Extras](/content/python-api/attributes/material_extras)
Add a [material-ext] attribute:
```python
material_extras=MaterialExtras(encoding, transparentOccluder, gltfOpacity, ...)
```

# Generic Attribute
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

[animation-mixer]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation_mixer.py
[animation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation.py
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
[model-update]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/modelUpdate.py
[multisrc]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/multisrc.py
[parent]: https://github.com/arenaxr/arena-py/blob/master/examples/simple/earth-moon.py
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
