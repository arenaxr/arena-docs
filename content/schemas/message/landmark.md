---
title: 
nav_order: 22
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Landmark
========


Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)

Landmark Attributes
--------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|randomRadiusMin|number|```0```|Minimum radius from the landmark to teleport to. (randomRadiusMax must > 0)|No|
|randomRadiusMax|number|```0```|Maximum radius from the landmark to teleport to.|No|
|offsetPosition|||Use as a static teleport x,y,z offset|No|
|constrainToNavMesh|string; One of: ```['false', 'any', 'coplanar']```|```'false'```|Teleports should snap to navmesh. Valid values: 'false', 'any', 'coplanar'|No|
|startingPosition|boolean|```False```|Set to true to use this landmark as a scene start (spawn) position. If several landmarks with startingPosition=true exist in a scene, one will be randomly selected.|No|
|lookAtLandmark|boolean|```True```|Set to true to make users face the landmark when teleported to it.|No|
|label|string|```''```|Landmark description to display in the landmark list|Yes|