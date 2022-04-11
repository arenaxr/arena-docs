---
title: 
nav_order: 13
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Environment Presets
===================


A-Frame Environment presets. 

More properties at <a href='https://github.com/supermedium/aframe-environment-component'>https://github.com/supermedium/aframe-environment-component</a>

Environment Presets Attributes
-------------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|active|Show/hides the environment presets component. Use this instead of using the visible attribute.|boolean|```True```|Yes|
|dressing|Dressing is the term we use here for the set of additional objects that are put on the ground for decoration.|string; One of: ```['apparatus', 'arches', 'cubes', 'cylinders', 'hexagons', 'mushrooms', 'none', 'pyramids', 'stones', 'torii', 'towers', 'trees']```|```'none'```|No|
|dressingAmount|Number of objects used for dressing|number|```10```|No|
|dressingColor|Base color of dressing objects.|string|```'#795449'```|No|
|dressingOnPlayArea|Amount of dressing on play area.|number|```0```|No|
|dressingScale|Height (in meters) of dressing objects.|number|```5```|No|
|dressingUniformScale|If false, a different value is used for each coordinate x, y, z in the random variance of size.|boolean|```True```|No|
|dressingVariance|See: [Vector3](Vector3)|Vector3|```{'x': 1, 'y': 1, 'z': 1}```|No|
|flatShading|Whether to show everything smoothed (false) or polygonal (true).|boolean|```False```|No|
|fog|Amount of fog (0 = none, 1 = full fog). The color is estimated automatically.|number|```0```|No|
|grid|1x1 and 2x2 are rectangular grids of 1 and 2 meters side, respectively.|string; One of: ```['1x1', '2x2', 'crosses', 'dots', 'none', 'xlines', 'ylines']```|```'none'```|No|
|gridColor|Color of the grid.|string|```'#ccc'```|No|
|ground|Orography style.|string; One of: ```['canyon', 'flat', 'hills', 'noise', 'none', 'spikes']```|```'hills'```|No|
|groundColor|Main color of the ground.|string|```'#553e35'```|No|
|groundColor2|Secondary color of the ground. Used for textures, ignored if groundTexture is none.|string|```'#694439'```|No|
|groundScale|See: [Vector3](Vector3)|Vector3|```{'x': 1, 'y': 1, 'z': 1}```|No|
|groundTexture|Texture applied to the ground.|string; One of: ```['checkerboard', 'none', 'squares', 'walkernoise']```|```'none'```|No|
|groundYScale|Maximum height (in meters) of ground's features (hills, mountains, peaks..).|number|```3```|No|
|hideInAR|If true, hide the environment when entering AR.|boolean|```True```|No|
|horizonColor|Horizon Color|string|```'#ffa500'```|No|
|lighting|A hemisphere light and a key light (directional or point) are added to the scene automatically when using the component. Use none if you don't want this automatic lighting set being added. The color and intensity are estimated automatically.|string; One of: ```['distant', 'none', 'point']```|```'distant'```|No|
|lightPosition|See: [Vector3](Vector3)|Vector3|```{'x': 0, 'y': 1, 'z': -0.2}```|No|
|playArea|Radius of the area in the center reserved for the player and the gameplay. The ground is flat in there and no objects are placed inside.|number|```1```|No|
|preset|An A-frame preset environment.|string; One of: ```['arches', 'checkerboard', 'contact', 'default', 'dream', 'egypt', 'forest', 'goaland', 'goldmine', 'japan', 'none', 'osiris', 'poison', 'starry', 'threetowers', 'tron', 'volcano', 'yavapai']```|```'default'```|Yes|
|seed|Seed for randomization. If you don't like the layout of the elements, try another value for the seed.|number|```1```|No|
|shadow|Shadows on/off. Sky light casts shadows on the ground of all those objects with shadow component applied|boolean|```False```|No|
|shadowSize|Size of the shadow, if applied|number|```10```|No|
|skyColor|Sky Color|string|```'#ffa500'```|No|
|skyType|A sky type|string; One of: ```['atmosphere', 'color', 'gradient', 'none']```|```'color'```|No|
