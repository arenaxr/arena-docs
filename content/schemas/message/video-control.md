---
title: 
nav_order: 48
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Video
=====


Video Control

Video Attributes
-----------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|frame_object|string||URL of a thumbnail image, e.g. 'store/users/wiselab/images/conix-face-white.jpg'|Yes|
|video_object|string||Name of object where to put the video, e.g. 'square_vid6'|Yes|
|video_path|string||URL of the video file, e.g. 'store/users/wiselab/videos/kungfu.mp4'|Yes|
|anyone_clicks|boolean|```True```|Responds to clicks from any user|No|
|video_loop|boolean|```True```|Video automatically loops|No|
|autoplay|boolean|```False```|Video starts playing automatically|No|
|volume|number|```1```|Video sound volume|No|