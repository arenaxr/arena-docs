---
title: Function Definitions
nav_order: 5
layout: default
parent: Messaging Format
---

# Messaging Format Function Definitions

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

## Camera
(from A-Frame documentation)

The camera component defines from which perspective the user views the scene. The camera is commonly paired with controls components that allow input devices to move and rotate the camera.

A camera should usually be positioned at the average height of human eye level (1.6 meters). When used with controls that receive rotation or position (e.g. from a VR device) this position will be overridden.
```html
<a-entity camera look-controls position="0 1.6 0"></a-entity>
```
  - The above example puts the camera at a position in the scene, but sure enough, when we use a tablet+WebXRViewer or a VR or AR headset, these values are overwritten. IN FACT it turns out that from a desktop browser, at the start of our A-Frame session, regardless of the values set in the HTML above, the start position is set to (0, 1.6, 0). It was misleading that the HTML definition just happened to match. Our code sets it to (0,0,0) in the declaration. It gets more interesting: on a tablet or phone, the start position again gets overridden - by (0,0,0) this time!

When moving or rotating the camera relative to the scene, use a camera rig. By doing so, the camera’s height offset can be updated by roomscale devices, while still allowing the tracked area to be moved independently around the scene.
```html
<a-entity id="rig" position="25 10 0">
  <a-entity id="camera" camera look-controls></a-entity>
</a-entity>
```
