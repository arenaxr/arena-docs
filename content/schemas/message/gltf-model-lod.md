---
title: 
nav_order: 15
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


GLTF Model Level of Detail
==========================


Simple switch between the default gltf-model and a detailed one when a user camera is within specified distance

GLTF Model Level of Detail Attributes
--------------------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|detailedUrl|Alternative 'detailed' gltf model to load by URL|string|``````|No|
|detailedDistance|At what distance to switch between the models|number|```10```|No|
|updateRate|How often user camera is checked for LOD (default 333ms)|number|```333```|No|
|retainCache|Whether to skip freeing the detailed model from browser cache (default false)|boolean|```False```|No|
