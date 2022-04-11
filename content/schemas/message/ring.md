---
title: 
nav_order: 32
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Ring
====


Ring Geometry

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Ring Attributes
----------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default true = persist on server)|boolean|```true```|Yes|
|type|AFrame 3D Object|string; Must be: ```object```|```'object'```|Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|Yes|
|data|Ring Data|Ring data||Yes|

### Ring Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|3D object type.|string; Must be: ```ring```|```ring```|Yes|
|radiusInner|radius inner|number|```1```|Yes|
|radiusOuter|radius outer|number|```1```|Yes|
|segmentsPhi|segments phi|number|```8```|No|
|segmentsTheta|segments theta|number|```32```|No|
|thetaLength|theta length|number|```360```|No|
|thetaStart|theta start|number|```0```|No|
|animation|See: [animation](animation)|animation||No|
|armarker|See: [armarker](armarker)|armarker||No|
|click-listener|Object will listen for clicks|boolean||No|
|collision-listener|Name of the collision-listener, default can be empty string|string||No|
|color|Color|string|```'#ffa500'```|No|
|dynamic-body|See: [dynamic-body](dynamic-body)|dynamic-body||No|
|goto-url|See: [goto-url](goto-url)|goto-url||No|
|hide-on-enter-ar|Hide object when entering AR. Remove component to *not* hide|boolean; Must be: ```True```|```True```|No|
|impulse|See: [impulse](impulse)|impulse||No|
|landmark|See: [landmark](landmark)|landmark||No|
|material-extras|See: [material-extras](material-extras)|material-extras||No|
|parent|Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|string||No|
|position|See: [position](position)|position|```{'x': 0, 'y': 0, 'z': 0}```|No|
|rotation|See: [rotation](rotation)|rotation|```{'x': 0, 'y': 0, 'z': 0}```|No|
|scale|See: [scale](scale)|scale||No|
|shadow|See: [shadow](shadow)|shadow||No|
|sound|See: [sound](sound)|sound||No|
|url|Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|string||No|
|screenshareable|Whether or not a user can screenshare on an object|boolean|```True```|No|
|video-control|See: [video-control](video-control)|video-control||No|
|buffer|Transform geometry into a BufferGeometry to reduce memory usage at the cost of being harder to manipulate (geometries only: box, circle, cone, ...).|boolean|```true```|No|
|jitsi-video|See: [jitsi-video](jitsi-video)|jitsi-video||No|
|material|See: [material](material)|material|```{'color': '#7f7f7f'}```|No|
|multisrc|See: [multisrc](multisrc)|multisrc||No|
|skipCache|Disable retrieving the shared geometry object from the cache. (geometries only: box, circle, cone, ...).|boolean|```true```|No|
