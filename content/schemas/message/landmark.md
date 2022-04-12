---
title: 
nav_order: 21
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Landmark
========


Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)

Landmark Attributes
--------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|randomRadiusMin|Minimum radius from the landmark to teleport to. (randomRadiusMax must > 0)|number|```0```|No|
|randomRadiusMax|Maximum radius from the landmark to teleport to.|number|```0```|No|
|offsetPosition|Use as a static teleport x,y,z offset|||No|
|constrainToNavMesh|Teleports should snap to navmesh. Valid values: 'false', 'any', 'coplanar'|string; One of: ```['false', 'any', 'coplanar']```|```'false'```|No|
|startingPosition|Set to true to use this landmark as a scene start (spawn) position. If several landmarks with startingPosition=true exist in a scene, one will be randomly selected.|boolean|```False```|No|
|lookAtLandmark|Set to true to make users face the landmark when teleported to it.|boolean|```True```|No|
|label|Landmark description to display in the landmark list|string|```''```|Yes|
