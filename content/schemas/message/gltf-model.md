---
title: 
nav_order: 16
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


GLTF Model
==========


Load a GLTF model. 

Format: <a href='https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/README.md'>https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/README.md</a>

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

GLTF Model Attributes
----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database (default true = persist on server)|Yes|
|type|string; Must be: ```object```|```'object'```|AFrame 3D Object|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|GLTF Model data||GLTF Model Data|Yes|

### GLTF Model Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|string; Must be: ```gltf-model```|```gltf-model```|3D object type.|Yes|
|url|string||Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|Yes|
|animation|[animation](animation)||Animate and tween values. |No|
|armarker|[armarker](armarker)||A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.|No|
|click-listener|boolean||Object will listen for clicks|No|
|collision-listener|string||Name of the collision-listener, default can be empty string|No|
|color|string|```'#ffa500'```|Color|No|
|dynamic-body|[dynamic-body](dynamic-body)||Physics type attached to the object. |No|
|goto-landmark|[goto-landmark](goto-landmark)||Teleports user to the landmark with the given name; Requires click-listener|No|
|goto-url|[goto-url](goto-url)||Goto given URL; Requires click-listener|No|
|hide-on-enter-ar|boolean; Must be: ```True```|```True```|Hide object when entering AR. Remove component to *not* hide|No|
|hide-on-enter-vr|boolean; Must be: ```True```|```True```|Hide object when entering VR. Remove component to *not* hide|No|
|impulse|[impulse](impulse)||The force applied using physics. Requires click-listener|No|
|landmark|[landmark](landmark)||Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)|No|
|material-extras|[material-extras](material-extras)||Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. |No|
|parent|string||Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|No|
|position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|3D object position|Yes|
|rotation|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|Yes|
|scale|[scale](scale)|```{'x': 1, 'y': 1, 'z': 1}```|3D object scale|Yes|
|shadow|[shadow](shadow)||shadow|No|
|sound|[sound](sound)||The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. |No|
|screenshareable|boolean|```True```|Whether or not a user can screenshare on an object|No|
|video-control|[video-control](video-control)||Video Control|No|
|animation-mixer|[animation-mixer](animation-mixer)||A list of available animations can usually be found by inspecting the model file or its documentation. All animations will play by default. To play only a specific set of animations, use wildcards: animation-mixer='clip: run_*'. |No|
|gltf-model-lod|[gltf-model-lod](gltf-model-lod)||Simple switch between the default gltf-model and a detailed one when a user camera is within specified distance|No|
