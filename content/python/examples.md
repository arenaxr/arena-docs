---
title: Examples
nav_order: 2
layout: default
parent: Python Library
---

# Python Examples

- [**ARENA-py**](https://github.com/conix-center/ARENA-py) Python repository

{% include alert type="warning" title="Coming Soon" content="Writing in progress..." %}

## Viewer

For all these standalone examples, open your browser first at this address: [https://arena.andrew.cmu.edu/?scene=example](https://arena.andrew.cmu.edu/?scene=example)

Use this template for all of these examples, import arena, init, handle events.

## Python Structure

```python
import arena
# [Callback functions may go before/after arena.init()]
arena.init("arena.andrew.cmu.edu", "realm", "example")
# [All other arena.py functions must be call after arena.init()]
arena.handle_events()
```

## Debug Messages

```python
arena.debug()
```

## Add Subtopic

```python
def secondary_callback(msg):
    print(msg.payload)

arena.add_topic("$SYS/#", secondary_callback)
```

## Remove Subtopic

```python
arena.remove_topic("$SYS/#")
```

## Object Names

```python

```

## Objects with no names

```python

```

## Observe name collisions

```python

```

## Draw a Cube

Instantiate a cube and set all of it's basic parameters.

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
cube = arena.Object(objType=arena.Shape.cube)
arena.handle_events()
```

## Colors, 3 kinds!

Change only the color of the already-drawn cube.

```python
cube.update(color=(0, 255, 0))
cube.update(data='{"color":"#00ff00"}')
cube.update(data='{"color":"green"}')
```

## Transparency

Say the cube has already been drawn. In a second command, this sets 50% transparency.

```python
cube.update(transparency=arena.Transparency(True, 0.5))
```

## Move

Move the position of the already drawn cube.

```python
cube.update(location=(2, 2, -1))
```

## Rotate

Rotate the already drawn cube; these are in quaternions, not A-Frame degrees.

```python
cube.update(rotation=(0.4, 0.4, 0.4, 0.4))
```

The quaternion (native) representation of rotation is a bit more tricky. The 4 parameters are X, Y, Z, W. Here are some simple examples:

- `1, 0, 0, 0`: rotate 180 degrees around X axis
- `0, 0.7, 0, 0.7`: rotate 90 degrees around Y axis
- `0, 0, -0.7, 0.7`: rotate -90 degrees around Z axis

## Animate

Animate rotation of the already drawn cube.

```python
cube.update(data='{"animation": {"property":"rotation", "to":"0 360 0", "loop":"true", "dur":10000}}')
```

Other animations are available that resemble the `"data": {"animation": { "property": ... }}` blob above: see [A-Frame Animation](https://aframe.io/docs/1.0.0/components/animation.html) documentation for more examples.

## Remove

Remove the cube.

```python
cube.delete()
```

## Images

Create an image on the floor.

```python
floor = arena.Object(
    objName="my_image_floor",
    objType=arena.Shape.image,
    location=(0, 0, 0.4),
    rotation=(-0.7, 0, 0, 0.7),
    scale=(12, 12, 12),
    data='{"url": "images/floor.png", "material": {"repeat": {"x":4, "y":4}}}',
)
```

URLs work in the URL parameter slot. Instead of `images/2.png` it would be e.g. `url(http://arena.andrew.cmu.edu/images/foo.jpg)`.
To update the image of a named image already in the scene, use this syntax.

```python
floor.update(
    data='{"material": {"src": "https://arena.andrew.cmu.edu/abstract/downtown.png"}}'
)
```

## Images on Objects (e.g. cube)

Use the `multisrc` A-Frame Component to specify different bitmaps for sides of a cube or other primitive shape.

```python
# TODO
```

## Other Primitives: TorusKnot

Instantiate a wacky torusKnot, then turn it blue. Other primitive types are available in the in [A-Frame docs](https://aframe.io/docs/1.0.0/components/geometry.html#built-in-geometries). Here is a brief list: **box circle cone cylinder dodecahedron icosahedron tetrahedron octahedron plane ring sphere torus torusKnot triangle**.

```python
# TODO
```

## Models

Instantiate a glTF v2.0 binary model (file extension .glb) from a URL.

```python
duck = arena.Object(
    objName="model1",
    objType=arena.Shape.gltf_model,
    location=(0, 0, -4),
    url="models/Duck.glb",
)
```

## Animating GLTF Models

To animate a GLTF model (see [GLTF Files](../3d-content/gltf-files) for how to find animation names), and set the animation-mixer parameter.

```python
cow = arena.Object(
    objName="model2",
    objType=arena.Shape.gltf_model,
    location=(-21, 1.8, -8),
    scale=(0.02, 0.02, 0.02),
    url="models/cow2/scene.gltf",
)
cow.update(data='{"animation-mixer": {"clip": "*"}}')
```

The asterisk means "play all animations", and works better in some situations, where other times the name of a specific animation in the GLTF file works (or maybe several in sequence).

## Relocalize Camera Rig

Move the camera rig (parent object of the camera) with ID camera_1234_er1k to a new coordinate (system). Values are x, y, z, (meters) x, y, z, w (quaternions).

```python
# (dangerous) technique to update everyone's camera rig without knowing name
rig = arena.Object(objName="cameraRig")
rig.update(location=(1, 1, 1))
```

This assumes we know our camera ID was assigned as `1234`. One way to find out your camera ID is, automatically assigned ones get printed on web browsers' Developer Tools Console in a message like `my-camera name camera_1329_X`. That might not be easily knowable without snooping MQTT messages, so the `&fixedCamera=er1k` URL parameter lets us choose manually the unique ID. If used in the URL, the `&name=` parameter is ignored, and the derived camera/user ID is based on fixedCamera, so would be in this case `camera_er1k_er1k`

## Text

Add some red text that says "Hello World".

```python
text = arena.Object(
    objName="text_3",
    objType=arena.Shape.text,
    color=(255, 0, 0),
    location=(0, 3, -4),
    text="Hello world!",
)
```

Change text color properties [A-Frame Text](https://aframe.io/docs/0.9.0/components/text.html#properties).

```python
text.update(color=(0, 255, 0))
```

## Lights

Create a red light in the scene.

```python
light = arena.Object(
    objName="myLight",
    objType=arena.Shape.light,
    location=(1, 1, 1),
    rotation=(0.25, 0.25, 0.25, 1),
    color=(255, 0, 0),
)
```

Default is ambient light. To change type, or other light [A-Frame Light](https://aframe.io/docs/0.9.0/components/light.html) parameters, example: change to **directional**. Options: **ambient, directional, hemisphere, point, spot**.

```python
# TODO
```

## Sound

Play toy piano sound from a URL when you click a cube. Sets click-listener Component, waveform URL, and sound attribute.

```python
# TODO
```

## 360 Video

Draw a sphere, set the texture src to be an equirectangular video, on the 'back' (inside).

```python
# TODO
```

## Lines

Draw a purple line from (2, 2, 2) to (3, 3, 3).

```python
arena.Object(
    objName="line1",
    objType=arena.Shape.line,
    line=arena.Line(start=(3, 2, -4), end=(3, 3, -4), color=(206, 0, 255)),
)
```

Extend the line with a new segment, colored green.

```python
# TODO
```

## Thicklines

A "thickline" (to improve openpose skeleton rendering visibility) - works like a line, but the `lineWidth` value specifies thickness, and multiple points can be specified at once, e.g. draw a pink line 11 pixels thick from 0, 0, 0 to 1, 0, 0 to 1, 1, 0 to 1, 1, 1. The shorthand syntax for coordinates is a bonus feature of lower level code; extending it for the rest of ARENA commands remains as an enhancement.

```python
arena.Object(
    objName="line2",
    objType=arena.Shape.thickline,
    thickline=arena.Thickline(line_width=11, color=(255, 136, 238), path=[
        (3, 4, -4), (4, 4, -4), (4, 5, -4), (4, 5, -5)]),
)
```

You might be wondering, why can't normal lines just use the scale value to specify thickness? But this one goes to eleven! Really though, normal lines perform faster. To update a "thickline" takes a special syntax because thicklines are really "meshline"s.

```python
# TODO
```

## Events

Add the "click-listener" event to a scene object; click-listener is a Component defined in `events.js`. This works for adding other, arbitrary Components. A non-empty message gets sent to the Component's `init:` function.

```python
# TODO
```

## Persisted Objects

If we want our objects to return to the scene when we next open or reload our browser, we can commit them on creation to the ARENA Persistance DB by setting `"persist": true`.

```python
# TODO
```

## Temporary Objects: TTL

It's desirable to have objects that don't last forever and pile up. For that there is the 'ttl' parameter that gives objects a lifetime, in seconds. This is an example usage for a sphere that disappears after 5 seconds.

```python
# TODO
```

## Transparent Occlusion

To draw a shape that is transparent, but occludes other virtual objects behind it (to simulate virtual objects hidden by real world surfaces like a wall or table), include in the data section this JSON.

```python
# TODO
```

`colorWrite` is an attribute of the THREE.js Shader Material that, by exposing it, we make accessible like others belonging to the Material A-Frame Component, and is an alternative way of controlling visibility. `render-order` is a custom Component that controls which objects are drawn first (not necessarily the same as which are "in front of" others). All other ARENA objects are drawn with render-order of 1. 

{% include alert type="note" title="Note" content="
This does not occlude the far background A-Frame layer (like environment component stars) but, in AR, that layer is not drawn anyway.
" %}

## Background Themes

Adds one of many predefined backgrounds ( one of: **none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris**) to the scene

```python
# TODO
```

## Physics

You can enable physics (gravity) for a scene object by adding the dynamic-body Component.

```python
torus = arena.Object(
    objName="", objType=arena.Shape.torusKnot, color=(255, 0, 0), location=(0, 3, -6)
)
torus.update(color=(0, 0, 255))
torus.update(physics=arena.Physics.dynamic)
torus.update(ttl=2)
```

One physics feature is applying an impulse to an object to set it in motion. This happens in conjunction with an event. As an example, here are messages setting objects fallBox and fallBox2 to respond to `mouseup` and `mousedown` messages with an impulse with a certain force and position.

```python
# TODO
```

## Parent/Child Linking

There is support to attach a child to an already-existing parent scene objects. When creating a child object, set the `"parent": "parent_object_id"` value in the JSON data. For example if parent object is gltf-model_Earth and child object is gltf-model_Moon, the commands would look like:

```python
# TODO
```

Child objects inherit attributes of their parent, for example scale. Scale the parent, the child scales with it. If the parent is already scaled, the child scale will be reflected right away. Child position values are relative to the parent and also scaled.

## Goto URL

Navigates to entirely new page into browser when clicked, or other event (requires `click-listener`).

```python
newtab = arena.Object(
    objType=arena.Shape.cube,
    location=( 0, 0, -5),
    color=(0,255,0),
    clickable=True,
    data='{"goto-url": { "dest":"newtab", "on": "mousedown", "url": "http:www.eet.com"} } ',
)
```

## Particles

Particles are based on [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component), javascript loaded from [aframe-spe-particles-component.min.js](https://unpkg.com/aframe-spe-particles-component@^1.0.4/dist/aframe-spe-particles-component.min.js).

For now, its not directly supported, but rather by passing JSON inside the `data{}` element. The syntax for parameter names has been updated so instead of a name like this that is `space-separated` it becomes `spaceSeparated` (camel case). Three examples here have been created starting with the examples in [aframe-spe-particles-component examples](https://harlyq.github.io/aframe-spe-particles-component/) then reformulating to ARENA JSON syntax.

```python
# TODO
```

Particles are very complicated and take a lot of parameters. It would not make sense to translate all of them into explicit ARENA types, thus this flexible 'raw JSON' format is used.

## Events

Click events are generated as part of the laser-controls A-Frame entity; you get the events if you click the lasers on scene entities that have click-listener Component in their HTML declaration (see index.html), or have later had click-listener enabled via an MQTT message (see above). Mouse events occur if you click in a browser, or tap on a touchscreen as well.

* `mouseenter`
* `mouseleave`
* `mousedown`
* `mouseup`
- `triggerdown` / `triggerup` for left and right hand controllers  

The MQTT topic name for viewing these events can be the standard prefix (e.g. realm/s/example/) concatenated with a string made up of object ID that generated the event. An example event MQTT:

```python
import arena

def cube_callback(msg):
    print("cube_callback: ", msg)

arena.init("arena.andrew.cmu.edu", "realm", "example")
cube = arena.Object(objType=arena.Shape.cube, clickable=True, cube_callback)
arena.handle_events()
```

{% include alert type="note" title="Note" content="
The message itself will contain the originator of the event as a camera/user ID and other data like where the object was clicked.
" %}

Full list of Vive controller event names:
  - `triggerdown`
  - `triggerup`
  - `gripdown`
  - `gripup`
  - `menudown`
  - `menuup`
  - `systemdown`
  - `systemup`
  - `trackpaddown`
  - `trackpadup`
