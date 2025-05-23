---
title: Physics Settings
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


Physics Settings
================


Clientside PhysX-based physics system. Required for all physx-* components

Physics Settings Attributes
----------------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|**enabled**|boolean|```False```|Set true to load|Yes|
|**delay**|number|```5000```|Amount of time in ms to wait after loading before starting the physics. Can be useful if there is still some things loading or initializing elsewhere in the scene|No|
|**useDefaultScene**|boolean|```True```|If true, sets up a default scene with a ground plane and bounding cylinder.|No|
|**throttle**|number|```10```|Throttle for running the physics simulation. On complex scenes, you can increase this to avoid dropping video frames|No|
|**speed**|number|```1```|Simulation speed multiplier. Increase or decrease to speed up or slow down simulation time|No|
|**groundCollisionLayers**|array|```[2]```|Which collision layers the ground belongs to|No|
|**groundCollisionMask**|array|```[1, 2, 3, 4]```|Which collision layers will collide with the ground|No|
|**gravity**|[vector3](vector3)|```{'x': 0, 'y': -9.8, 'z': 0}```|Gravity vector in m/s^2|No|
|**stats**|array|```[]```|Where to output performance stats:, panel, console, events (or some combination)|No|
