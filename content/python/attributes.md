---
title: Attributes
nav_order: 3
layout: default
parent: Python Library
---

# Attributes in ARENA-py

Attributes are used to specify parameters for ARENA Objects.

See [messaging](https://arena.conix.io/content/messaging/examples.html).

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

# Appendix
## Position
The position of an object can be specified by:
```python
position=Position(x, y, z)
# or
position=(x, y, z)
```

## Rotation
The rotation (in euler coordinates) of an object can be specified by:
```python
rotation=Rotation(x, y, z)
# or
rotation=(x, y, z)
```

The rotation (in quaternions) of an object can be specified by:
```python
rotation=Rotation(x, y, z, w) # note the additional "w" field
# or
rotation=(x, y, z, w)
```
{% include alert type="warning" title="Warning" content="All units for euler rotation are in **degrees** and quaternion rotation are in **radians**!" %}

## Scale
The scale of an object can be specified by:
```python
scale=Scale(x, y, z)
# or
scale=(x, y, z)
```

## Material
The color and transparency of an object can be set by:
```python
material=Material(color, transparent, opacity, ...)
```

## Color
The color of an object can be specified by:
```python
color=Color(red, green, blue)
# or
color=(red, green, blue)
```
{% include alert type="warning" title="Warning" content="As of version 0.1.8, color should be specified in Material!" %}

## Animation
See [Animations and Morphs](animations.md).

## Sound
A sound can be added to an object using:
```python
sound=Sound(positional, poolSize, autoplay, src, ...)
```

## GotoUrl
Goes to a url on click.
```python
goto_url=GotoUrl(dest, on, url)
```
{% include alert type="warning" title="Warning" content="click-listener must be True for this to work!" %}

## Impulse
An impulse can be added by:
```python
impulse=Impulse(on, force, position)
```

## Physics
Physics ("none", "static", or "dynamic") can be added with:
```python
physics=Physics(type)
```
or
```python
dynamic_body=Physics(type)
```

## Generic attribute
For attributes that are not specified by the library, you can use this (put anything you want in the "...")! Inherit from this class to create custom attributes.
```python
Attribute(...)
```

## Additional Attributes (which are just specified as numbers or strings) may include:
```python
persist=True
ttl=30  # seconds
clickable=True
# click_listener=True works too
# etc.
```
