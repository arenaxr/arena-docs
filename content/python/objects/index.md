---
title: Objects
nav_order: 1.2
layout: default
has_children: true
parent: Python Library
---

# Objects in arena-py

Objects are the main interface for placing content into the ARENA.

See [object definition reference](/content/schemas/definitions).

## Creating an Object and Adding Attributes
See Appendix for all types of Objects.

Attributes can be added upon `Object` creation in the three ways used below (special attributes like `position`, `rotation`, `scale`, `color`, etc. can be added with tuples, lists, or dictionaries).
```python
box = Box(
    object_id="my_box",
    position=Position(0,4,-2),
    rotation=(0,0,0,1),
    scale={"x":2,"y":2,"z":2}
)

# objects can be added to a scene with the add_object method
scene.add_object(box)
```

## Adding Attributes
```python
# use update_attributes with kwargs to add attributes
box.update_attributes(physics=Physics(type="dynamic"))

# shorthand way:
box.data.physics = Physics(type="dynamic")

# don't forget to call scene.update_object to see your chnages in the ARENA!
scene.update_object(box)
```

## Updating Attributes
Most attributes (except `object_id`, `persist`, `ttl`, and `parent`) are under the "data" field. Access these by using ```obj.data```.
```python
box.data.position.x = 2
# box.update_attributes(position=Position(2,4,-2)) works too
scene.update_object(box)
```

## Removing Object Attributes
```python
obj.data.click_listener = None # or, obj.data.clickable = None
# obj.update_attributes(click_listener=None) works too
```

## Update Handler
The update_handler will be called whenever the object is updated by the library of by some external program
```python
# [obj] is the Object that called the update handler
def update(obj):
    print(obj)

obj.update_handler = update
# obj.update_attributes(update_handler=update) works too
```

# Automatic Updates
arena-py will keep track of internal states of active objects in a scene, so the library user doesn't have to.
This means if you create an `Object` in a `Scene`, the `Scene` instance will listen to incoming messages and update
your `Object` instance's attributes automatically!

This allows arena-py programs to interact with the build page, with users, and even with other arena-py programs.
As long as your program is running, you do not need to manually keep track of your `Object`s' current state in the scene.

For instance, if you create an `Object` in arena-py and you update its position with the build page or with another program,
that `Object`'s position in the original arena-py program will automatically be updated for you!

# Generic Object
For objects that might not exist yet (but may exist in AFRAME). Inherit from this class to create custom objects.
```python
Object(object_type, ...)
```

# More Objects

The table of contents for the Python Objects section includes links below to Python examples to create an manipulate all object types.
