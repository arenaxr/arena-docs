---
title: GLTF Files
nav_order: 5
layout: default
parent: 3D Content
---

# GLTF Files

Here are some notes to help you convert GLTF models used in the ARENA.

## Sketchfab
[Sketchfab](https://sketchfab.com/3d-models) GLTF models don't always come in convenient single .glb files. Sometimes they consist of a main .gltf file that refers to several textures and other files in a textures/ folder and .glb file. And to make matters worse, the default name is scene.gltf. But if you put everything from the download into a folder of it's own, you can keep it separate from other scene.gltf files, and they will find the right files through relative paths. For example
```shell
ls /var/www/html/models/nara
scene.bin  scene.gltf  textures
```

## SketchUp
Getting from [SketchUp](https://www.sketchup.com/) to GLTF is a bit of an adventure:
- The online converters don’t generate valid GLTFs.
- The SketchUp GLTF export plugin was written for SketchUp 2016 and seems to hang SketchUp 2020 — these models were created in SketchUp 2017, so the 2016 version refuses to open them.
- What worked was installing Adobe Dimension, opening the SketchUp file there, and exporting it.

Dimension doesn’t seem to edit these models well, so if you want to patch up some textures, it's recommended to do that in SketchUp first, then saving a copy, using Dimension to convert to GLTF.

## GLTF Viewer
Drag-and-drop preview tool for glTF 2.0 3D models: [https://gltf-viewer.donmccurdy.com/](https://gltf-viewer.donmccurdy.com/).

## ARENA 3D models

Here are some ready-to-use models on the `andrew.andrew.cmu.edu` server, accessible with the `models/modelname.glb` path:

|------------------------------:|-------------------------:|-----------------------------:|----------------------------:|---------------:|
|2CylinderEngine.glb            |Cameras.gltf              |MultiUVTest.glb               |TriangleWithoutIndices.gltf  |hat2.glb|
|2CylinderEngine.gltf           |CesiumMan.glb             |MultiUVTest.gltf              |TwoSidedPlane.gltf           |helios|
|AlphaBlendModeTest.glb         |CesiumMan.gltf            |NormalTangentMirrorTest.glb   |UnlitTest.glb                |hololens.glb|
|AlphaBlendModeTest.gltf        |CesiumMilkTruck.glb       |NormalTangentMirrorTest.gltf  |UnlitTest.gltf               |izzy|
|AnimatedCube.gltf              |CesiumMilkTruck.gltf      |NormalTangentTest.glb         |VC.glb                       |marcus2.glb|
|AnimatedMorphCube.glb          |Corset.glb                |NormalTangentTest.gltf        |VC.gltf                      |marcus3.glb|
|AnimatedMorphCube.gltf         |Corset.gltf               |OrientationTest.glb           |VertexColorTest.glb          |monkey|
|AnimatedMorphSphere.glb        |Court.glb                 |OrientationTest.gltf          |VertexColorTest.gltf         |nara|
|AnimatedMorphSphere.gltf       |Cube.gltf                 |Plane.mtl                     |WaterBottle.glb              |nuno.glb|
|AnimatedTriangle.gltf          |Cube.mtl                  |Plane.obj                     |WaterBottle.gltf             |palm|
|AntiqueCamera.glb              |Cube.obj                  |ReciprocatingSaw.glb          |anthony.glb                  |peacock|
|AntiqueCamera.gltf             |DamagedHelmet.glb         |ReciprocatingSaw.gltf         |avocadoman                   |rearbody.mtl|
|Avocado.glb                    |DamagedHelmet.gltf        |RiggedFigure.glb              |baby_yoda                    |rearbody.obj|
|Avocado.gltf                   |Drone.glb                 |RiggedFigure.gltf             |body.mtl                     |rhetoritician|
|BarramundiFish.glb             |Duck.glb                  |RiggedSimple.glb              |body.obj                     |scene.bin|
|BarramundiFish.gltf            |Duck.gltf                 |RiggedSimple.gltf             |cat                          |skull|
|BoomBox.glb                    |Earth.glb                 |Scene.bin                     |chicken                      |sphere_clicktest.gltf|
|BoomBox.gltf                   |EnvironmentTest.gltf      |SciFiHelmet.gltf              |chickenmove                  |tail.mtl|
|BoomBoxWithAxes.gltf           |Flags.glb                 |Shuttle.glb                   |cow                          |tail.obj|
|Box.glb                        |FlightHelmet.gltf         |SimpleMeshes.gltf             |cow2                         |throne|
|Box.gltf                       |GearboxAssy.glb           |SimpleMorph.gltf              |crown                        |tiles.mtl|
|BoxAnimated.glb                |GearboxAssy.gltf          |SimpleSparseAccessor.gltf     |cybertruck                   |tiles.obj|
|BoxAnimated.gltf               |Head.gltf                 |SmilingFace.glb               |drone-small.glb              |toni.glb|
|BoxInterleaved.glb             |Head2.glb                 |Snoop.glb                     |drone.gltf                   |tri_prism.glb|
|BoxInterleaved.gltf            |InterpolationTest.glb     |SpecGlossVsMetalRough.glb     |enginside.mtl                |valve_index_left.gltf|
|BoxTextured.glb                |InterpolationTest.gltf    |SpecGlossVsMetalRough.gltf    |enginside.obj                |valve_index_right.gltf|
|BoxTextured.gltf               |Lantern.glb               |Sponza.gltf                   |engmount.mtl                 |vr_controller_vive.mtl|
|BoxTexturedNonPowerOfTwo.glb   |Lantern.gltf              |Stringlights.glb              |engmount.obj                 |vr_controller_vive.obj|
|BoxTexturedNonPowerOfTwo.gltf  |MetalRoughSpheres.glb     |Suzanne.gltf                  |engout.mtl                   |windows.mtl|
|BoxVertexColors.glb            |MetalRoughSpheres.gltf    |TextureCoordinateTest.glb     |engout.obj                   |windows.obj|
|BoxVertexColors.gltf           |Monster.glb               |TextureCoordinateTest.gltf    |engrim.mtl                   |wings.mtl|
|BrainStem.glb                  |Monster.gltf              |TextureSettingsTest.glb       |engrim.obj                   |wings.obj|
|BrainStem.gltf                 |Moon.glb                  |TextureSettingsTest.gltf      |er1k.glb||
|Buggy.glb                      |MorphPrimitivesTest.glb   |TextureTransformTest.gltf     |frog|||
|Buggy.gltf                     |MorphPrimitivesTest.gltf  |Triangle.gltf                 |goose|||
