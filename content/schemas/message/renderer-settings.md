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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|gammaFactor|number|```2.2```|Gamma factor (three.js default is 2.0; we use 2.2 as default)|No|
|localClippingEnabled|boolean|```False```|Defines whether the renderer respects object-level clipping planes|No|
|outputEncoding|string; One of: ```['BasicDepthPacking', 'GammaEncoding', 'LinearEncoding', 'LogLuvEncoding', 'RGBADepthPacking', 'RGBDEncoding', 'RGBEEncoding', 'RGBM16Encoding', 'RGBM7Encoding', 'sRGBEncoding']```|```'sRGBEncoding'```|Defines the output encoding of the renderer (three.js default is LinearEncoding; we use sRGBEncoding as default)|Yes|
|physicallyCorrectLights|boolean|```False```|Whether to use physically correct lighting mode.|No|
|sortObjects|boolean|```True```|Defines whether the renderer should sort objects|No|
