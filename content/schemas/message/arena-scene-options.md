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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string|```'scene-options'```|A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database|Yes|
|type|string; Must be: ```scene-options```|```'scene-options'```|ARENA scene options|Yes|
|action|string; One of: ```['create', 'delete', 'update']```|```'create'```|One of 3 basic Create/Update/Delete actions|Yes|
|data|Scene Config data||Scene Config Data|Yes|

### Scene Config Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|env-presets|[environment-presets](environment-presets)||A-Frame Environment presets. |Yes|
|renderer-settings|[renderer-settings](renderer-settings)||These settings are fed into three.js WebGLRenderer properties|No|
|scene-options|[scene-options](scene-options)||ARENA Scene Options|Yes|