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

## Adobe Dimension
For [Adobe Dimension](https://www.adobe.com/products/dimension.html), the general conversion steps are:
- Open a new file in Dimension
- Import the file
- Double click the Google Earth terrain in the view
- Select terrain in the scene hierarchy, delete it
- Select the top level folder in the scene for the model
- File>Export the file to glb

## GLTF Viewer
Drag-and-drop preview tool for glTF 2.0 3D models: [https://gltf-viewer.donmccurdy.com/](https://gltf-viewer.donmccurdy.com/).

## GLTF Attribution

ARENA automatically collects GLTF model metadata to be displayed in the scene credits, accessible from **Settings->Scene Credits**. Checkout the credits for a scene created with these [Spinosaurus](https://sketchfab.com/models/2135501583704537907645bf723685e7) and [Jurassic Park Gate](https://sketchfab.com/3d-models/jurassic-park-gate-3b7728e476544f6c99c99da5a34bea1d) models:

| ![img](/assets/img/3dcontent/settings.png){: style="float: left"} | ![img](/assets/img/3dcontent/credits.png){: style="float: left"}

{% include alert type="Important" content="
Please make sure your GLTF files contain metadata to credit authors as explained below.
"%}

### Attribution Metadata

The ARENA looks for authorship metadata in the format used by [Sketchfab](https://sketchfab.com/3d-models), and models downloaded from Sketchfab will have such metadata. For example:
```
"asset": {
  "extras": {
    "author": "Vaptor-Studio (https://sketchfab.com/VapTor)",
    "license": "CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/)",
    "source": "https://sketchfab.com/models/2135501583704537907645bf723685e7",
    "title": "Spinosaurus"
  },
  "generator": "Sketchfab-5.74.0",
  "version": "2.0"
}
```
You can always use a text editor to open your GLTF file and search/add the above metadata. It must be inside the `asset` mandatory property.

If creating models in **Blender**, you can add this metadata as Scene custom properties:

<img src="/assets/img/3dcontent/blender-scene-properties.png" width="400"/>

When exporting the GLTF model in Blender (File->Export), check 'Custom Properties' in the data to include in the export:

<img src="/assets/img/3dcontent/blender-gltf-export.png" width="200"/>

Metadata exported from blender will be included in the GLTF file in the `scene.extras` property. Don't worry; ARENA will look for its existence and use it.

## Chronos GLTF sample models

The [Chronos GLTF sample models](https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0) are available on the ARENA main (`andrew.andrew.cmu.edu`) server, accessible from the `store/models/<model-filename.glb>` path:

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
