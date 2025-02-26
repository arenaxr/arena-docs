---
title: GLTF Morph
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


GLTF Morph
==========


Allows you to target and control a gltf model's morphTargets created in Blender. Requires `object_type: gltf-model`.

More properties at <a href='https://github.com/elbobo/aframe-gltf-morph-component'>A-Frame GLTF Morph</a> component.

GLTF Morph Attributes
----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|**morphtarget**|string|```''```|Name of morphTarget, can be found as part of the GLTF model.|Yes|
|**value**|number|```0```|Value that you want to set that morphTarget to (0 - 1).|Yes|
