---
title: Optical Markers
nav_order: 1
layout: default
parent: Mixed Reality
---

In general, ARENA requires a WebXR-compatible browser, which currently include [Edge (desktop), Chrome (desktop and mobile), Firefox (desktop and mobile; not enabled by default)](https://caniuse.com/webxr), among others. Note that these include browsers that can be run in many headsets. For example, oculus and magic leap's browsers are based on the open source codebase of Chrome (Chromium).

In order to prototype the needs for future browser platforms, we are maintaining a custom Browser version of Firefox for iOS (based of [WebXRViewer](https://apps.apple.com/us/app/webxr-viewer/id1295998056)) which supports a custom computer vision pipeline

 is able to perform local image processing as well as 3D click I/O events.


### WebXRViewer
The AprilTag detection requires that the browser supports computer vision while in AR mode using [WebXR](https://immersiveweb.dev/). Currently, the only browser with such support is the experimental browser from Mozilla [WebXRViewer](https://apps.apple.com/us/app/webxr-viewer/id1295998056).

After installing WebXRViewer, go to 'Settings -> XRViewer' and change:

**WebXR Polyfill URL**:  ```https://arenaxr.org/webxrios.js``` or ```https://arenaxr.org/vendor/webxr-webxrviewer-ios.js```

**Always Allow World Sensing**:```Yes```

![img](../../assets/img/localization/webxrviewer-settings.png)

### Use the device in portrait orientation

The ARENA localization solver assumes that the device is in portrait orientation, and **we recommend locking the device to portrait orientation**. The picture below shows a scene with a blue box at the origin; while not visible, the blue box is overlayed on an AprilTag with ID 0.

![img](../../assets/img/localization/portrait.png)
