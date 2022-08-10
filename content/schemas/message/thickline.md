---
title: 
nav_order: 46
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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database (default true = persist on server)|Yes|
|type|string; Must be: ```object```|```'object'```|AFrame 3D Object|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|Thickline data||Thickline Data|Yes|

### Thickline Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|string; Must be: ```thickline```|```thickline```|3D object type.|Yes|
|color|string|```#7f7f7f```|color|No|
|lineWidth|number|```5```|Line width|No|
|lineWidthStyler|number|```1```|Allows defining the line width as a function of relative position p along the path of the line. By default it is set to a constant 1. The final, rendered width is scaled by lineWidth. You can use p in your function definition. It varies from 0 at the first vertex of the path to 1 at the last vertex of the path.|No|
|path|string|```-2 -1 0, 0 20 0, 10 -1 10```|Comma-separated list of x y z coordinates of the line vertices|Yes|
|parent|string||Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|No|
|position|[position](position)||3D object position|No|
|rotation|[rotation](rotation)||3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|No|
|scale|[scale](scale)||3D object scale|No|
