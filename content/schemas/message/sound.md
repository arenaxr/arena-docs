---
title: 
nav_order: 38
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Positional Sound
================


The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. 

More properties at <a href='https://aframe.io/docs/1.3.0/components/sound.html'>https://aframe.io/docs/1.3.0/components/sound.html</a>

Positional Sound Attributes
----------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|autoplay|Whether to automatically play sound once set.|boolean|```False```|No|
|distanceModel|Sound model: linear, inverse, or exponential.|string; One of: ```['linear', 'inverse', 'exponential']```|```'inverse'```|No|
|loop|Whether to loop the sound once the sound finishes playing.|boolean|```False```|No|
|maxDistance|Maximum distance between the audio source and the listener, after which the volume is not reduced any further.|number|```10000```|No|
|on|An event for the entity to listen to before playing sound.|string; One of: ```['mousedown', 'mouseup', 'mouseenter', 'mouseleave', 'triggerdown', 'triggerup', 'gripdown', 'gripup', 'menudown', 'menuup', 'systemdown', 'systemup', 'trackpaddown', 'trackpadup']```|```'mousedown'```|No|
|poolSize|Numbers of simultaneous instances of this sound that can be playing at the same time|number|```1```|No|
|positional|Whether or not the audio is positional (movable).|boolean|```True```|No|
|refDistance|Reference distance for reducing volume as the audio source moves further from the listener.|number|```1```|No|
|rolloffFactor|Describes how quickly the volume is reduced as the source moves away from the listener.|number|```1```|No|
|src|URL path to sound file e.g. 'store/users/wiselab/sound/wave.mp3'|string||No|
|volume|How loud to play the sound|number|```1```|No|
