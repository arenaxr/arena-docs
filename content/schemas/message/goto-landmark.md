---
title: Goto Landmark
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


Goto Landmark
=============


Teleports user to the landmark with the given name. Requires `click-listener` attribute.

Goto Landmark Attributes
-------------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|**on**|string; One of: ```['mousedown', 'mouseup']```|```'mousedown'```|Event to listen 'on'.|Yes|
|**landmark**|string|```''```|Id of landmark to teleport to.|Yes|
