---
title: Debug Visually
nav_order: 8
layout: tutorial
parent: Overview
---

# Debugging ARENA Web Browser Visually

When running programs in Python or Unity, you have a plethora of debug tools at your disposal to debug lines of code. For debugging the visual elements of the Browser view, here are some other tools to help.

## Debug your scene with A-Frame Scene Inspector

Since the ARENA's rendering uses the A-Frame web 3D rendering engine, you can open the [A-Frame Scene Inspector](https://aframe.io/docs/1.4.0/introduction/visual-inspector-and-dev-tools.html) on any scene to examine and manipulate any of the A-Frame elements in your scene. Try this now from your example scene by typing `<ctrl> + <alt> + i` on most systems.

Examine the list of elements on the left side. Each element or object you select will show it's details and attributes on the right side. You may edit any attributes here you wish, however, remember that the A-Frame Scene Inspector will not persist any changes to the persistence database. We do have a way to visually manipulate objects and save changes that we will share next.

![](../../../assets/img/overview/inspector.png)

{% include alert type="tip" content="
While in the A-Frame Inspector view, press the `H` key to pull up a list of super-useful A-Frame Inspector commands.
"%}

![](../../../assets/img/overview/inspector-help.png)

## WebXR API Emulator

Since ARENA's web view runs on WebXR, we can use the ebXR API Emulator to test Immersive VR (headset) features without a headset.

1. Go to the addon stores to install ([Firefox](https://addons.mozilla.org/firefox/addon/webxr-api-emulator), [Chrome](https://chrome.google.com/webstore/detail/webxr-api-emulator/mjddjgeghkdijejnciaefnkjmkafnnje))
1. Open your ARENA scene web view and the ARENA detects that you have a XR device (emulated) and it will let you enter the immersive (VR、AR) mode.
1. Open the `WebXR` tab in the browser developer tool ([Firefox](https://developer.mozilla.org/en-US/docs/Tools), [Chrome](https://developers.google.com/web/tools/chrome-devtools/)) to control the emulated devices. You can move the headset and controllers, and trigger the controller buttons.

![WebXR tab](../../../assets/img/overview/webxr-vr-emulator.png)

## AR Builder, visual content authoring

We also have a Python program, [AR Builder (ARB)](../tools/authoring), which you can use to create and edit objects for your scene. You can use it in VR (virtual reality) as a way to edit your scene and save changes to the persistence database. Importantly, you can use it in AR (augmented reality) in combination with supported browsers and localization techniques to anchor scene objects in physical space. See our [section on miXed Reality (XR)](../xr) for details.

{% include alert type="note" title="note" content="
Check out the [Platforms Section](/content/xr/requirements) for details on browsers and platforms that support XR in ARENA.
" %}

In either case, ARB allows any user in the scene to edit, so it can be used collaboratively by multiple users remotely as VR, in person as AR, or as XR (miXed Reality), a combination of both.

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bYantKzkTFk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
