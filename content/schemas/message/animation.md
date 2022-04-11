---
title: 
nav_order: 1
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Animation
=========


Animate and tween values. 

More properties at <a href='https://aframe.io/docs/1.3.0/components/animation.html'>https://aframe.io/docs/1.3.0/components/animation.html</a>

Animation Attributes
---------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|autoplay|Whether or not the animation should autoplay. Should be specified if the animation is defined for the animation-timeline component (currently not supported).|boolean|```True```|No|
|delay|How long (milliseconds) to wait before starting.|number|```0```|No|
|dir|Which dir to go from from to to.|string; One of: ```['normal', 'alternate', 'reverse']```|```'normal'```|No|
|dur|How long (milliseconds) each cycle of the animation is.|number|```1000```|No|
|easing|Easing function of animation. To ease in, ease out, ease in and out.|string|```'easeInQuad'```|No|
|elasticity|How much to bounce (higher is stronger).|number|```400```|No|
|enabled|If disabled, animation will stop and startEvents will not trigger animation start.|boolean|```True```|No|
|from|Initial value at start of animation. If not specified, the current property value of the entity will be used (will be sampled on each animation start). It is best to specify a from value when possible for stability.|string|```''```|No|
|isRawProperty|Flag to animate an arbitrary object property outside of A-Frame components for better performance. If set to true, for example, we can set property to like components.material.material.opacity. If property starts with components or object3D, this will be inferred to true.|boolean|```False```|No|
|loop|How many times the animation should repeat. If the value is true, the animation will repeat infinitely.|number|```0```|No|
|pauseEvents|Comma-separated list of events to listen to trigger pause. Can be resumed with resumeEvents.|array|```[]```|No|
|property|Property to animate. Can be a component name, a dot-delimited property of a component (e.g., material.color), or a plain attribute.|string||No|
|resumeEvents|Comma-separated list of events to listen to trigger resume after pausing.|array|```[]```|No|
|round|Whether to round values.|boolean|```False```|No|
|startEvents|Comma-separated list of events to listen to trigger a restart and play. Animation will not autoplay if specified. startEvents will restart the animation, use pauseEvents to resume it. If there are other animation components on the entity animating the same property, those animations will be automatically paused to not conflict.|array|```[]```|No|
|to|Target value at end of animation.|string|```''```|No|
|type|Right now only supports color for tweening isRawProperty color XYZ/RGB vector values.|string|```''```|No|
