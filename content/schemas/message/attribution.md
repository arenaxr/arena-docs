---
title: 
nav_order: 5
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Attribution
===========


Attribution Component. Saves attribution data in any entity.

Attribution Attributes
-----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|author|string|```'Unknown'```|Author name; e.g. “Vaptor-Studio”|No|
|authorURL|string||Author homepage/profile; e.g. https://sketchfab.com/VapTor|No|
|license|string|```'Unknown'```|License summary/short name; e.g. “CC-BY-4.0”.|No|
|licenseURL|string||License URL; e.g. http://creativecommons.org/licenses/by/4.0/|No|
|source|string|```'Unknown'```|Model source e.g. “Sketchfab”.|No|
|sourceURL|string||Model source URL; e.g. https://sketchfab.com/models/2135501583704537907645bf723685e7|No|
|title|string|```'No Title'```|Model title; e.g. “Spinosaurus”.|No|
|extractAssetExtras|boolean|```True```|Extract attribution info from asset extras; will override attribution info given (default: true)|No|