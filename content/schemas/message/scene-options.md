---
title: 
nav_order: 36
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Scene Options
=============


ARENA Scene Options

Scene Options Attributes
-------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|clickableOnlyEvents|true = publish only mouse events for objects with click-listeners; false = all objects publish mouse events|boolean|```True```|Yes|
|distanceModel|Algorithm to use to reduce the volume of the audio source as it moves away from the listener|string; One of: ```['exponential', 'inverse', 'linear']```|```'inverse'```|No|
|sceneHeadModels|Define the default head model(s) for the scene in a list. Users may still choose from the ARENA default list of head models as well.|array|```[]```|No|
|jitsiHost|Jitsi host used for this scene.|string|```'jitsi0.andrew.cmu.edu:8443'```|No|
|maxAVDist|Maximum distance between cameras/users until audio and video are cut off. For saving bandwidth on scenes with large amounts of user activity at once|number|```20```|Yes|
|navMesh|Navigation Mesh URL|string|```''```|No|
|networkedLocationSolver|ARMarker location solver parameter. By default (networkedLocationSolver=false) clients solve camera location locally when a static marker is detected. When true, publishes marker detections (to realm/g/a/camera-name) and defers all tag solving of client camera to a solver sitting on pubsub.|boolean|```False```|No|
|privateScene|false = scene will be visible; true = scene will not show in listings|boolean|```False```|Yes|
|refDistance|Distance at which the volume reduction starts taking effect|number|```1```|No|
|rolloffFactor|How quickly the volume is reduced as the source moves away from the listener|number|```1```|No|
|screenshare|Name of the 3D object used when sharing desktop|string|```'screenshare'```|No|
|videoFrustumCulling|If false, will disable video frustum culling (video frustum culling stops video from users outside of view)|boolean|```True```|Yes|
|videoDistanceConstraints|If false, will disable video distance constraints (video resolution decreases with distance from users in view)|boolean|```True```|Yes|
|volume|Volume for users in a scene|number|```1```|No|
|physics|If true, will load the aframe-physics-system. Required for the following: `dynamic-body`, `impulse`, `collision-listener`.|boolean|```False```|No|
