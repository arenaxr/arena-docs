---
title: 
nav_order: 32
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Renderer Settings
=================


These settings are fed into three.js WebGLRenderer properties

Renderer Settings Attributes
-----------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|gammaFactor|Gamma factor (three.js default is 2.0; we use 2.2 as default)|number|```2.2```|No|
|localClippingEnabled|Defines whether the renderer respects object-level clipping planes|boolean|```False```|No|
|outputEncoding|Defines the output encoding of the renderer (three.js default is LinearEncoding; we use sRGBEncoding as default)|string; One of: ```['BasicDepthPacking', 'GammaEncoding', 'LinearEncoding', 'LogLuvEncoding', 'RGBADepthPacking', 'RGBDEncoding', 'RGBEEncoding', 'RGBM16Encoding', 'RGBM7Encoding', 'sRGBEncoding']```|```'sRGBEncoding'```|Yes|
|physicallyCorrectLights|Whether to use physically correct lighting mode.|boolean|```False```|No|
|sortObjects|Defines whether the renderer should sort objects|boolean|```True```|No|
