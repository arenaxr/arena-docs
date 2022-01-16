---
title: Exporting from Unity
layout: default
parent: 3D Content
---

# Exporting from Unity

There are some limitations and things to keep in mind when exporting from [Unity](https://unity.com). A plugin like [GLTF Exporter](https://github.com/Plattar/gltf-exporter) can be useful with the following guidance.

1. In order to optimize load times, reduce file sizes and increase frame rates, all meshes with same material should be combined into single mesh.
1. Meshes should be compressed by reducing floating point accuracy and decimating mesh polygon count.
1. Textures should be also be combined to single atlased "large" compressed textures as opposed to multiple single texture in either PNG or JPG. This reduces load time significantly and reduces the change of material application error in ARENA.
1. Normal maps are supported; however other more complex shaders are not supported.
1. Unity Lightmaps are not supported. It is possible to bake approximate lightmaps directly onto diffuse textures to create "fake" shadows.
1. Unity real time lights do not appear to be exported. Real time lights should be recreated in ARENA.
1. It is possible to export transparent materials.
1. It is possible to export animated models from Unity. Animated models in Unity should be set to "Legacy" mode with compressed keyframes. All animations must be contained and combined within the same model for animation export to work. Separated animation and model files do not work (Unity FBX convention is to separate mesh from animation files, so significant animation+mesh reprocessing may be required for proper animation export to GLTF.)
