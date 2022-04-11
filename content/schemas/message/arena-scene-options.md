---
title: 
nav_order: 3
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Scene Config
============


Scene Config

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Scene Config Attributes
------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string|```'scene-options'```|Yes|
|persist|Persist this object in the database|boolean|```true```|Yes|
|type|ARENA scene options|string; Must be: ```scene-options```|```'scene-options'```|Yes|
|action|One of 3 basic Create/Update/Delete actions|string; One of: ```['create', 'delete', 'update']```|```'create'```|Yes|
|data|Scene Config Data|Scene Config data||Yes|

### Scene Config Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|env-presets|See: [environment-presets](environment-presets)|environment-presets||Yes|
|renderer-settings|See: [renderer-settings](renderer-settings)|renderer-settings||No|
|scene-options|See: [scene-options](scene-options)|scene-options||Yes|
