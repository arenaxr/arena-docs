---
title: 
nav_order: 4
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


ARMarker
========


A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.

ARMarker Attributes
--------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|publish|Publish detections. Send detections to external agents (e.g. external builder script that places new markers in the scene). If dynamic=true and publish=true, object position is not updated (left up to external agent).|boolean|```False```|No|
|dynamic|Dynamic tag, not used for localization. E.g., to move object to which this ARMarker component is attached to. Requires permissions to update the scene (if dynamic=true).|boolean|```False```|No|
|ele|Tag elevation in meters.|number|```0```|No|
|lat|Tag latitude.|number|```0```|No|
|long|Tag longitude.|number|```0```|No|
|markerid|The marker id (e.g. for AprilTag 36h11 family, an integer in the range [0, 586])|string|```0```|Yes|
|markertype|The marker type (apriltag_36h11, lightanchor, uwb)|string; One of: ```['apriltag_36h11', 'lightanchor', 'uwb']```|```apriltag_36h11```|Yes|
|size|Tag size in millimeters|number|```150```|Yes|
|url|URL associated with the tag|string|```''```|No|
