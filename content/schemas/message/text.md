---
title: 
nav_order: 46
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Text
====


Display text. 

More properties at <a href='https://aframe.io/docs/1.3.0/components/text.html'>https://aframe.io/docs/1.3.0/components/text.html</a>

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Text Attributes
----------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database (default true = persist on server)|Yes|
|type|string; Must be: ```object```|```'object'```|AFrame 3D Object|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|Text data||Text Data|Yes|

### Text Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|string; Must be: ```text```|```text```|3D object type.|Yes|
|align|; One of: ```['left', 'center', 'right']```|```left```|align|No|
|alphaTest|number|```0.5```|alphaTest|No|
|anchor|; One of: ```['left', 'right', 'center', 'align']```|```center```|anchor|No|
|baseline|; One of: ```['top', 'center', 'bottom']```|```center```|baseline|No|
|color|string|```white```|color|No|
|font|string; One of: ```['aileronsemibold', 'dejavu', 'exo2bold', 'exo2semibold', 'kelsonsans', 'monoid', 'mozillavr', 'roboto', 'sourcecodepro']```|```roboto```|font|No|
|fontImage|string||fontImage|No|
|height|number||height|No|
|letterSpacing|number|```0```|letterSpacing|No|
|lineHeight|number||lineHeight|No|
|negate|boolean|```True```|negate|No|
|opacity|number|```1```|opacity|No|
|shader|; One of: ```['portal', 'flat', 'standard', 'sdf', 'msdf', 'ios10hls', 'skyshader', 'gradientshader']```|```sdf```|shader|No|
|side|; One of: ```['front', 'back', 'double']```|```double```|side|No|
|tabSize|number|```4```|tabSize|No|
|text|string||Please use attribute 'value' in new Text objects;|No|
|transparent||```True```|transparent|No|
|value|string|``````|Any string of ASCII characters. e.g. 'Hello world!'|No|
|whiteSpace|; One of: ```['normal', 'pre', 'nowrap']```|```normal```|whiteSpace|No|
|width|number|```5```|width|No|
|wrapCount|number|```40```|wrapCount|No|
|wrapPixels|number||wrapPixels|No|
|xOffset|number|```0```|xOffset|No|
|zOffset|number|```0.001```|zOffset|No|
|parent|string||Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|No|
|position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|3D object position|No|
|rotation|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|No|
|scale|[scale](scale)||3D object scale|No|
