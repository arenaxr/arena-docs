---
title: Objects
nav_order: 2
layout: default
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

# All Objects

## Box
Create a [box]:
```python
Box(...)
```

## Circle
Create a flat [circle]:
```python
Circle(...)
```

## Cone
Create a [cone]:
```python
Cone(...)
```

## Cylinder
Create a [cylinder]:
```python
Cylinder(...)
```

## Dodecahedron
Create a [dodecahedron]:
```python
Dodecahedron(...)
```

## GLTF
Create a [gltf] 3D model:
```python
GLTF(url, ...)
```

## Icosahedron
Create an [icosahedron]:
```python
Icosahedron(...)
```

## Image
Create a flat [image]:
```python
Image(url, ...)
```

## Light
Create a [light]:
```python
Light(...)
```

## Line
Create a thin [line]:
```python
Line(path, ...)
```

## Octahedron
Create an [octahedron]:
```python
Octahedron(...)
```

## Plane
Create a flat [plane]:
```python
Plane(...)
```

## Ring
Create a flat [ring]:
```python
Ring(...)
```

## Sphere
Create a [sphere]:
```python
Sphere(...)
```

## Tetrahedron
Create a [tetrahedron]:
```python
Tetrahedron(...)
```

## Text
Write 3D [text]:
```python
Text(...)
```

## ThickLine
Create a [thickline]:
```python
ThickLine(path, lineWidth, ...)
```

## Torus
Create a [torus]:
```python
Torus(...)
```

## TorusKnot
Create a [torusKnot]:
```python
TorusKnot(...)
```

## Triangle
Create a flat [triangle]:
```python
Triangle(...)
```

## Camera
[camera]
```python
Camera(object_id, ...)
```

## Card
Create an [arenaui-card]
```python
Card(...)
```

## ButtonPanel
Create an [arenaui-button-panel]
```python
ButtonPanel(buttons=[Button(...), ...], ...)
```

## Prompt
Create an [arenaui-prompt]
```python
Prompt(...)
```


## Generic Object
For objects that might not exist yet (but may exist in AFRAME). Inherit from this class to create custom objects.
```python
Object(object_type, ...)
```

[arenaui-button-panel]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[arenaui-card]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[arenaui-prompt]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[box]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/box.py
[camera]: https://github.com/arenaxr/arena-py/blob/master/examples/camera-print.py
[capsule]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/capsule.py
[circle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/circle.py
[cone]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cone.py
[cylinder]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cylinder.py
[dodecahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/dodecahedron.py
[entity]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/entity.py
[gltf]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/gltf.py
[hands]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/hands.py
[icosahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/icosahedron.py
[image]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/image.py
[light]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/light.py
[line]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/line.py
[ocean]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ocean.py
[octahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/octahedron.py
[parent]: https://github.com/arenaxr/arena-py/blob/master/examples/earth-moon.py
[pcd]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/pcd.py
[plane]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/plane.py
[ring]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ring.py
[roundedbox]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/roundedbox.py
[sphere]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/sphere.py
[splat]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/splat.py
[tetrahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/tetrahedron.py
[text]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/text.py
[thickline]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/thickline.py
[threejs]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/threejs_scene.py
[torus]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus.py
[torusKnot]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus_knot.py
[triangle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/triangle.py
[videosphere]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/videosphere.py
