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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|detailedUrl|string|``````|Alternative 'detailed' gltf model to load by URL|No|
|detailedDistance|number|```10```|At what distance to switch between the models|No|
|updateRate|number|```333```|How often user camera is checked for LOD (default 333ms)|No|
|retainCache|boolean|```False```|Whether to skip freeing the detailed model from browser cache (default false)|No|