---
title: Debug Visually
nav_order: 9.8
layout: tutorial
parent: Tutorial
---

# Debugging ARENA Web Browser Visually

When running programs in Python or Unity, you have a plethora of debug tools at your disposal to debug lines of code. For debugging the visual elements of rendered scenes, here are some other tools to help, and some guidance of where they are useful. Each tool has an expansive or limited capacity to display object messages (**Read Objects**), and add/change/delete object messages (**Write Objects**), as noted

| Visual Object Editors                                 | Format | Read Objects                                       | Write Objects                                      |
| ----------------------------------------------------- | ------ | -------------------------------------------------- | -------------------------------------------------- |
| [Python Console Interface](#python-console-interface) | MQTT   | <span style="color:green">All</span>               | <span style="color:red">None</span>                |
| [Build JSON](#build-json-page)                        | JSON   | <span style="color:green">All</span>               | <span style="color:green">All</span>               |
| [Build 3D](#build-3d)                                 | 3D     | <span style="color:green">All</span>               | <span style="color:green">All</span>               |
| [A-Frame Inspector](#a-frame-inspector)               | 3D     | <span style="color:green">All</span>               | <span style="color:red">None</span>                |
| [Unity Editor](#unity-editor)                         | 3D     | <span style="color:orange">Most</span><sup>1</sup> | <span style="color:green">All</span>               |
| [WebXR API Emulator](#webxr-api-emulator)             | 3D     | <span style="color:orange">Camera/Hands</span>     | <span style="color:orange">Camera/Hands</span>     |
| [AR Builder](#ar-builder)                             | 3D     | <span style="color:green">All</span>               | <span style="color:orange">Primitives/GLTFs</span> |

<sup>1</sup> The `arena-unity` library is still in development. Objects currently rendered are all Primitives, GLTFs, Lights, Lines, Text, Images. Others [still to be rendered](/content/schemas/render-support#rendering-support) are: PCD, Threejs, URDF, UI Panels, Gaussian Splat.<br/>

## Python Console Interface

There is a [console interface tutorial](/content/programs/debug) to the `arena-py` Python library. This is designed to have a way to inspect the program from the console, without having to send a heartbeat or write your own command/response interface.

<img src="/assets/img/programs/cli-interpreter.png" width="50%" />

## Build (JSON) Page

There is a [JSON scene build tutorial](/content/overview/build) for ARENA scenes. This is for editing persisted scene objects and configuration in JSON format with full support of all objects and their components.

<img src="/assets/img/overview/builder.png" width="50%" />

## Build 3D

There is a [Build 3D tutorial](/content/interface/debug#build-3d) for ARENA scenes using Build 3D. This is for editing persisted scene objects and configuration in 3D just as they would be on the 3D browser view. Build 3D leverages the A-Frame Inspector, with some critical differences, namely that changes are shared to other users.

<img src="/assets/img/examples/build3d.png" width="50%" />

## A-Frame Inspector

There is a [A-Frame Inspector tutorial](/content/interface/debug#a-frame-scene-inspector) for ARENA scenes using A-Frame Inspector. **NOTE: The default A-Frame Inspector does not publish MQTT updates. Any changes you make are local only.**

{% include alert type="warning" content="
A-Frame Inspector and Build 3D are similar, but operate critically differently. Learn to tell them apart: The A-Frame Inspector has **opaque black** control panels, and Build 3D has **transparent black** control panels.
"%}

<img src="/assets/img/overview/inspector.png" width="50%" />

## Unity Editor

There is a [Unity 3D scene editing tutorial](/content/unity/editor) for ARENA scenes. This is for editing persisted scene objects and configuration in 3D in a Unity rendering window.

<img src="/assets/img/unity/unity-desktop.png" width="50%" />

## WebXR API Emulator

Since ARENA's web view runs on WebXR, we can use the WebXR API Emulator to test Immersive VR (headset) features without a headset.

1. Go to the addon stores to install ([Firefox](https://addons.mozilla.org/firefox/addon/webxr-api-emulator), [Chrome](https://chrome.google.com/webstore/detail/webxr-api-emulator/mjddjgeghkdijejnciaefnkjmkafnnje))
1. Open your ARENA scene web view and the ARENA detects that you have a XR device (emulated) and it will let you enter the immersive (VR、AR) mode.
1. Open the `WebXR` tab in the browser developer tool ([Firefox](https://developer.mozilla.org/en-US/docs/Tools), [Chrome](https://developers.google.com/web/tools/chrome-devtools/)) to control the emulated devices. You can move the headset and controllers, and trigger the controller buttons.

<img src="/assets/img/overview/webxr-vr-emulator.png" width="50%" />

## AR Builder

We also have a Python program, [AR Builder (ARB)](/content/tools/authoring), which you can use to create and edit objects for your scene. You can use it in VR (virtual reality) as a way to edit your scene and save changes to the persistence database. Importantly, you can use it in AR (augmented reality) in combination with supported browsers and localization techniques to anchor scene objects in physical space. See our [section on miXed Reality (XR)](/content/xr) for details.

{% include alert type="note" title="note" content="
Check out the [Platforms Section](/content/xr/requirements) for details on browsers and platforms that support XR in ARENA.
" %}

In either case, ARB allows any user in the scene to edit, so it can be used collaboratively by multiple users remotely as VR, in person as AR, or as XR (miXed Reality), a combination of both.

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bYantKzkTFk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

{% include alert type="goal" content="
Use a tool like A-Frame Inspector to navigate a real-time ARENA scene graph and seek out an object to discover its properties and feel free to change them and observe the rendered changes.
"%}
