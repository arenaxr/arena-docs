---
title: Camera Objects
nav_order: 5
layout: default
parent: Presence
---

# Camera Objects

## Camera
(from [A-Frame documentation](https://aframe.io/docs/1.0.0/components/camera.html))

| The camera component defines from which perspective the user views the scene. The camera is commonly paired with controls components that allow input devices to move and rotate the camera.

| A camera should usually be positioned at the average height of human eye level (1.6 meters). When used with controls that receive rotation or position (e.g. from a VR device) this position will be overridden.

```html
  <a-entity camera look-controls position="0 1.6 0"></a-entity>
```

The above example puts the camera at a position in the scene, but sure enough, when we use a tablet + WebXRViewer or a VR or AR headset, these values are overwritten. IN FACT it turns out that from a desktop browser, at the start of our A-Frame session, regardless of the values set in the HTML above, the start position is set to (0, 1.6, 0). It was misleading that the HTML definition just happened to match. Our code sets it to (0,0,0) in the declaration. It gets more interesting: on a tablet or phone, the start position again gets overridden - by (0,0,0) this time!

| When moving or rotating the camera relative to the scene, use a camera rig. By doing so, the camera’s height offset can be updated by room-scale devices, while still allowing the tracked area to be moved independently around the scene.

```html
  <a-entity id="rig" position="25 10 0">
    <a-entity id="camera" camera look-controls></a-entity>
  </a-entity>
```

## 3d Head Model

By default the ARENA shows your location as a 3d model of a head, with your nose at your location coordinates. If you want to change this, it is available in the scene addressable by an object_id based on your (camera) name, e.g `head-model_camera_1234_er1k` or if you set your name manually in the URL parameter `&fixedCamera=name` as `head-model_camera_name_name`. You can also change the text above your head, which defaults to the last part of your automatically assigned or fixedCamera name (after the underscore). So by default it would appear as `er1k` in the examples above, but can be modified by MQTT message addressed to object_id `head-text_camera_er1k_er1k`.

## Vive (laser) controls

We've noticed the controllers don't show up in the scene unless they both - and EVERYTHING else for SteamVR - are all working (headset, lighthouses). And sometimes you have to restart SteamVR for hand controllers to show up in the scene; even though SteamVR shows them as being working/on/available/etc., it's possible to open VR mode in an Arena scene and be missing the hand controls.

By default we use A-Frame 'laser-controls' which default to showing Valve Index controller 3D models (gray, circular), even if we are using (equivalent) Vive controllers (black, paddle shaped, not included in the list of controllers known to A-Frame).
