---
title: 
nav_order: 39
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Sphere
======


Sphere Geometry

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Sphere Attributes
------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default true = persist on server)|boolean|```true```|Yes|
|type|AFrame 3D Object|string; Must be: ```object```|```'object'```|Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|Yes|
|data|Sphere Data|Sphere data||Yes|

### Sphere Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|3D object type.|string; Must be: ```sphere```|```sphere```|Yes|
|phiLength|phi length|number|```360```|No|
|phiStart|phi start|number|```0```|No|
|radius|radius|number|```1```|No|
|segmentsHeight|segments height|number|```36```|No|
|segmentsWidth|segments width|number|```18```|No|
|thetaLength|theta length|number|```360```|No|
|thetaStart|theta start|number|```0```|No|
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
|position|3D object position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|No|
|rotation|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|No|
|scale|3D object scale|[scale](scale)||No|
|shadow|shadow|[shadow](shadow)||No|
|sound|The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. |[sound](sound)||No|
|url|Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|string||No|
|screenshareable|Whether or not a user can screenshare on an object|boolean|```True```|No|
|video-control|Video Control|[video-control](video-control)||No|
|buffer|Transform geometry into a BufferGeometry to reduce memory usage at the cost of being harder to manipulate (geometries only: box, circle, cone, ...).|boolean|```true```|No|
|jitsi-video|Apply a jitsi video source to the geometry|[jitsi-video](jitsi-video)||No|
|material|The material properties of the object’s surface. |[material](material)|```{'color': '#7f7f7f'}```|No|
|multisrc|Define multiple visual sources applied to an object.|[multisrc](multisrc)||No|
|skipCache|Disable retrieving the shared geometry object from the cache. (geometries only: box, circle, cone, ...).|boolean|```true```|No|
