---
title: Box Collision Listener
nav_order: 6
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


Box Collision Listener
======================


Listen for bounding-box collisions with user camera and hands. Must be applied to an object or model with geometric mesh. Collisions are determined by course bounding-box overlaps

Box Collision Listener Attributes
----------------------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|enabled|boolean|```True```|Publish detections, set `false` to disable|No|
|dynamic|boolean|```False```|Set true for a moving object, which should have its bounding box recalculated regularly to determine proper collision|Yes|