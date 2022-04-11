---
title: 
nav_order: 41
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Thickline
=========


Draw a line that can have a custom width

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Thickline Attributes
---------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default true = persist on server)|boolean|```true```|Yes|
|type|AFrame 3D Object|string; Must be: ```object```|```'object'```|Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|Yes|
|data|Thickline Data|Thickline data||Yes|

### Thickline Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|3D object type.|string; Must be: ```thickline```|```thickline```|Yes|
|lineWidth|Line width|number|```5```|No|
|lineWidthStyler|Allows defining the line width as a function of relative position p along the path of the line. By default it is set to a constant 1. The final, rendered width is scaled by lineWidth. You can use p in your function definition. It varies from 0 at the first vertex of the path to 1 at the last vertex of the path.|number|```1```|No|
|path|Comma-seperated list of x y z coordinates of the line vertices|string|```-2 -1 0, 0 20 0, 10 -1 10```|Yes|
|animation|See: [animation](animation)|animation||No|
|armarker|See: [armarker](armarker)|armarker||No|
|click-listener|Object will listen for clicks|boolean||No|
|collision-listener|Name of the collision-listener, default can be empty string|string||No|
|color|Color|string|```#7f7f7f```|No|
|dynamic-body|See: [dynamic-body](dynamic-body)|dynamic-body||No|
|goto-url|See: [goto-url](goto-url)|goto-url||No|
|hide-on-enter-ar|Hide object when entering AR. Remove component to *not* hide|boolean; Must be: ```True```|```True```|No|
|impulse|See: [impulse](impulse)|impulse||No|
|landmark|See: [landmark](landmark)|landmark||No|
|material-extras|See: [material-extras](material-extras)|material-extras||No|
|parent|Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|string||No|
|position|See: [position](position)|position||No|
|rotation|See: [rotation](rotation)|rotation||No|
|scale|See: [scale](scale)|scale||No|
|shadow|See: [shadow](shadow)|shadow||No|
|sound|See: [sound](sound)|sound||No|
|url|Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|string||No|
|screenshareable|Whether or not a user can screenshare on an object|boolean|```True```|No|
|video-control|See: [video-control](video-control)|video-control||No|
|buffer|Transform geometry into a BufferGeometry to reduce memory usage at the cost of being harder to manipulate (geometries only: box, circle, cone, ...).|boolean|```true```|No|
|jitsi-video|See: [jitsi-video](jitsi-video)|jitsi-video||No|
|material|See: [material](material)|material||No|
|multisrc|See: [multisrc](multisrc)|multisrc||No|
|skipCache|Disable retrieving the shared geometry object from the cache. (geometries only: box, circle, cone, ...).|boolean|```true```|No|
