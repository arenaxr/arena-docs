---
title: Objects
nav_order: 2
layout: default
parent: Python Library
---

# Objects in ARENA-py

Objects are the main interface for placing content into the ARENA.

See [messaging](https://arena.conix.io/content/messaging/examples.html).

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
obj.data.click_listener = None
# obj.update_attributes(click_listener=None) works too
```

## Update Handler
The update_handler will be called whenever the object is updated by the library of by some external program
```python
def update(obj):
    print(obj)

obj.update_handler = update
# obj.update_attributes(update_handler=update) works too
```

# Automatic Updates
ARENA-py will keep track of internal states of active objects in a scene, so the library user doesn't have to.
This means if you create an Object in a Scene, the Scene instance will listen to incoming messages and update
your Object instance's attributes automatically!

This allows ARENA-py programs to interact with the build page, with users, and even with other ARENA-py programs.
As long as your program is running, you do not need to manually keep track of your Objects' current state in the scene.

For instance, if you create an Object in ARENA-py and you update its position with the build page or with another program,
that Object's position in the original ARENA-py program will automatically be updated for you!

# Appendix

## Box
```python
Box(...)
```

## Sphere
```python
Sphere(...)
```

## Circle
```python
Circle(...)
```

## Cone
```python
Cone(...)
```

## Cylinder
```python
Cylinder(...)
```

## Dodecahedron
```python
Dodecahedron(...)
```

## Icosahedron
```python
Icosahedron(...)
```

## Tetrahedron
```python
Tetrahedron(...)
```

## Octahedron
```python
Octahedron(...)
```

## Plane
```python
Plane(...)
```

## Ring
```python
Ring(...)
```

## Torus
```python
Torus(...)
```

## Triangle
```python
Triangle(...)
```

## GLTF
```python
GLTF(url, ...)
```

## Image
```python
Image(url, ...)
```

## Particle
```python
Particle(...)
```

## Text
```python
Text(...)
```

## Light
```python
Light(...)
```

## Line
```python
Line(start, end, ...)
```

## ThickLine
```python
ThickLine(path, lineWidth, ...)
```

## Camera
```python
Camera(object_id, ...)
```

## Generic Object
For objects that might not exist yet. Inherit from this class to create custom objects.
```python
Object(object_type, ...)
```

## ARENA Object JSON example
```json
{
    "object_id": "my_box",
    "type": "object",
    "persist": false,
    "data": {
        "object_type": "box",
        "position": {
            "x": 0,
            "y": 4,
            "z": -2
        },
        "scale": {
            "x": 2,
            "y": 2,
            "z": 2
        },
        # more attributes here
    },
    "timestamp" : "[time goes here]"
}
```
