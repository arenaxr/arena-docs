---
title: Function Definitions
nav_order: 5
layout: default
parent: Messaging Format
---

# Messaging Format Function Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

## Draw a Cube

Instantiate, persist a cube and set all it's basic parameters

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "create", "type": "object", "data": {"object_type": "cube", "position": {"x": 1, "y": 1, "z": -1}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}, "color": "#FF0000"}}'
```

## Color

change only the color of the already-drawn cube

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": {"material": {"color": "#00FF00"}}}'
```

## Transparency

Say the cube has already been drawn. In a second command, something like this sets 50% transparency:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": {"material": {"transparent": true, "opacity": 0.5}}}'
```

## Move

move the position of the already drawn cube

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": {"position": {"x": 2, "y": 2, "z": -1}}}'
```

## Rotate

rotate the already drawn cube; these are in quaternions, not A-Frame degrees

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": {"rotation": {"x": 60, "y": 2, "z": 3}}}'
```

the quaternion (native) representation of rotation is a bit more tricky. The 4 parameters are X, Y, Z, W. Here are some simple examples:

- `1, 0, 0, 0`: rotate 180 degrees around X axis
- `0, 0.7, 0, 0.7`: rotate 90 degrees around Y axis
- `0, 0, -0.7, 0.7`: rotate -90 degrees around Z axis

## Animate (rotation, position)

animate rotation of the already drawn cube

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": { "animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000}} }'
```

other animations are available that resemble the `"data": {"animation": { "property": ... }}` blob above: see [A-Frame Animation](https://aframe.io/docs/1.0.0/components/animation.html) documentation for more examples

## Remove

remove the cube

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "delete"}'
```

## Images

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/drone/image_floor -m '{"object_id": "image_floor", "action": "create", "data": {"object_type": "image", "position": {"x":0, "y": 0, "z": 0.4}, "rotation": {"x": -0.7, "y": 0, "z": 0, "w": 0.7}, "url": "images/floor.png", "scale": {"x":12, "y":12, "z": 2}, "material": {"repeat": {"x":4, "y":4}}}}'
```

URLs work in the URL parameter slot. Instead of `images/2.png` it would be e.g. `url(http://arena.andrew.cmu.edu/images/foo.jpg)`.
To update the image of a named image already in the scene, use this syntax:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/image_2 -m '{"object_id" : "image_2", "action": "update", "type": "object", "data": {"material": {"src": "https://arena.andrew.cmu.edu/abstract/downtown.png"}}}'
```

## Images on Objects (e.g.cube)

Use the `multisrc` A-Frame Component to specify different bitmaps for sides of a cube or other primitive shape, e.g:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/ -m '{"object_id":"die1", "action":"create", "type":"object", "persist":true, "data":{"object_type":"cube", "position":{"x":0, "y":0.5, "z":-2}, "rotation":{"x":0, "y":0, "z":0, "w":1}, "scale":{"x":1, "y":1, "z":1}, "color":"#ffffff", "dynamic-body":{"type":"dynamic"}, "multisrc":{"srcspath":"images/dice/", "srcs":"side1.png, side2.png, side3.png, side4.png, side5.png, side6.png"}}}'
```

## Other Primitives: TorusKnot

