---
title: Debug A-Frame
nav_order: 9
layout: tutorial
parent: Web Interface
---

# Debug A-Frame

Our ARENA deployment of A-Frame includes the A-Frame Inspector, which is a **local-only** scene editor, and useful to locate, observe, and test objects in ARENA scenes. We have added a wrapper application around A-Frame Inspector called Build 3D, which adds the ability to become a **remote distributed** scene editor.

Examine the list of elements on the left side. Each element or object you select will show it's details and attributes on the right side. You may edit any attributes here you wish, however, remember that the A-Frame Scene Inspector will not persist any changes to the persistence database. We do have a way to visually manipulate objects and save changes that we will share next.

## Build 3D

Build 3D is for editing persisted scene objects and configuration in 3D just as they would be on the 3D browser view. Build 3D leverages the A-Frame Inspector, with some critical differences, namely that changes are shared to other users.

Usage:

1. Enter on your example scene by clicking: expand settings (`v`), then the `3D Editor` link.
1. Optionally, you can enter from the JSON Build Page, clicking on the `Edit 3D` button to the right of any object in your list of scene objects.
1. Be sure to "Play" the scene to allow your ability to publish MQTT changes by clicking the Play (`▶`) button.
1. From this point, any changes you make, including add/remove objects/components, should be reflected in the bottom logging panel of MQTT publish events.
1. If you want to edit JSON from this view, an easy way back to JSON Build is to select the object, open the `build3d-mqtt-object` component, and toggle on `openJsonEditor`.
1. Exit by clicking the `Back to Scene` button. **Note: This will reload a new scene page.**

<img src="/assets/img/examples/build3d.png" width="50%" />

## A-Frame Scene Inspector

Since the ARENA's rendering uses the A-Frame web 3D rendering engine, you can open the [A-Frame Scene Inspector](https://aframe.io/docs/1.5.0/introduction/visual-inspector-and-dev-tools.html) on any scene to examine and manipulate any of the A-Frame elements in your scene.

Usage:

1. Enter on your example scene by typing `<ctrl> + <alt> + i` on most systems.
1. Exit by clicking the `Back to Scene` button.

<img src="/assets/img/overview/inspector.png" width="50%" />

## Help Commands

{% include alert type="tip" content="
While in the Build 3D or A-Frame Inspector views, press the `H` key to pull up a list of super-useful A-Frame Inspector commands.
"%}

<img src="/assets/img/overview/inspector-help.png" width="50%" />
