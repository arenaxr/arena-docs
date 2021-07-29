---
title: JSON Spec
nav_order: 3
layout: default
parent: Messaging Format
---

## ARENA MQTT Message Payload JSON Specification
Each ARENA message is JSON formatted and is structured for its general use and persistence within the ARENA environment. Each message begins with a [`Scene Message object`](#scene-message-object) of general properties, paired with a more granular detailed `data` sub-object which varies in form and follow the examples below.
- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

{% include alert type="tip" title="Tip" content="
In most cases arbitrary A-Frame properties which are applied in HTML as attributes can be submitted as JSON below.
"%}

## Examples

### Object Message
[`Scene Message object`](#scene-message-object) with a `data` property of the [`Object Data` object](#object-data-object).
```json
{"object_id": "cube_1", "action": "create", "type": "object", "data": {"object_type": "cube", "position": {"x": 1, "y": 1, "z": -1}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}, "color": "#FF0000"}}
```

### Event Message
[`Scene Message object`](#scene-message-object) with a `data` property of the [`Event Data` object](#event-data-object).
```json
{"object_id": "fallBox2", "action": "clientEvent", "type": "mousedown", "data": {"position": {"x": -0.993, "y": 0.342, "z": -1.797}, "source": "camera_8715_er"}}
```

### Program Message
[`Scene Message object`](#scene-message-object) with a `data` property of the [`Program Data` object](#program-data-object).
```json
{"object_id": "6aafedf3-e313-4785-a456-939de8677f07", "action": "update", "persist": true, "type": "program", "data": {"name": "wiselab/arb", "instantiate": "single", "filename": "arb.py", "filetype": "PY", "args": ["${scene}", "-b", " ${mqtth}"]}}
```

### Scene Options Message
[`Scene Message object`](#scene-message-object) with a `data` property of the [`Scene Options Data` object](#scene-options-data-object).
```json
{"object_id": "e9a16478-2606-4cd0-bb9f-b03879bc8baa", "action": "update", "persist": true, "type": "scene-options", "data": {"env-presets": {"active": true, "lighting": "distant", "lightPosition": {"x": 0, "y": 1, "z": -10}, "ground": "hills", "groundTexture": "squares", "groundColor": "#444241", "groundYScale": 0.5}, "scene-options": {"jitsiServer": "jitsi1.andrew.cmu.edu", "clickableOnlyEvents": true, "privateScene": true}}}
```

-------------------------

## How to Read These Tables

- **property** JSON name of the property, also a [link to an example](#object-message) if available.
-  **support**  *Support libraries:*<br/> **A**: ARENA-Managed property<br/> **H**: Arbitrary A-Frame HTML property<br/> **P**: Python library property
-  **type** JSON property type: `string, number, boolean,` or another [`named object type` with a link](#scene-message-object).
- **description** JSON property description. (Any *default settings for the property*, or **if the property is required**.)

-------------------------

## "Scene Message" object
This is the main payload body of every MQTT scene topic in the ARENA.

### properties

|property|support|type|description
|---|---|---|---
| object_id | *A/P* | `string` | A unique name within the scene (**required**).
| action | *A/P* | `string` | An action to perform: `create, delete, update, clientEvent` (**required**).
| type | *A/P* | `string` | Message type: `object, program, scene-options, rig, camera-override, mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup`.
| [persist](examples#persisted-objects) | *A/P* | `boolean` | Save to persistence database (*default: false*).
| [ttl](examples#temporary-objects-ttl) | *A/P* | `number` | Time-to-live seconds to create the object and automatically delete (*default: 0*).
| data | *A/P* | [`Object Data` object](#object-data-object) | The detailed properties of a 3d object in the scene. Used by Message Type `object`.
| data | *A/P* | [`Event Data` object](#event-data-object) | The detailed properties of an event in the scene. Used by Event Type `mousedown (and others)`, Action: `clientEvent`.
| data | *A* | [`Program Data` object](#program-data-object) | The detailed properties of a program managed by the [runtime manager](../arts) in the scene. Used by Message Type `program`.
| data | *A* | [`Scene Options Data` object](#scene-options-data-object) | The detailed properties of the scene environment. Used by Message Type `scene-options`.

-------------------------

## Actions

The `create`, `update`, and `delete` actions are similar to typical C\(R\)UD operations.

- `create` - *Upserts* an object. If the object already does exist, `data` fields will be *merged*.
- `update` - Merges the `data` attributes with a currently existing object. To **remove** an attribute, set the value
             to `null`.
- `delete` - Delete an object. No data field required.

-------------------------
## "Object Data" object

{% include alert type="warning" title="Arbitrary A-Frame Components" content="
Some A-Frame attributes and components we don't officially include in our JSON may be usable by following certain [patterns of use](../developer/aframe). We make no promises!
"%}

### properties

|property|support|type|description
|---|---|---|---
| object_type | *A/P* | `string` | A primitive object type: `cube, sphere, circle, cone, cylinder, dodecahedron, icosahedron, tetrahedron, octahedron, plane, ring, torus, torusKnot, triangle`
| | *A/P* | | ...or, A complex object type: `gltf_model, image, particle, text, line, light, thickline`
| | *A* | | ...or, A presence object type : `camera, viveLeft, viveRight` (`camera` is used by web browsers and VIO cameras)
| [position](examples#move) | *A/P* | [`Position` object](#position-object) | Position of the object's origin in 3d, relative to world-origin.
| [rotation](examples#rotate) | *A/P* | [`Rotation` object](#rotation-object) | Quaternion rotation of the object.
| scale | *A/P* | [`scale` object](#scale-object) | Scale factor of the object in 3d.
| [color](examples#color) | *A/P* | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| [text](examples#text) | *A/P* | `string` | Any `string` of [ASCII characters](https://aframe.io/docs/1.0.0/components/text.html#non-ascii-characters). e.g. "Hello world!"
| [click-listener](examples#events) | *A/P* | `string` | Name of the click-listener, default can be empty string. e.g. ""
| [url](examples#images) | *A/P* | `string` | URI, relative or full path of a file. e.g. "store/models/Duck.glb"
| [material](examples#360-video) | *A/P* | [`Material` object](#material-object) | The material properties of the object's surface.
| [multisrc](examples#images-on-objects) | *A* | [`Multisrc` object](#multisrc-object) | Define multiple visual sources applied to an object.
| [light](examples#lights) | *A* | [`Light` object](#light-object) | Properties of a light source. Used by `object_type`: `light`.
| [animation](examples#animate) | *A* | [`Animation` object](#animation-object) | Animation rules of an object.
| [animation-mixer](examples#animating-gltf-models) | *A/P* | [`Animation-Mixer` object](#animation-mixer-object) | Animation sequence rules.
| [start](examples#lines) | *A/P* | [`Position` object](#position-object) | Starting position of a line. Used by `object_type`: `line`.
| [end](examples#lines) | *A/P* | [`Position` object](#position-object) | Ending position of a line. Used by `object_type`: `line`.
| [meshline](examples#thicklines) | *A/P* | [`Meshline` object](#meshline-object) | A line type with multiple way-points. Used by `object_type`: `thickline`.
| [sound](examples#sound) | *A* | [`Sound` object](#sound-object) | The sound properties of an object. Requires `click-listener`
| [dynamic-body](examples#physics) | *A/P* | [`Dynamic-Body` object](#dynamic-body-object) | The physics rules an object should obey.
| [impulse](examples#physics) | *A/P* | [`Impulse` object](#impulse-object) | The force applied using physics. Requires `click-listener`
| [spe-particles](examples#particles) | *A* | [`SPE-Particles` object](#spe-particles-object) | Properties of the particles effects component and its animations.
| ~~[environment](examples#background-themes)~~ | *A* | ~~[`Environment` object](#environment-object)~~ | ~~Environment options.~~ May be deprecated due to the new [`env-presets` object](#env-presets-object).
| [collision-listener](examples#events) | *A/P* | `string` | Name of the collision-listener, default can be empty string. e.g. ""
| [parent](examples#parentchild-linking) | *A/P* | `string` | `object_id` of the object which is the parent.
| [goto-url](examples#goto-url) | *A* | [`Goto URL` object](#goto-url-object) | Requires `click-listener`
| [landmark](examples#landmark) | *P* | [`Landmark` object](#landmark-object) | A landmark either as teleport destination or starting point


## "position" object
Follows A-Frame [position](https://aframe.io/docs/1.0.0/components/position.html).

### properties

|property|support|type|description
|---|---|---|---
| x | *A/P* | `number` | X-axis distance from origin, in meters (*default: 0*, **required**).
| y | *A/P* | `number` | Y-axis distance from origin, in meters (*default: 0*, **required**).
| z | *A/P* | `number` | Z-axis distance from origin, in meters (*default: 0*, **required**).

## "rotation" object
Follows A-Frame [rotation](https://aframe.io/docs/1.0.0/components/rotation.html).

### properties

|property|support|type|description
|---|---|---|---
| x | *A/P* | `number` | Quaternion rotation around the X-axis (*default: 0*, **required**).
| y | *A/P* | `number` | Quaternion rotation around the Y-axis (*default: 0*, **required**).
| z | *A/P* | `number` | Quaternion rotation around the Z-axis (*default: 0*, **required**).
| w | *A/P* | `number` | Quaternion value for theta (*default: 1*, **required**).

## "scale" object
Follows A-Frame [scale](https://aframe.io/docs/1.0.0/components/scale.html).

### properties

|property|support|type|description
|---|---|---|---
| x | *A/P* | `number` | X-axis length of object, in meters (*default: 1*, **required**).
| y | *A/P* | `number` | Y-axis length of object, in meters (*default: 1*, **required**).
| z | *A/P* | `number` | Z-axis length of object, in meters (*default: 1*, **required**).

## "material" object
Follows A-Frame [material](https://aframe.io/docs/1.0.0/components/material.html).

### properties

|property|support|type|description
|---|---|---|---
| src | *A* | `string` | URI, relative or full path of an image/video file. e.g. "images/360falls.mp4"
| transparent | *A/P* | `boolean` | e.g. true
| opacity | *A/P* | `number` | e.g. 0.5
| colorWrite | *A/P* | `boolean` | e.g. false
| render-order | *A/P* | `string` | e.g. "0"
| side | *A* | `string` | e.g. "back"
| color | *A* | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| repeat | *A* | [`Repeat` object](#repeat-object) | Used by `material`: `repeat`.

## "repeat" object
Follows A-Frame [repeating-textures](https://aframe.io/docs/1.0.0/components/material.html#repeating-textures).

### properties

|property|support|type|description
|---|---|---|---
| x | *A* | `number` | e.g. 4 (**required**).
| y | *A* | `number` | e.g. 4 (**required**).

## "multisrc" object

### properties

|property|support|type|description
|---|---|---|---
| srcspath | *A* | `string` | URI, relative or full path of a directory containing `srcs`, e.g. "images/dice/" (**required**).
| srcs | *A* | `string` | A comma-delimited list if URIs, e.g. "side1.png, side2.png, side3.png, side4.png, side5.png, side6.png" (**required**).

## "light" object
Follows A-Frame [light](https://aframe.io/docs/1.0.0/components/light.html).

### properties

|property|support|type|description
|---|---|---|---
| type | *A* | `string` | `ambient, directional, hemisphere, point, spot` e.g. "directional" (**required**).

## "animation" object
Follows A-Frame [animation](https://aframe.io/docs/1.0.0/components/animation.html).

### properties

|property|support|type|description
|---|---|---|---
| property | *A* | `string` | e.g. "rotation"
| to | *A* | `string` | e.g. "0 360 0"
| loop | *A* | `boolean` | e.g. true
| dur | *A* | `number` | e.g. 10000

## "animation-mixer" object
Follows Don McCurdy’s [animation-mixer](https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation).

### properties

|property|support|type|description
|---|---|---|---
| clip | *A/P* | `string` | Name of the clip sequence in the GLTF "scene". e.g. "Take 001"

## "meshline" object

### properties

|property|support|type|description
|---|---|---|---
| lineWidth | *A/P* | `number` | e.g. 11 (**required**).
| color | *A/P* | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*, **required**).
| path | *A/P* | `string` | e.g. "0 0 0, 0 0 1" (**required**).

## "sound" object
Follows A-Frame [sound](https://aframe.io/docs/1.0.0/components/sound.html).

### properties

|property|support|type|description
|---|---|---|---
| src | *A* | `string` | URI, relative or full path of a directory containing a sound file, e.g. "audio/toypiano/asharp1.wav" (**required**).
| on | *A* | `string` | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).
| positional | *A* | `boolean` | e.g. true
| poolSize | *A* | `number` | e.g. 8

## "dynamic-body" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system#dynamic-body-and-static-body).

### properties

|property|support|type|description
|---|---|---|---
| type | *A/P* | `string` | `none, static, dynamic` (**required**).

## "impulse" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system).

### properties

|property|support|type|description
|---|---|---|---
| on | *A/P* | `string` | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).
| force | *A/P* | `string` | e.g. "1 50 1" (**required**).
| position | *A/P* | `string` | e.g. "1 1 1" (**required**).

## "spe-particles" object
Follows [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component#aframe-spe-particles-component).

### properties

|property|support|type|description
|---|---|---|---
| texture | *A* | `string` | e.g. "textures/square.png"
| color | *A* | `string` | e.g. "yellow, red"
| particleCount | *A* | `number` | e.g. 3
| maxAge | *A* | `number` | e.g. 0.5
| maxAgeSpread | *A* | `number` | e.g. 1
| velocity | *A* | `string` | e.g. "40 200 40"
| velocitySpread | *A* | `string` | e.g. "10 3 10"
| wiggle | *A* | `string` | e.g. "50 0 50"
| wiggleSpread | *A* | `string` | e.g. "15 0 15"
| emitterScale | *A* | `number` | e.g. 8
| sizeSpread | *A* | `number` | e.g. 10
| randomizeVelocity | *A* | `boolean` | e.g. true

## "environment" object

### properties

|property|support|type|description
|---|---|---|---
| preset | *A/P* | `string` | e.g. `none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris` (**required**).

## "goto-url" object

### properties

|property|support|type|description
|---|---|---|---
| dest | *A* | `string` | `popup, newtab, sametab` e.g. "sametab" (**required**).
| on | *A* | `string` | e.g. "mousedown" (**required**).
| url | *A* | `string` | e.g. "http://www.formula1.com" (**required**).

## "landmark" object

### properties

|property|support|type|description
|---|---|---|---
| label | *A* | `string` | Label that shows up in landmarks list on bottom left of UI
| randomRadiusMin | *A* | `number` | Random radius min distance to teleport
| randomRadiusMax | *A* | `number` | Random radius max distance to teleport. Can be equal value as radius min, to enforce a circle of particular radius.
| lookAtLandmark | *A* | `boolean` | When used with an offsetPosition or randomRadius, whether to rotate user camera to look at the landmark base position.
| startingPosition | *A* | `boolean` | Whether to use this as a random starting position. Does *not* show up on landmarks list regardless of `label`
| offsetPosition | *A* | [`Position` object](#position-object) | Additive offset from object base position to teleport to e.g. `{ x: 3, y: 0, z: -1 }`
| constrainToNavMesh | *A* | `string` | One of `false`, `any` or `coplanar` to describe how a teleport should forcibly behave relative to a navigation mesh. `false` implies no forced constraint, `any` snaps to nearest navMesh, and `coplanar` only snaps to nearest navMeshes on *same* Y-plane

-------------------------

## "Event Data" object

### properties

|property|support|type|description
|---|---|---|---
| position | *A* | [`Position` object](#position-object) | The event destination position. (**required**)
| clickPos | *A* | [`Position` object](#position-object) | The event origination position. (**required**)
| source | *A* | `string` | `object_id` of event origination. e.g "camera_8715_er1k" (**required**)

-------------------------

## "Program Data" object
Follows [ARENA Program Schema](https://arenaxr.org/build/arena-program.json)

### properties

|property|support|type|description
|---|---|---|---
| name | *A* | `string` | Name of the program in the format namespace/program-name. e.g. "wiselab/arb" (**required**)
| affinity | *A* | `string` | Indicates the module affinity (client=client's runtime; none or empty=any suitable/available runtime) (*default: "client"*)
| instantiate | *A* | `string` | Single instance of the program (=single), or let every client create a program instance (=client). Per client instance will create new uuid for each program. (*default: "client"*, **required**)
| filename | *A* | `string` | Filename of the entry binary. e.g. "arb.py" (**required**)
| filetype | *A* | `string` | Type of the program (WA=WASM or PY=Python) (*default: "PY"*, **required**)
| args | *A* | `string` array | Command-line arguments (passed in argv). Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} e.g. [ "${scene}", "-b", " ${mqtth}" ]
| env | *A* | `string` array | Environment variables. Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} (*default: [ "MID=${moduleid}", "SCENE=${scene}", "MQTTH=${mqtth}", "REALM=realm" ]*, **required**)
| channels | *A* | [`Channel` object](#channel-object) array | Channels describe files representing access to IO from pubsub and client sockets (possibly more in the future; currently only supported for WASM programs).

## "channel" object
Follows [ARENA Program Schema](https://arenaxr.org/build/arena-program.json)

### properties

|property|support|type|description
|---|---|---|---
| path | *A* | `string` | Folder visible by the program. (*default: "/ch/${scene}"*, **required**)
| type | *A* | `string` | Pubsub or client socket. [ "pubsub", "client" ] (*default: "pubsub"*, **required**)
| mode | *A* | `string` | Access mode. [ "r", "w", "rw" ] (*default: "rw"*, **required**)
| params | *A* | [`Params` object](#params-object) | Type (i.e. pubsub/client)-specific parameters.

## "params" object
Follows [ARENA Program Schema](https://arenaxr.org/build/arena-program.json)

### properties

|property|support|type|description
|---|---|---
| topic | *A* | `string` | Pubsub topic (pubsub) (*default: "realm/s/${scene}"*)
| host | *A* | `string` | Destination host address (client socket; ignored for now)
| port | *A* | `number` | Destination port (client socket; ignored for now)

-------------------------

## "Scene Options Data" object
Follows [ARENA Scene Options Schema](https://arenaxr.org/build/arena-scene-options.json)

### properties

|property|support|type|description
|---|---|---|---
| env-presets | *A* | [`env-presets` object](#env-presets-object) | Environment presets.
| scene-options | *A* | [`scene-options` object](#scene-options-object) | Scene Options.

## "env-presets" object
Follows [ARENA Scene Options Schema](https://arenaxr.org/build/arena-scene-options.json) from the [aframe-environment-component](https://github.com/supermedium/aframe-environment-component).

### properties

|property|support|type|description
|---|---|---|---
| active | *A* | `boolean` | Show/hides the environment presets component. Use this instead of using the visible attribute. (*default: true*, **required**)
| preset | *A* | `string` | `none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, arches, threetowers, poison, tron, japan, dream, volcano, starry, osiris`; An A-Frame preset environment. (*default: "default"*, **required**)
| seed | *A* | `number` | Seed for randomization. If you don't like the layout of the elements, try another value for the seed. (*default: 1*)
| skyType | *A* | `string` | `none, color, gradient, atmosphere`; a sky type. (*default: "color"*)
| skyColor | *A* | `string` | Sky color. (*default: "#ffa500"*)
| horizonColor | *A* | `string` | Horizon color. (*default: "#ffa500"*)
| lighting | *A* | `string` | `none, distant, point`; A hemisphere light and a key light (directional or point) are added to the scene automatically when using the component. Use none if you don't want this automatic lighting set being added. The color and intensity are estimated automatically. (*default: "distant"*)
| shadow | *A* | `boolean` | Shadows on/off. Sky light casts shadows on the ground of all those objects with shadow component applied. (*default: false*)
| shadowSize | *A* | `number` | Size of the shadow, if applied. (*default: 10*)
| lightPosition | *A* | [`Position` object](#position-object) | Position of the main light. If skyType is atmospheric, only the orientation matters (is a directional light) and it can turn the scene into night when lowered towards the horizon. (*default: {"x": 0, "y": 1, "z": -0.2}*)
| fog | *A* | `number` | Amount of fog (0 = none, 1 = full fog). The color is estimated automatically. (*default: 0*)
| flatShading | *A* | `boolean` | Whether to show everything smoothed (false) or polygonal (true). (*default: false*)
| playArea | *A* | `number` | Radius of the area in the center reserved for the player and the game play. The ground is flat in there and no objects are placed inside. (*default: 1*)
| ground | *A* | `string` | `none, flat, hills, canyon, spikes, noise`; Orography style. (*default: "hills"*)
| groundScale | *A* | [`scale` object](#scale-object) | Ground dimensions (in meters). (*default: {"x": 1, "y": 1, "z": 1}*)
| groundYScale | *A* | `number` | Maximum height (in meters) of ground's features (hills, mountains, peaks..). (*default: 3*)
| groundTexture | *A* | `string` | `none, checkerboard, squares, walkernoise`; Texture applied to the ground. (*default: "none"*)
| groundColor | *A* | `string` | Main color of the ground. (*default: "#553e35"*)
| groundColor2 | *A* | `string` | Secondary color of the ground. Used for textures, ignored if groundTexture is none. (*default: "#694439"*)
| dressing | *A* | `string` | `none, cubes, pyramids, cylinders, hexagons, stones, trees, mushrooms, towers, apparatus, arches, torii`; Dressing is the term we use here for the set of additional objects that are put on the ground for decoration. (*default: "none"*)
| dressingAmount | *A* | `number` | `number` of objects used for dressing. (*default: 10*)
| dressingColor | *A* | `string` | Base color of dressing objects. (*default: "#795449"*)
| dressingScale | *A* | `number` | Height (in meters) of dressing objects. (*default: 5*)
| dressingVariance | *A* | [`Scale` object](#scale-object) | Maximum x,y,z meters to randomize the size and rotation of each dressing object. Use 0 0 0 for no variation in size nor rotation. (*default: {"x": 1, "y": 1, "z": 1}*)
| dressingUniformScale | *A* | `boolean` | If false, a different value is used for each coordinate x, y, z in the random variance of size. (*default: true*)
| dressingOnPlayArea | *A* | `number` | Amount of dressing on play area. (*default: 0*)
| grid | *A* | `string` | `none, 1x1, 2x2, crosses, dots, xlines, ylines`; Grid, 1x1 and 2x2 are rectangular grids of 1 and 2 meters side, respectively. (*default: "none"*)
| gridColor | *A* | `string` | Color of the grid. (*default: "#ccc"*)

## "scene-options" object
Follows [ARENA Scene Options Schema](https://arenaxr.org/build/arena-scene-options.json)

### properties

|property|support|type|description
|---|---|---|---
| jitsiServer | *A* | `string` | Jitsi host used for this scene. (*default: "mr.andrew.cmu.edu"*)
| bigscreen | *A* | `string` | Name of the 3D object used as a big screen when sharing desktop. (*default: "bigscreen"*)
| clickableOnlyEvents | *A* | `boolean` | true = publish only mouse events for objects with click-listeners; false = all objects publish mouse events. (*default: "true"*)
| privateScene | *A* | `boolean` | false = scene will be visible; true = scene will not show in listings. (*default: "false"*)
| speedModifier | *A* | `number` | Movement speed mulitiplier to base `30`. (e.g. `speedModifier: 2` results in `60` speed)
| navMesh | *A* | `string` | URL of gltf model to preload as nav-mesh
