---
title: Function Definitions
nav_order: 3
layout: default
parent: Messaging Format
---

# Messaging Format Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

{% include alert type="warning" title="Coming Soon" content="Writing in progress..."%}

## Examples

### Object Message
```json
{"object_id": "cube_1", "action": "create", "type": "object", "data": {"object_type": "cube", "position": {"x": 1, "y": 1, "z": -1}, "rotation": {"x": 0, "y": 0, "z": 0, "w": 1}, "scale": {"x": 1, "y": 1, "z": 1}, "color": "#FF0000"}}
```

### Event Message
```json
{"object_id": "fallBox2", "action": "clientEvent", "type": "mousedown", "data": {"position": {"x": -0.993, "y": 0.342, "z": -1.797}, "source": "camera_8715_er"}}
```

### Program Message
```json
{"object_id": "6aafedf3-e313-4785-a456-939de8677f07", "action": "update", "persist": true, "type": "program", "data": {"name": "wiselab/arb", "instantiate": "single", "filename": "arb.py", "filetype": "PY", "args": ["${scene}", "-b", " ${mqtth}"]}}
```

### Scene Options Message
```json
{"object_id": "e9a16478-2606-4cd0-bb9f-b03879bc8baa", "action": "update", "persist": true, "type": "scene-options", "data": {"env-presets": {"active": true, "lighting": "distant", "lightPosition": {"x": 0, "y": 1, "z": -10}, "ground": "hills", "groundTexture": "squares", "groundColor": "#444241", "groundYScale": 0.5}, "scene-options": {"jitsiServer": "jitsi1.andrew.cmu.edu", "clickableOnlyEvents": true, "privateScene": true}}}
```

### Landmarks Message
```json
{"object_id": "af4cef99-2700-4986-b44c-c4ce7fddfc88", "action": "update", "persist": true, "type": "landmarks", "data": {"landmarks": [{"object_id": "controls_sign_img1", "label": "Sign: How to Move"}, {"object_id": "controls_sign_img2", "label": "Sign: Buttons"}, {"object_id": "controls_sign_img3", "label": "Sign: Video Capabilities"}, {"object_id": "controls_sign_img4", "label": "Sign: Chat, Find People and Landmarks"}]}}
```

## ARENA MQTT Message Payload JSON Specification

### properties

