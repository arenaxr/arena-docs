---
title: 
nav_order: 0
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Animation Mixer
===============


A list of available animations can usually be found by inspecting the model file or its documentation. All animations will play by default. To play only a specific set of animations, use wildcards: animation-mixer='clip: run_*'. 

More properties at <a href='https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation'>https://github.com/n5ro/aframe-extras/tree/master/src/loaders#animation</a>

Animation Mixer Attributes
---------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|clampWhenFinished|If true, halts the animation at the last frame.|boolean|```False```|No|
|clip|Name of the animation clip(s) to play. Accepts wildcards.|string|```'*'```|No|
|crossFadeDuration|Duration of cross-fades between clips, in seconds.|number|```0```|No|
|duration|Duration of the animation, in seconds (0 = auto).|number|```0```|No|
|repetitions|Number of times to play the clip, in addition to the first play. Repetitions are ignored for loop: once.|number; One of: ```['once', 'repeate', 'pingpong']```|```0```|No|
|timeScale|Scaling factor for playback speed. A value of 0 causes the animation to pause. Negative values cause the animation to play backwards.|number|```1```|No|
