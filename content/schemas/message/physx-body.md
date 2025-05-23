---
title: PhysX Body
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


PhysX Body
==========


Turns an entity into a PhysX rigid body. This is the main component for creating physics objects. There are 3 types of rigid bodies: dynamic objects that have physics simulated on them, static objects that cannot move, and kinematic objects that can be moved programmatically but not by simulation. Requires `scene-options: physics`.

PhysX Body Attributes
----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|**type**|string; One of: ```['dynamic', 'static', 'kinematic']```|```'dynamic'```|Type of the rigid body to create. Dynamic can be moved by physics, Static cannot be moved, Kinematic can be moved programmatically.|No|
|**mass**|number|```1```|Total mass of the body.|No|
|**angularDamping**|number|```0```|If > 0, will set the rigid body's angular damping to reduce rotation over time.|No|
|**linearDamping**|number|```0```|If > 0, will set the rigid body's linear damping to reduce movement over time.|No|
|**emitCollisionEvents**|boolean|```False```|If set to true, it will emit 'contactbegin' and 'contactend' events when collisions occur.|No|
|**highPrecision**|boolean|```False```|If set to true, the object will receive extra attention by the simulation engine (at a performance cost).|No|
|**shapeOffset**|[vector3](vector3)|```{'x': 0, 'y': 0, 'z': 0}```|Offset applied to generated collision shapes.|No|
