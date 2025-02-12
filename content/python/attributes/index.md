---
title: Attributes
nav_order: 1.3
layout: default
has_children: true
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


## Additional Attributes (which are just specified as numbers or strings) may include persist, ttl, [clickable], etc:
```python
persist=True
ttl=30  # seconds
clickable=True
# click_listener=True works too
# etc.
```

# Generic Attribute
For attributes that are not specified by the library, you can use this (put anything you want in the "...")! Inherit from this class to create custom attributes.
```python
Attribute(...)
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

See [Animations and Morphs](../animations).

# More Attributes

The table of contents for the Python Attributes section includes links below to Python examples to create an manipulate all attribute types.
