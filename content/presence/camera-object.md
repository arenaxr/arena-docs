---
title: Camera Objects
nav_order: 5
layout: default
parent: Presence
---

# Camera Objects

## 3d Head Model

By default the ARENA shows your location as a 3d model of a head, with your nose at your location coordinates. If you want to change this, it is available in the scene addressable by an object_id based on your (camera) name, e.g `head-model_camera_1234_er1k` or if you set your name manually in the URL parameter `&fixedCamera=name` as `head-model_camera_name_name`. You can also change the text above your head, which defaults to the last part of your automatically assigned or fixedCamera name (after the underscore). So by default it would appear as `er1k` in the examples above, but can be modified by MQTT message addressed to object_id `head-text_camera_er1k_er1k`.

## Vive (laser) controls

We've noticed the controllers don't show up in the scene unless they both - and EVERYTHING else for SteamVR - are all working (headset, lighthouses). And sometimes you have to restart SteamVR for hand controllers to show up in the scene; even though SteamVR shows them as being working/on/available/etc., it's possible to open VR mode in an Arena scene and be missing the hand controls.

By default we use A-Frame 'laser-controls' which default to showing Valve Index controller 3D models (gray, circular), even if we are using (equivalent) Vive controllers (black, paddle shaped, not included in the list of controllers known to A-Frame).
