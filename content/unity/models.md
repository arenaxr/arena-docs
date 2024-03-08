---
title: Models
nav_order: 1.5
layout: default
parent: Unity Library
---

# Model Import and Export
Since the ARENA uses GLTF models as a web-friendly format, it is useful to know how to export your Unity work as a GLTF model, which the ARENA web can render.

## Importing GLTF With glTFast
GLTFs with urls stored as objects in the ARENA are automatically downloaded at Runtime (Play) and rendered with the help of the [glTFast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.2/manual/index.html) library. Decompression of GLTFs compressed with Draco, KTX, and Mesh Optimization are supported.

## Exporting GLTF With glTFast
In the `GameObject` and `Asset` menus, you can export your models as GLTF:
![/assets/img/unity/arena-unity-gltf-menu.png](/assets/img/unity/arena-unity-gltf-menu.png)
- Remote File & ARENA Object: choose `ARENA Export GLTF`.
- Local File: choose `Export glTF`.

There is also an advanced menu available to fine tune your ARENA export:

![/assets/img/unity/arena-unity-gltf-advanced.png](/assets/img/unity/arena-unity-gltf-advanced.png)

## Exporting GLTF With GLTF-Exporter
1. Use the [GLTF-Exporter](/content/3d-content/unity) package to export to GLTF file format.
1. Store this model online, like the on the [ARENA File Store](/content/interface/filestore) or [Dropbox](/content/overview/build#add-new-objects).
1. In scene  `ARENA View` [load your ARENA scene](/content/unity).
1. Import your model, adding an ARENA object using the menu `GameObject > ARENA > GLTF Model` and provide your model URL.
