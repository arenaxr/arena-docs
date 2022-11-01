---
title: 
nav_order: 28
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Material extras
===============


Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. 

More properties at <a href='https://threejs.org/docs/#api/en/materials/Material'>https://threejs.org/docs/#api/en/materials/Material</a>

Material extras Attributes
---------------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|encoding|string; One of: ```['LinearEncoding', 'sRGBEncoding', 'GammaEncoding', 'RGBEEncoding', 'LogLuvEncoding', 'RGBM7Encoding', 'RGBM16Encoding', 'RGBDEncoding', 'BasicDepthPacking', 'RGBADepthPacking']```|```sRGBEncoding```|encoding|No|
|needsUpdate|boolean|```False```|needsUpdate|No|
|render-order|number|```1```|This value allows the default rendering order of scene graph objects to be overridden.|No|
|colorWrite|boolean||Whether to render the material’s color|No|
|transparentOccluder|boolean||If true, will set colorWrite=false and renderOrder=0 to make the material a transparent occluder.|No|
|defaultRenderOrder|number||Used as the renderOrder when transparentOccluder is reset to false.|No|
