---
title: Cross Platform Support
nav_order: 4
layout: default
parent: Architecture
---

# Cross Platform Support

A core component of the ARENA is an environment to view and interact in virtual and augmented reality. This environment was built using Web standards (notably, WebXR and WebGL) and frameworks for building 3D scenes and AR/VR environments (three.js and A-Frame). This allows ARENA content to be view on a number of platforms ranging from standard web browsers on desktop computers and VR headsets (desktop browsers, FireFox Reality for VR headsets, Oculus Browser for VR headsets), on phones / tablets with passthrough AR (FireFox WebXR Viewer, Chrome) and wearable AR headsets (Hololens Edge Browser, Magic Leap Lumin Browser). All of these devices can interact in a multi-user manner with a consistent scene. In order to prototype the needs for future browser platforms, we are maintaining a custom WebXR version of Firefox for iOS that is able to perform local image processing as well as 3D click I/O events. We also plan to integrate the ARENA with systems developed to aid coordinating mobile teams (of first responders, firefighters, police) in real-time .

![img](../../assets/img/arena-stack.png)

**Figure 3**. ARENA Browser Stack