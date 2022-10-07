---
title: 
nav_order: 54
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Videosphere
===========


Videosphere Geometry

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Videosphere Attributes
-----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database (default true = persist on server)|Yes|
|type|string; Must be: ```object```|```'object'```|AFrame 3D Object|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|Videosphere data||Videosphere Data|Yes|

### Videosphere Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|string; Must be: ```videosphere```|```videosphere```|3D object type.|Yes|
|autoplay|boolean|```True```|autoplay|No|
|crossOrigin|string|```'anonymous'```|crossOrigin|No|
|loop|boolean|```True```|loop|No|
|radius|number|```5000```|radius|No|
|segmentsHeight|number|```64```|segments height|No|
|segmentsWidth|number|```64```|segments width|No|
|src|string||URI, relative or full path of an image/video file. e.g. 'store/users/wiselab/images/360falls.mp4'|No|
|parent|string||Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|No|
|position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|3D object position|No|
|rotation|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|No|
|scale|[scale](scale)||3D object scale|No|
|buffer|boolean|```true```|Transform geometry into a BufferGeometry to reduce memory usage at the cost of being harder to manipulate (geometries only: box, circle, cone, ...).|No|
|jitsi-video|[jitsi-video](jitsi-video)||Apply a jitsi video source to the geometry|No|
|material|[material](material)||The material properties of the object’s surface. |No|
|material-extras|[material-extras](material-extras)||Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. |No|
|multisrc|[multisrc](multisrc)||Define multiple visual sources applied to an object.|No|
|skipCache|boolean|```true```|Disable retrieving the shared geometry object from the cache. (geometries only: box, circle, cone, ...).|No|
