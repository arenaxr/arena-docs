---
title: Panoramic Rooms
nav_order: 6
layout: tutorial
parent: Overview
---

# Panoramic Video Rooms

You can use the ARENA to setup a 360° panoramic streaming video room, or several rooms with a video camera like the 360° Ricoh [Theta Z1](https://theta360.com/en/about/theta/z1.html) or [Theta X](https://theta360.com/en/about/theta/x.html).

## General Performance Requirements

To ensure the upload of the 360 video stream isn't diminished before other users get a chance to download it, each 360 camera should have:

- A **fast computer**. This is a little hard to measure, but slower computers will diminish the video upload. We've had good results with the MacBook Pro M1 chip.
- A **wired network connection** of at least 1Gbps since we need to make sure our upload of the 360 video stream has as much bandwidth as possible and without the variable instability of wireless connections.
- Optimally a **2K output stream** from the camera so detail renders well, higher outputs like 4K may work, but it's untested.
- Google **Chrome** or Microsoft **Edge**. Firefox and other browsers have trouble ingesting the 2:1 video ratio required. Check the `A/V Setup` screen when entering the scene for strange visual artifacts.
- ARENA Web Core [**version 1.11**](https://arenaxr.org/conf/versions.html) or higher.
- Shutdown and close any unnecessary applications and browser tabs.
- Do not stream more than one camera per computer.

## Setup World Single Panoramic Room

Setup a scene where the 360 video stream encompasses the entire world, and while other users can move in it, the "walls" of the video are 5000 meters away, so even if users move, the `videosphere` walls appear to stay in place. This 5000 meter radius is the default for a `videosphere` object.

<img src="/assets/img/overview/videosphere1.png"/>

1. In [Build](/content/overview/build), add a `videosphere` object.
1. Add the `jitsi-video` attribute to the `videosphere` object.
1. Add a displayName for the `jitsi-video` attribute. The JSON should look like this:
   ```json
   {
     "object_id": "my-videosphere-object",
     "persist": true,
     "type": "object",
     "action": "update",
     "data": {
       "object_type": "videosphere",
       "position": {
         "x": 0,
         "y": 0,
         "z": 0
       },
       "rotation": {
         "x": 0,
         "y": 0,
         "z": 0
       },
       "radius": 5000,
       "jitsi-video": {
         "displayName": "360 cam"
       }
     }
   }
   ```
1. Remove the ground and sky effects from your scene, your world scale `videosphere` replaces them.
1. To do this, add a `scene-options` object if you don't already have one and remove the environment presets by adding attributes that override the default theme, sky, and ground:
   ```json
   {
     "object_id": "scene-options",
     "persist": true,
     "type": "scene-options",
     "action": "update",
     "data": {
       "env-presets": {
         "active": true,
         "preset": "none",
         "ground": "none",
         "skyType": "none"
       },
       "scene-options": {
         ...
       }
     }
   }
   ```
1. Follow [Connect the 360 camera to the ARENA.](#connect-360-camera-to-arena) at the end of this page.

## Setup Digital Twin Single Panoramic Room

Match a `videosphere` to a space in a scanned model of a space or room. Users may feel like they are joining you live and can enter and leave a "streaming" room.

<img src="/assets/img/overview/videosphere2.png"/>

1. Camera position is important. You may want to mount the camera lens in the exact center of the room, on a table or tripod or both.
1. Assumption: you already have a [scanned room/space](/content/3d-content/scaniverse) converted to GLB and loaded into the ARENA.
1. In [Build](/content/overview/build), add a `videosphere` object similar to [`Setup World Single Panoramic Room`](#world-single-panoramic-room) but with some crucial differences.
1. Add a displayName for the `jitsi-video` attribute, but also you are going to scale down this `videosphere` to the size and position of your room to match your scanned model.

   - Our conference room is a small 5x7 meters and 3 meters high, not a perfect cube, so we'll position it at the center of the scanned room model at position x=2.7, z=-3.6, which matches the position of the camera in reality.
   - We'll set the height of the sphere at position y=2, which matches the real position of the the camera lens in the room at 2 meters.
   - At the position we've mounted the camera we are 90 degrees off the model, so we can set rotation of the sphere at y=-90.
   - We want the outside edge of the sphere wall to just graze the shortest longitudinal axis of the room to not miss any of the movement of the people in the room, so we will set the radius at 2.5 meters since we are in the center between the shortest wall of 5 meters.

   ```json
   {
     "object_id": "360-conference-room4",
     "persist": true,
     "type": "object",
     "action": "update",
     "data": {
       "object_type": "videosphere",
       "position": {
         "x": 2.7,
         "y": 2,
         "z": -3.6
       },
       "rotation": {
         "x": 0,
         "y": -90,
         "z": 0
       },
       "radius": 2.5,
       "jitsi-video": {
         "displayName": "Conference Room 4"
       }
     }
   }
   ```

1. Leave the ground and sky effects from your scene intact, you will need them for context.
1. Follow [Connect the 360 camera to the ARENA.](#connect-360-camera-to-arena) and the end of this page.

## Setup Digital Twin Multiple Panoramic Rooms

Repeat the instructions for `Setup Digital Twin Single Panoramic Room`, just make sure you give each camera a different `Display Name` and make sure each `videosphere` object has that unique `Display Name` in it's `jitsi-video` attribute.

## Connect 360 Camera to ARENA

1. Connect the 360 camera to the computer and start the camera's "live stream".
1. Open the scene in Chrome/Edge and select the 360 camera on the `A/V Setup` dialog and you should see a 2:1 radio preview of the video stream.
1. Make sure your `Display Name` on the `A/V Setup` dialog is the same as the `displayName` of the `jitsi-video` attribute above.
1. `Enter Scene`, and the scene will appear white, then black if you wait.
1. Click the camera button in the upper right corner of the browser and you should see a preview again, as well as the video displayed on the "walls" of the 3d sphere.
1. Click the microphone button if you want.
