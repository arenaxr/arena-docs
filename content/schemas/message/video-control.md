---
title: 
nav_order: 46
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Video
=====


Video Control

Video Attributes
-----------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|frame_object|URL of a thumbnail image, e.g. 'store/users/wiselab/images/conix-face-white.jpg'|string||Yes|
|video_object|Name of object where to put the video, e.g. 'square_vid6'|string||Yes|
|video_path|URL of the video file, e.g. 'store/users/wiselab/videos/kungfu.mp4'|string||Yes|
|anyone_clicks|Responds to clicks from any user|boolean|```True```|No|
|video_loop|Video automatically loops|boolean|```True```|No|
|autoplay|Video starts playing automatically|boolean|```False```|No|
|volume|Video sound volume|number|```1```|No|
