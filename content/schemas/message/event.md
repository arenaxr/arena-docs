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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```false```|Persist this object in the database (default false = do not persist on server)|No|
|type|string; One of: ```['mousedown', 'mouseup', 'mouseenter', 'mouseleave', 'triggerdown', 'triggerup', 'gripdown', 'gripup', 'menudown', 'menuup', 'systemdown', 'systemup', 'trackpaddown', 'trackpadup', 'soundplay', 'soundpause', 'soundstop']```||One of the client event action types like 'mousedown'.|Yes|
|action|string; Must be: ```clientEvent```|```'clientEvent'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|Event data||Event Data|Yes|

### Event Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|source|string||The `object_id` of event origination. e.g camera or client program connection id.|Yes|
|position|[position](position)||The event destination position in 3D.|Yes|
|clickPos|||The event origination position in 3D.|No|