---
title: 
nav_order: 26
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Material
========


The material properties of the object’s surface. 

More properties at <a href='https://aframe.io/docs/1.3.0/components/material.html'>https://aframe.io/docs/1.3.0/components/material.html</a>

Material Attributes
--------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|alphaTest|number|```0```|Alpha test threshold for transparency.|No|
|blending|string; One of: ```['none', 'normal', 'additive', 'subtractive', 'multiply']```|```'normal'```|The blending mode for the material’s RGB and Alpha sent to the WebGLRenderer. Can be one of none, normal, additive, subtractive or multiply|No|
|color|string|```'#7f7f7f'```|Base diffuse color.|No|
|depthTest|boolean|```True```|Whether depth testing is enabled when rendering the material.|No|
|dithering|boolean|```True```|Whether material is dithered with noise. Removes banding from gradients like ones produced by lighting.|No|
|flatShading|boolean|```False```|Use THREE.FlatShading rather than THREE.StandardShading.|No|
|npot|boolean|```False```|Use settings for non-power-of-two (NPOT) texture.|No|
|offset|object|```{'x': 1, 'y': 1}```|Texture offset to be used.|No|
|opacity|number|```1```|Extent of transparency. If the transparent property is not true, then the material will remain opaque and opacity will only affect color.|No|
|repeat|object|```{'x': 1, 'y': 1}```|Texture repeat to be used.|No|
|shader|string|```'standard'```|Which material to use. Defaults to the standard material. Can be set to the flat material or to a registered custom shader material.|No|
|side|string; One of: ```['front', 'back', 'double']```|```'front'```|Which sides of the mesh to render. Can be one of front, back, or double.|No|
|src|string||URI, relative or full path of an image/video file. e.g. 'store/users/wiselab/images/360falls.mp4'|No|
|transparent|boolean|```False```|Whether material is transparent. Transparent entities are rendered after non-transparent entities.|No|
|vertexColors|string; One of: ```['none', 'vertex', 'face']```|```'none'```|Whether to use vertex or face colors to shade the material. Can be one of none, vertex, or face.|No|
|visible|boolean|```True```|Whether material is visible. Raycasters will ignore invisible materials.|No|