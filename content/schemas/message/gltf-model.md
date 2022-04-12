---
title: 
nav_order: 16
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


GLTF Model
==========


Load a GLTF model

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

GLTF Model Attributes
----------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default true = persist on server)|boolean|```true```|Yes|
|type|AFrame 3D Object|string; Must be: ```object```|```'object'```|Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|Yes|
|data|GLTF Model Data|GLTF Model data||Yes|

### GLTF Model Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|3D object type.|string; Must be: ```gltf-model```|```gltf-model```|Yes|
|url|Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|string||Yes|
|animation|Animate and tween values. |[animation](animation)||No|
|armarker|A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.|[armarker](armarker)||No|
|click-listener|Object will listen for clicks|boolean||No|
|collision-listener|Name of the collision-listener, default can be empty string|string||No|
|color|Color|string|```'#ffa500'```|No|
|dynamic-body|Physics type attached to the object. |[dynamic-body](dynamic-body)||No|
|goto-url|Goto given URL; Requires click-listener|[goto-url](goto-url)||No|
|hide-on-enter-ar|Hide object when entering AR. Remove component to *not* hide|boolean; Must be: ```True```|```True```|No|
|impulse|The force applied using physics. Requires click-listener|[impulse](impulse)||No|
|landmark|Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)|[landmark](landmark)||No|
|material-extras|Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. |[material-extras](material-extras)||No|
|parent|Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|string||No|
|position|3D object position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|Yes|
|rotation|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|Yes|
|scale|3D object scale|[scale](scale)|```{'x': 1, 'y': 1, 'z': 1}```|Yes|
|shadow|shadow|[shadow](shadow)||No|
|sound|The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. |[sound](sound)||No|
|screenshareable|Whether or not a user can screenshare on an object|boolean|```True```|No|
|video-control|Video Control|[video-control](video-control)||No|
|animation-mixer|A list of available animations can usually be found by inspecting the model file or its documentation. All animations will play by default. To play only a specific set of animations, use wildcards: animation-mixer='clip: run_*'. |[animation-mixer](animation-mixer)||No|
|gltf-model-lod|Simple switch between the default gltf-model and a detailed one when a user camera is within specified distance|[gltf-model-lod](gltf-model-lod)||No|
