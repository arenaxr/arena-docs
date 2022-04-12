---
title: 
nav_order: 14
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Event
=====


Generate an event message for an object.

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Event Attributes
-----------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default false = do not persist on server)|boolean|```false```|No|
|type|One of the client event action types like 'mousedown'.|string; One of: ```['mousedown', 'mouseup', 'mouseenter', 'mouseleave', 'triggerdown', 'triggerup', 'gripdown', 'gripup', 'menudown', 'menuup', 'systemdown', 'systemup', 'trackpaddown', 'trackpadup', 'soundplay', 'soundpause', 'soundstop']```||Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; Must be: ```clientEvent```|```'clientEvent'```|Yes|
|data|Event Data|Event data||Yes|

### Event Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|source|The `object_id` of event origination. e.g camera or client program connection id.|string||Yes|
|position|The event destination position in 3D.|[position](position)||Yes|
|clickPos|The event origination position in 3D.|||No|
