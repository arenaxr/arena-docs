---
title: Coordinate System Map
layout: default
parent: 3D Content
---

#  Coordinate System Map

Since the ARENA is a synchronization system, in part, across a number of 3d rendering platforms and model systems, it is useful to note how different each system orients itself. In some cases these platforms have adjusted import and export of models to account for the differences, between ARENA-Web (A-frame) and ARENA-Unity, we try to do most conversions in Unity, and let A-frame standardize our wire format.

## Y-Axis Up-Down Systems

Noted in terms of X, Y, Z order of positive axis:
- X (Right, Left)
- Y (Up, Down)
- Z (Forward, Back)

Y Up Platforms:
- RUB - OpenGL, three.js, A-frame, SPZ ([ARENA-Web Coordinates](/content/xr/optical-markers#coordinate-system))
- LUF - GLTF, GLB
- RUF - Unity
- RDF - PLY

## Z-Axis Up-Down Systems

Noted in terms of X, Y, Z order of positive axis:
- X (Right, Left)
- Y (Forward, Back)
- Z (Up, Down)

Z Up Platforms:
- RFU - Blender
- RBU - Unreal Engine