Instantiate a wacky torusKnot, then turn it blue. (look for other primitive types in A-Frame docs; here's a brief list: box circle cone cylinder dodecahedron icosahedron tetrahedron octahedron plane ring sphere torus torusKnot triangle)

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/torusKnot_1 -m '{"object_id" : "torusKnot_1", "action": "create", "data": {"object_type": "torusKnot", "color": "red", "position": {"x": 0, "y": 1, "z": -4}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}}}'

mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/torusKnot_1 -m '{"object_id" : "torusKnot_1", "action": "update", "type": "object", "data": {"material": {"color": "blue"}}}'
```

## Models

Instantiate a glTF v2.0 binary model (file extension .glb) from a URL.

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/gltf-model_1 -m '{"object_id" : "gltf-model_1", "action": "create", "data": {"object_type": "gltf-model", "url": "https://arena.andrew.cmu.edu/models/Duck.glb", "position": {"x": 0, "y": 1, "z": -4}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}}}'
```

## Animating GLTF Models

To animate a GLTF model (see above for how to find animation names), set the animation-mixer parameter, e.g:

```json
mosquitto_pub -t realm/s/northstar/gltf-model_3-animation -h arena.andrew.cmu.edu -m '{"object_id": "gltf-model_3", "action": "update", "type": "object", "data": {"animation-mixer": {"clip": "*"}}}'
```

The asterisk means play all animations, and works better in some situations, where other times the name of a specific animation in the GLTF file works (or maybe several in sequence).

## Relocalize Camera (Rig)

Move the camera rig (parent object of the camera) with ID camera_1234_er1k to a new coordinate (system). Values are x, y, z, (meters) x, y, z, w (quaternions)

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/ -m '{"object_id" : "camera_1234_er1k", "action": "update", "type": "rig", "data": {"position": {"x": 1, "y":1, "z":1}, "rotation": {"x": 0.1, "y":0, "z":0, "w":1} }}'
```

This assumes we know our camera ID was assigned as `1234`. One way to find out your camera ID is, automatically assigned ones get printed on web browsers' Developer Tools Console in a message like `my-camera name camera_1329_X`. That might not be easily knowable without snooping MQTT messages, so the `&fixedCamera=er1k` URL parameter lets us choose manually the unique ID. If used in the URL, the `&name=` parameter is ignored, and the derived camera/user ID is based on fixedCamera, so would be in this case `camera_er1k_er1k`

## Text

Add some red text that says "Hello World"

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/text_3 -m '{"object_id" : "text_3", "action": "create", "data": {"color": "red", "text": "Hello world!", "object_type": "text", "position": {"x": 0, "y": 3, "z": -4}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}}}'
```

Change text color properties [A-Frame Text](https://aframe.io/docs/0.9.0/components/text.html#properties)

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/text_3 -m '{"object_id" : "text_3", "action": "update", "type": "object", "data": {"text": {"color": "green"}}}'
```

## Lights

Persist a red light to the scene

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/light_3 -m '{"object_id" : "light_3", "action": "create", "data": {"object_type": "light", "position": {"x": 1, "y": 1, "z": 1}, "rotation": {"x": 0.25, "y": 0.25, "z": 0, "w": 1}, "color": "#FF0000"}}'
```

Default is ambient light. To change type, or other light [A-Frame Light](https://aframe.io/docs/0.9.0/components/light.html) parameters, example: change to directional. Options: ambient, directional, hemisphere, point, spot

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/light_3 -m '{"object_id" : "light_3", "action": "update", "type": "object", "data": {"light": {"type": "directional"}}}'
```

## Sound

Play toy piano sound from a URL when you click a cube. Sets click-listener Component, waveform URL, and sound attribute:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/piano/box_asharp -m '{"object_id" : "box_asharp", "action": "create", "data": {"object_type": "cube", "position": {"x": 2.5, "y": 0.25, "z": -5}, "scale": {"x": 0.8, "y":1, "z":1}, "color": "#000000", "sound": {"src": "url(https://arena.andrew.cmu.edu/audio/toypiano/Asharp1.wav)", "on": "mousedown"}, "click-listener": ""}}'
```

## 360 Video

Draw a sphere, set the texture src to be an equirectangular video, on the 'back' (inside):

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/waterfall/sphere_vid -m '{"object_id" : "sphere_vid", "action": "create", "type": "object", "data": {"object_type": "sphere", "scale": {"x": 200, "y": 200, "z": 200}, "rotation": {"x": 0, "y": 0.7, "z":0, "w": 0.7}, "color": "#808080", "material": {"src": "images/360falls.mp4", "side": "back"}}}'
```

## Lines

Draw a purple line from (2, 2, 2) to (3, 3, 3)

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/line_1 -m '{"object_id" : "line_1", "action": "create", "data": {"object_type": "line", "start": {"x": 2, "y": 2, "z": 2}, "end": {"x": 3, "y": 3, "z": 3}, "color": "#CE00FF"}}'
```

Extend the line with a new segment, colored green

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/line_1 -m '{"object_id" : "line_1", "action": "update", "type": "object", "data": {"line__2": {"start": {"x": 3, "y": 3, "z": 3}, "end": {"x": 4, "y": 4, "z": 4}, "color": "#00FF00"}}}'
```

## Thicklines

"thickline" (to improve openpose skeleton rendering visibility) - works like a line, but the lineWidth value specifies thickness, and multiple points can be specified at once, e.g. draw a pink line 11 pixels thick from 0, 0, 0 to 1, 0, 0 to 1, 1, 0 to 1, 1, 1. The shorthand syntax for coordinates is a bonus feature of lower level code; extending it for the rest of ARENA commands remains as an enhancement.

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/thickline_8 -m '{"object_id" : "thickline_8", "action": "create", "type": "object", "data": {"object_type": "thickline", "lineWidth": 11, "color": "#FF88EE", "path": "0 0 0, 1 0 0, 1 1 0, 1 1 1"}}'
```

You might be wondering, why can't normal lines just use the scale value to specify thickness? But this one goes to eleven! (really though, normal lines perform faster) To update a "thickline" takes a special syntax because thicklines are really "meshline"s:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/thickline_8 -m '{"object_id": "thickline_8", "action": "update", "type": "object", "data": {"meshline": {"lineWidth": 11, "color": "#FFFFFF", "path": "0 0 0, 0 0 1"}}}'
```

## Events

Add the "click-listener" event to a scene object; click-listener is a Component defined in `events.js`. This works for adding other, arbitrary Components. A non-empty message gets sent to the Component's `init:` function

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/cube_1 -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": {"click-listener": "enable"}}'
```

## Temporary Objects: ttl

It's desirable to have objects that don't last forever and pile up. For that there is the 'ttl' parameter that gives objects a lifetime, in seconds. Example usage for a sphere that disappears after 5 seconds (must also use `persist=true`):

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/pool/Ball2 -m '{"object_id": "Ball2", "action": "create", "ttl": 5, "persist": true, "data": {"position": {"x": -1, "y": 1, "z": -1}, "color": "blue", "object_type": "sphere"}}'
```

## Transparent Occlusion

To draw a shape that is transparent, but occludes other virtual objects behind it (to simulate virtual objects hidden by real world surfaces like a wall or table), include in the data section this JSON:

```json
{"material":{"colorWrite": false}, "render-order": "0"}
```

colorWrite is an attribute of the THREE.js Shader Material that, by exposing it, we make accessible like others belonging to the Material A-Frame Component, and is an alternative way of controlling visibility. render-order is a custom Component that controls which objects are drawn first (not necessarily the same as which are "in front of" others). All other ARENA objects are drawn with render-order of 1. Note: this does not occlude the far background A-Frame layer (like environment component stars) but in AR that layer is not drawn anyway.

## Background themes

Adds one of many predefined backgrounds ( one of: `[none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris]`) to the scene

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/env -m '{"object_id" : "env", "action": "update", "type": "object", "data": {"environment": {"preset": "arches"}}}'
```

## Physics

You can enable physics (gravity) for a scene object by adding the dynamic-body Component e.g for box_3:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/box_3 -m '{"object_id" : "box_3", "action": "update", "type": "object", "data": {"dynamic-body": {"type": "dynamic"}}}'
```

One physics feature is applying an impulse to an object to set it in motion. This happens in conjunction with an event. As an example, here are messages setting objects fallBox and fallBox2 to respond to mouseup and mousedown messages with an impulse with a certain force and position:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/fallBox2 '{"object_id": "fallBox2", "action": "create", "data": {"object_type": "cube", "dynamic-body": {"type": "dynamic"}, "impulse": {"on": "mousedown", "force": "1 50 1", "position": "1 1 1"}, "click-listener": "", "position": {"x":0.1, "y": 4.5, "z": -4}, "scale": {"x":0.5, "y":0.5, "z": 0.5}}}'

mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/fallBox '{"object_id": "fallBox", "action": "create", "data": {"object_type": "cube", "dynamic-body": {"type": "dynamic"}, "impulse": {"on": "mouseup", "force": "1 50 1", "position": "1 1 1"}, "click-listener": "", "position": {"x":0, "y": 4, "z": -4}, "scale": {"x":0.5, "y":0.5, "z": 0.5}}}'
```

## Parent/Child Linking

There's support to attach a child to an already-existing parent scene objects. When creating a child object, set the `"parent": "parent_object_id"` value in the JSON data. For example if parent object is gltf-model_Earth and child object is gltf-model_Moon, the commands would look like:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/earth/gltf-model_Earth -m '{"object_id": "gltf-model_Earth", "action": "create", "data": {"object_type": "gltf-model", "position": {"x":0, "y": 0.1, "z": 0}, "url": "models/Earth.glb", "scale": {"x": 5, "y": 5, "z": 5}}}'

mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/earth/gltf-model_Moon -m '{"object_id": "gltf-model_Moon", "action": "create", "data": {"parent": "gltf-model_Earth", "object_type": "gltf-model", "position": {"x":0, "y": 0.05, "z": 0.6}, "scale": {"x":0.05, "y": 0.05, "z": 0.05}, "url": "models/Moon.glb" }}'
```

Child objects inherit attributes of their parent, for example scale. Scale the parent, the child scales with it. If the parent is already scaled, the child scale will be reflected right away. Child position values are relative to the parent and also scaled.

## Special Components: load-scene and goto-url

In HTML form (which can also be specified inside the `data{}` portion of an MQTT message as attribute-value pairs) we have a couple special things

## load-scene

Loads the contents of another ARENA scene at a coordinate within the current scene (requires `click-listener`)
as MQTT

`attribute "load-scene" value "on: mousedown; url://arena.andrew.cmu.edu/drone; position: 0 0 0"`

as html

```html
<a-entity load-scene="on: mousedown; url://arena.andrew.cmu.edu/drone; position: 0 0 0" ...other stuff...></a-entity>
```

## goto-url

Navigates to entirely new page into browser when clicked, or other event (requires `click-listener`)
as MQTT

`attribute "goto-url" value "on: mousedown; url://arena.andrew.cmu.edu/drone;"`

as html

```html
<a-entity goto-url="on: mousedown; url://arena.andrew.cmu.edu/drone;"></a-entity>
```

## Particles

Particles are based on [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component), javascript loaded from [aframe-spe-particles-component.min.js](https://unpkg.com/aframe-spe-particles-component@^1.0.4/dist/aframe-spe-particles-component.min.js)
For now not directly supported, but rather by passing JSON inside the `data{}` element. The syntax for parameter names has been updated so instead of a name like this that is `space-separated` it becomes `spaceSeparated` (camel case). Three examples here have been created starting with the examples in [aframe-spe-particles-component examples](https://harlyq.github.io/aframe-spe-particles-component/) then reformulating to ARENA JSON syntax:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/smoke -m '{"object_id":"smoke", "action":"create", "data":{"object_type":"cube", "position":{"x":0, "y":1, "z":-3.9}, "rotation":{"x":0, "y":0, "z":0, "w":1}, "scale":{"x":0.01, "y":0.01, "z":0.01}, "color":"#ffffff", "spe-particles":{"texture":"textures/fog.png", "velocity":"1 30 0", "velocitySpread":"2 1 0.2", "particleCount":50, "maxAge":4, "size":"3, 8", "opacity":"0, 1, 0", "color":"#aaa, #222"}}}'

mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/flames -m '{"object_id":"flames", "action":"create", "data":{"object_type":"cube", "position":{"x":0, "y":1, "z":-3.8}, "rotation":{"x":0, "y":0, "z":0, "w":1}, "scale":{"x":0.01, "y":0.01, "z":0.01}, "color":"#ffffff", "spe-particles":{"texture":"textures/explosion_sheet.png", "textureFrames":"5 5", "velocity":"4 100 0", "acceleration":"0 10 0", "accelerationSpread":"0 10 0", "velocitySpread":"4 0 4", "particleCount":15, "maxAge":1, "size":"4, 8", "sizeSpread":2, "opacity":"1, 0", "wiggle":"0 1 0", "blending":"additive"}}}'

mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render/sparks -m '{"object_id":"sparks", "action":"create", "data":{"object_type":"cube", "position":{"x":0, "y":1, "z":-4}, "rotation":{"x":0, "y":0, "z":0, "w":1}, "scale":{"x":0.01, "y":0.01, "z":0.01}, "color":"#ffffff", "spe-particles":{"texture":"textures/square.png", "color":"yellow, red", "particleCount":3, "maxAge":0.5, "maxAgeSpread":1, "velocity":"40 200 40", "velocitySpread":"10 3 10", "wiggle":"50 0 50", "wiggleSpread":"15 0 15", "emitterScale":8, "sizeSpread":10, "randomizeVelocity":true}}}'
```

Particles are very complicated and take a lot of parameters. It would not make sense to translate all of them into explicit ARENA types, thus this flexible 'raw JSON' format is used.

## 3d Head Model

By default the ARENA shows your location as a 3d model of a head, with your nose at your location coordinates. If you want to change this, it is available in the scene addressable by an object_id based on your (camera) name, e.g `head-model_camera_1234_er1k` or if you set your name manually in the URL parameter `&fixedCamera=name` as `head-model_camera_name_name`. You can also change the text above your head, which defaults to the last part of your automatically assigned or fixedCamera name (after the underscore). So by default it would appear as `er1k` in the examples above, but can be modified by MQTT message addressed to object_id `head-text_camera_er1k_er1k`.

[//]: # (Much more now available in e.g. https://arena.andrew.cmu.edu/x/face/)

## Jitsi meet: share desktop window

[//]: # (Main documentation of Jitsi video conference integration with ARENA needs to be added, but can be found at https://arena.andrew.cmu.edu/x/jitsi/.)
What is documented here is how to share screens from web browser visit to Jitsi server on `https://mr.andrew.cmu.edu/<meeting room name>`.

- Jitsi Meet URL `https://mr.andrew.cmu.edu/arena-conference-<scenename>`
- Jitsi Meet screen share Settings->Profile->display name: `arena_screen_share_<unique id>`
- plane Object in scene: `arena_screen_share_<unique id>`

The plane object of course is up to creator to decide size, location, rotation, needs to be added as a persisted plane object

## Vive (laser) controls

We've noticed the controllers don't show up in the scene unless they both - and EVERYTHING else for SteamVR - are all working (headset, lighthouses). And sometimes you have to restart SteamVR for hand controllers to show up in the scene; even though SteamVR shows them as being working/on/available/etc., it's possible to open VR mode in an Arena scene and be missing the hand controls.

By default we use A-Frame 'laser-controls' which default to showing Valve Index controller 3D models (gray, circular), even if we are using (equivalent) Vive controllers (black, paddle shaped, not included in the list of controllers known to A-Frame)

## EVENTS

Click events are generated as part of the laser-controls A-Frame entity; you get the events if you click the lasers on scene entities that have click-listener Component in their HTML declaration (see index.html), or have later had click-listener enabled via an MQTT message (see above). Mouse events occur if you click in a browser, or tap on a touchscreen as well.

* mouseenter
* mouseleave
* mousedown
* mouseup
- triggerdown / triggerup for left and right hand controllers  
  The MQTT topic name for viewing these events can be the standard prefix (e.g. realm/s/render/) concatenated with a string made up of object ID that generated the event. An example event MQTT:

```json
realm/s/render/fallBox2 '{"object_id":"fallBox2", "action":"clientEvent", "type":"mousedown", "data":{"position":{"x":-0.993, "y":0.342, "z":-1.797}, "source":"camera_8715_er"}}'
```

Note the message itself will contain the originator of the event as a camera/"user" ID and other data like where the object was clicked (in world coordinates[?])

Full list of Vive controller event names:
  - triggerdown
  - triggerup
  - gripdown
  - gripup
  - menudown
  - menuup
  - systemdown
  - systemup
  - trackpaddown
  - trackpadup

Event listeners can be added directly in the hard coded index.html main Arena page, e.g:

```html
<a-entity vive-listener position="2 0.5 -4" id="ViveListenBox" name="Box2" obj-model="obj: #Cube-obj; mtl: #Cube-mtl"></a-entity>
```

or on demand from an MQTT message that enables click-listener when an object is created, or updated (see above)

- 6dof pose events are realtime events for movement of the Vive controls themselves in 3d space. These are kind of verbose in terms of MQTT messages, limited to 10 frames per second, much like the headset pose messages work. This supports the notion of tracking controller movement in real time, including direction (pose). These are enabled, much like the pose-listener Component (both defined in events.js) by adding the vive-pose-listener Component to a scene object directly, in the hard-coded index.html part of every Arena page e.g. 

```html
<a-entity vive-pose-listener vive-listener id="vive-leftHand" laser-controls="hand:left"></a-entity>
```

There is nothing coded yet in ARENA to fire events based on Vive control trigger presses in _other peoples viewers_ ... the events go to MQTT, and that's all. This is opposed to the way click events work, where all click events are first broadcast over MQTT, then those messages are received and interpreted by viewers, and turned into local, synthetic click events. The exception is that the laser-controls interface sends click events when the triggers are pressed, and click events ARE published to all scene subscribers. Handling of hand control pose information is for now limited to programs subscribing to MQTT.

## Scene (global) settings

Some settings are available by setting attributes of the Scene element (see [A-Frame Scene](https://aframe.io/docs/0.9.0/core/scene.html)) for example, turn on statistics:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render -m '{"object_id" : "scene", "action": "update", "type": "object", "data": {"stats": true}}'
```

customise the fog (notice 3 character hexadecimal color representation):

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render -m '{"object_id" : "scene", "action": "update", "type": "object", "data": {"fog": {"type": "linear", "color": "#F00"}}}'
```

remove the "enter VR" icon:

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/render -m '{"object_id" : "scene", "action": "update", "type": "object", "data": {"vr-mode-ui": {"enabled": false}}}'
```

other 'global' ARENA objects, by object_id:

- **groundPlane** an invisible 40x40m plane with physics set to 'static' that prevents objects from falling through the floor, and receives collision events
- **cameraRig** access to the translational part of camera rig object (to set data attributes beyond what rig update messages do)
- **cameraSpinner** access the part of the rig that does only rotation
- **weather** (if enabled) simple weather using particles for snow, rain, dust
- **sceneRoot** the root entity, parent of all objects
- **env** environments (see "A-Frame environments"): ground, trees, pillars, background, sky etc.
- **conix_box** a hard-coded box used for debugging
- **conix_text** a fixed text object used for debugging
- **myCamera** to attach HUD objects visible to everyone's camera