|name/example|JSON type|description
|--|--|--
| object_id | `string` | A unique name within the scene (**required**).
| action | `string` | An action to perform: `create, delete, update, clientEvent` (**required**).
| type | `string` | Message type: `object, program, scene-options, landmarks, rig, mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup`.
| [persist](examples#persisted-objects) | `boolean` | Save to persistance database (*default: false*).
| [ttl](examples#temporary-objects-ttl) | `number` | Time-to-live seconds to persist the object and automatically delete (*default: 0*).
| data | [`Object Data` object](#object-data-object) | The detailed properties of a program. Used by Message Type `object`.
| data | [`Event Data` object](#event-data-object) | The detailed properties of a program. Used by  by Event Type `mousedown (and others)`, Action: `clientEvent`.
| data | [`Program Data` object](#program-data-object) | The detailed properties of the object. Used by Message Type `program`.
| data | [`Scene Options Data` object](#scene-options-data-object) | The detailed properties of the scene environment. Used by Message Type `scene-options`.
| data | [`Landmarks Data` object](#landmarks-data-object) | The detailed properties of scene landmarks. Used by Message Type `landmarks`.

## "Object Data" object

{% include alert type="warning" title="Arbitrary A-Frame Components" content="
Some A-Frame attributes and components we don't officially include in our JSON may be usable by following certain [patterns of use](../developer/aframe). We make no promises!
"%}

### properties

|name/example|JSON type|description
|--|--|--
| object_type | `string` | An primitive type: `cube, sphere, circle, cone, cylinder, dodecahedron, icosahedron, tetrahedron, octahedron, plane, ring, torus, torusKnot, triangle`
| | | Also: `gltf_model, image, particle, text, line, light, thickline`
| [position](examples#move) | [`Position` object](#position-object)
| [rotation](examples#rotate) | [`Rotation` object](#rotation-object)
| scale | [`scale` object](#scale-object)
| [color](examples#color) | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| [text](examples#text) | `string` | Any `string` of [ASCII characters](https://aframe.io/docs/1.0.0/components/text.html#non-ascii-characters). e.g. "Hello world!"
| [click-listener](examples#events) | string
| [url](examples#images) | `string` | URI, relative or full path of a file. e.g. "https://arena.andrew.cmu.edu/models/Duck.glb"
| material | [`Material` object](#material-object)
| multisrc | [`Multisrc` object](#multisrc-object)
| [light](examples#lights) | [`Light` object](#light-object) | Used by `object_type`: `light`.
| [animation](examples#animate) | [`Animation` object](#animation-object)
| [animation-mixer](examples#animating-gltf-models) | [`Animation-Mixer` object](#animation-mixer-object)
| [start](examples#lines) | [`Position` object](#position-object) | Used by `object_type`: `line`.
| [end](examples#lines) | [`Position` object](#position-object) | Used by `object_type`: `line`.
| [meshline](examples#thicklines) | [`Meshline` object](#meshline-object) | Used by `object_type`: `thickline`.
| [sound](examples#sound) | [`Sound` object](#sound-object) | Requires `click-listener`
| [dynamic-body](examples#physics) | [`Dynamic-Body` object](#dynamic-body-object)
| [impulse](examples#physics) | [`Impulse` object](#impulse-object) | Requires `click-listener`
| [spe-particles](examples#particles) | [`SPE-Particles` object](#spe-particles-object)
| [environment](examples#background-themes) | [`Environment` object](#environment-object)
| [collision-listener](examples#events) | string
| [parent](examples#parentchild-linking) | `string` | `object_id` of the object which is the parent.
| [goto-url](examples#goto-url) | [`Goto URL` object](#goto-url-object) | Requires `click-listener`

## "position" object
Follows A-Frame [position](https://aframe.io/docs/1.0.0/components/position.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | `number` | X-axis distance from origin, in meters (*default: 0*, **required**).
| y | `number` | Y-axis distance from origin, in meters (*default: 0*, **required**).
| z | `number` | Z-axis distance from origin, in meters (*default: 0*, **required**).

## "rotation" object
Follows A-Frame [rotation](https://aframe.io/docs/1.0.0/components/rotation.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | `number` | Quaternion rotation around the X-axis (*default: 0*, **required**).
| y | `number` | Quaternion rotation around the Y-axis (*default: 0*, **required**).
| z | `number` | Quaternion rotation around the Z-axis (*default: 0*, **required**).
| w | `number` | Quaternion value for theta (*default: 1*, **required**).

## "scale" object
Follows A-Frame [scale](https://aframe.io/docs/1.0.0/components/scale.html).

### properties

|name/example|JSON type|description
|--|--|--
| x | `number` | X-axis length of object, in meters (*default: 1*, **required**).
| y | `number` | Y-axis length of object, in meters (*default: 1*, **required**).
| z | `number` | Z-axis length of object, in meters (*default: 1*, **required**).

## "material" object
Follows A-Frame [material](https://aframe.io/docs/1.0.0/components/material.html).

### properties

|name/example|JSON type|description
|--|--|--
| src | `string` | URI, relative or full path of an image/video file. e.g. "images/360falls.mp4"
| transparent | `boolean` | e.g. true
| opacity | `number` | e.g. 0.5
| colorWrite | `boolean` | e.g. false
| render-order | `string` | e.g. "0"
| side | `string` | e.g. "back"
| color | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*).
| repeat | [`Repeat` object](#repeat-object) | Used by `material`: `repeat`.

## "repeat" object
Follows A-Frame [repeating-textures](https://aframe.io/docs/1.0.0/components/material.html#repeating-textures).

### properties

|name/example|JSON type|description
|--|--|--
| x | `number` | e.g. 4 (**required**).
| y | `number` | e.g. 4 (**required**).

## "multisrc" object

### properties

|name/example|JSON type|description
|--|--|--
| srcspath | `string` | URI, relative or full path of a directory containing `srcs`, e.g. "images/dice/" (**required**).
| srcs | `string` | A comma-delimited list if URIs, e.g. "side1.png, side2.png, side3.png, side4.png, side5.png, side6.png" (**required**).

## "light" object
Follows A-Frame [light](https://aframe.io/docs/1.0.0/components/light.html).

### properties

|name/example|JSON type|description
|--|--|--
| type | `string` | `ambient, directional, hemisphere, point, spot` e.g. "directional" (**required**).

## "animation" object
Follows A-Frame [animation](https://aframe.io/docs/1.0.0/components/animation.html).

### properties

|name/example|JSON type|description
|--|--|--
| property | `string` | e.g. "rotation"
| to | `string` | e.g. "0 360 0"
| loop | `boolean` | e.g. true
| dur | `number` | e.g. 10000

## "animation-mixer" object
Follows Don McCurdy’s [animation-mixer](https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation).

### properties

|name/example|JSON type|description
|--|--|--
| clip | `string` | e.g. "*"

## "meshline" object

### properties

|name/example|JSON type|description
|--|--|--
| lineWidth | `number` | e.g. 11 (**required**).
| color | `string` | A hexadecimal color or [CSS/HTML color](https://htmlcolorcodes.com/color-names) name (*default: "#FFFFFF"*) (**required**).
| path | `string` | e.g. "0 0 0, 0 0 1" (**required**).

## "sound" object
Follows A-Frame [sound](https://aframe.io/docs/1.0.0/components/sound.html).

### properties

|name/example|JSON type|description
|--|--|--
| src | `string` | URI, relative or full path of a directory containing a sound file, e.g. "url(https://arena.andrew.cmu.edu/audio/toypiano/Asharp1.wav)" (**required**).
| on | `string` | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).

## "dynamic-body" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system#dynamic-body-and-static-body).

### properties

|name/example|JSON type|description
|--|--|--
| type | `string` | `none, static, dynamic` (**required**).

## "impulse" object
Follows [aframe-physics-system](https://github.com/n5ro/aframe-physics-system).

### properties

|name/example|JSON type|description
|--|--|--
| on | `string` | `mousedown, mouseup, mouseenter, mouseleave, triggerdown, triggerup, gripdown, gripup, menudown, menuup, systemdown, systemup, trackpaddown, trackpadup` (**required**).
| force | `string` | e.g. "1 50 1" (**required**).
| position | `string` | e.g. "1 1 1" (**required**).

## "spe-particles" object
Follows [aframe-spe-particles-component](https://github.com/harlyq/aframe-spe-particles-component#aframe-spe-particles-component).

### properties

|name/example|JSON type|description
|--|--|--
| texture | `string` | e.g. "textures/square.png"
| color | `string` | e.g. "yellow, red"
| particleCount | `number` | e.g. 3
| maxAge | `number` | e.g. 0.5
| maxAgeSpread | `number` | e.g. 1
| velocity | `string` | e.g. "40 200 40"
| velocitySpread | `string` | e.g. "10 3 10"
| wiggle | `string` | e.g. "50 0 50"
| wiggleSpread | `string` | e.g. "15 0 15"
| emitterScale | `number` | e.g. 8
| sizeSpread | `number` | e.g. 10
| randomizeVelocity | `boolean` | e.g. true

## "environment" object

### properties

|name/example|JSON type|description
|--|--|--
| preset | `string` | e.g. `none, default, contact, egypt, checkerboard, forest, goaland, yavapai, goldmine, threetowers, poison, arches, tron, japan, dream, volcano, starry, osiris` (**required**).

## "goto-url" object

### properties

|name/example|JSON type|description
|--|--|--
| dest | `string` | `popup, newtab, sametab` e.g. "sametab" (**required**).
| on | `string` | e.g. "mousedown" (**required**).
| url | `string` | e.g. "http:www.formula1.com" (**required**).

## "Program Data" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| name | `string` | Name of the program in the format namespace/program-name. e.g. "wiselab/arb" (**required**)
| affinity | `string` | Indicates the module affinity (client=client's runtime; none or empty=any suitable/available runtime) (*default: "client"*)
| instantiate | `string` | Single instance of the program (=single), or let every client create a program instance (=client). Per client instance will create new uuid for each program. (*default: "client"*, **required**)
| filename | `string` | Filename of the entry binary. e.g. "arb.py" (**required**)
| filetype | `string` | Type of the program (WA=WASM or PY=Python) (*default: "PY"*, **required**)
| args | `string` array | Command-line arguments (passed in argv). Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} e.g. [ "${scene}", "-b", " ${mqtth}" ]
| env | `string` array | Environment variables. Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key} (*default: [ "MID=${moduleid}", "SCENE=${scene}", "MQTTH=${mqtth}", "REALM=realm" ]*, **required**)
| channels | [`Channel` object](#channel-object) array | Channels describe files representing access to IO from pubsub and client sockets (possibly more in the future; currently only supported for WASM programs). 

## "channel" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| path | `string` | Folder visible by the program. (*default: "/ch/${scene}"*, **required**)
| type | `string` | Pubsub or client socket. [ "pubsub", "client" ] (*default: "pubsub"*, **required**)
| mode | `string` | Access mode. [ "r", "w", "rw" ] (*default: "rw"*, **required**)
| params | [`Params` object](#params-object) | Type (i.e. pubsub/client)-specific parameters.

## "params" object
Follows [ARENA Program Schema](https://arena.andrew.cmu.edu/build/arena-program.json)

### properties

|name/example|JSON type|description
|--|--|--
| topic | `string` | Pubsub topic (pubsub) (*default: "realm/s/${scene}"*)
| host | `string` | Destination host address (client socket; ignored for now)
| port | `number` | Destination port (client socket; ignored for now)

## "Event Data" object

### properties

|name/example|JSON type|description
|--|--|--
| position | [`Position` object](#position-object) | The event destination position.
| click_pos | [`Position` object](#position-object) | The event origination position.
| source | `string` | `object_id` of event origination. e.g  "camera_8715_er1k"

## "Scene Options Data" object
Follows [ARENA Scene Options Schema](https://arena.andrew.cmu.edu/build/arena-scene-options.json)

### properties

|name/example|JSON type|description
|--|--|--
| env-presets | [`env-presets` object](#env-presets-object) | Environment presets.
| scene-options | [`scene-options` object](#scene-options-object) | Scene Options.

## "env-presets" object
Follows [ARENA Scene Options Schema](https://arena.andrew.cmu.edu/build/arena-scene-options.json)

### properties

|name/example|JSON type|description
|--|--|--
| active | `boolean` | Show/hides the environment presets component. Use this instead of using the visible attribute. (**required**)
| preset | `string` | An A-frame preset environment. (**required**)
| seed | `number` | Seed for randomization. If you don't like the layout of the elements, try another value for the seed.
| skyType | `string` | `none, color, gradient, atmosphere`; a sky type.
| skyColor | `string` | `none, distant, point`; sky color. (*default: "#ffa500"*)
| horizonColor | `string` | Horizon color. (*default: "#ffa500"*)
| lighting | `string` | A hemisphere light and a key light (directional or point) are added to the scene automatically when using the component. Use none if you don't want this automatic lighting set being added. The color and intensity are estimated automatically.
| shadow | `boolean` | Shadows on/off. Sky light casts shadows on the ground of all those objects with shadow component applied.
| shadowSize | `number` | Size of the shadow, if applied. (*default: 10*)
| lightPosition | [`Position` object](#position-object) | Position of the main light. If skyType is atmospheric, only the orientation matters (is a directional light) and it can turn the scene into night when lowered towards the horizon.
| fog | `number` | Amount of fog (0 = none, 1 = full fog). The color is estimated automatically.
| flatShading | `boolean` | Whether to show everything smoothed (false) or polygonal (true).
| playArea | `number` | Radius of the area in the center reserved for the player and the game play. The ground is flat in there and no objects are placed inside.
| ground | `string` | `none, flat, hills, canyon, spikes, noise`; Orography style.
| groundScale | [`scale` object](#scale-object) | Ground dimensions (in meters).
| groundYScale | `number` | Maximum height (in meters) of ground's features (hills, mountains, peaks..).
| groundTexture | `string` | `none, checkerboard, squares, walkernoise`; Texture applied to the ground.
| groundColor | `string` | Main color of the ground.
| groundColor2 | `string` | Secondary color of the ground. Used for textures, ignored if groundTexture is none.
| dressing | `string` | Dressing is the term we use here for the set of additional objects that are put on the ground for decoration.
| dressingAmount | `number` | Number of objects used for dressing.
| dressingColor | `string` | Base color of dressing objects.
| dressingScale | `number` | Height (in meters) of dressing objects.
| dressingVariance | [`Scale` object](#scale-object) | Maximum x,y,z meters to randomize the size and rotation of each dressing object. Use 0 0 0 for no variation in size nor rotation.
| dressingUniformScale | `boolean` | If false, a different value is used for each coordinate x, y, z in the random variance of size.
| dressingOnPlayArea | `number` | Amount of dressing on play area.
| grid | `string` | Grid, 1x1 and 2x2 are rectangular grids of 1 and 2 meters side, respectively.
| gridColor | `string` | Color of the grid.


## "scene-options" object
Follows [ARENA Scene Options Schema](https://arena.andrew.cmu.edu/build/arena-scene-options.json)

### properties

|name/example|JSON type|description
|--|--|--
| jitsiServer | `string` | Jitsi host used for this scene.
| bigscreen | `string` | Name of the 3D object used as a big screen when sharing desktop.
| clickableOnlyEvents | `boolean` | true = publish only mouse events for objects with click-listeners; false = all objects publish mouse events.
| privateScene | `boolean` | false = scene will be visible; true = scene will not show in listings.

## "Landmarks Data" object
Follows [ARENA Landmarks Schema](https://arena.andrew.cmu.edu/build/arena-landmarks.json)

### properties

|name/example|JSON type|description
|--|--|--
| landmarks | [`Landmark` object](#landmark-object) array | List of landmarks of the scene. (**required**)

## "landmark" object
Follows [ARENA Landmarks Schema](https://arena.andrew.cmu.edu/build/arena-landmarks.json)

### properties

|name/example|JSON type|description
|--|--|--
| object_id | `string` | Identifier of the scene object to be used as the position of the landmark. The position and orientation of this object is used to place the user. (**required**)
| label | `string` | Description used in the landmark list. (**required**)

