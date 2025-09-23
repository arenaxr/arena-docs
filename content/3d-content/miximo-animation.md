---
title: Mixamo Animations
layout: default
parent: 3D Content
---

# Mixamo Animations

To add Mixamo animations to GLB models, you typically need to first convert the animations from FBX format to a compatible format, or use Blender to merge the animations with your GLB model. Ensure that both the model and animations share the same rigging structure for the best results.

## Adding Mixamo Animations to GLB Models

### Overview of the Process

To add Mixamo animations to GLB models, you typically need to follow these steps:

1.  **Download the GLB Model**: Ensure your model is in GLB format and properly rigged.

2.  **Obtain Mixamo Animations**: Download the desired animations from [Mixamo](https://www.mixamo.com) in FBX format.

3.  **Use Blender for Integration**: Import both the GLB model and FBX animations into [Blender](https://www.blender.org).

### Step-by-Step Instructions

#### Importing Models and Animations

1.  **Open Blender**: Start a new project.

2.  **Import the GLB Model**:

    - Go to `File > Import > glTF 2.0 (.glb/.gltf)`.

    - Select your GLB file.

3.  **Import the FBX Animation**:

    - Go to `File > Import > FBX (.fb)`.

    - Select the downloaded FBX file from Mixamo.

#### Combining Animations

1.  **Match Armatures**: Ensure that the armature (skeleton) of the GLB model matches the one from the FBX animation. This is crucial for the animations to work correctly.

2.  **Copy Animation Data**:

    - Select the armature of the FBX animation.

    - In the `Properties` panel, go to the `Animation` tab.

    - Copy the animation data to the GLB model's armature.

3.  **Export as GLB**:

    - Once the animations are applied, go to `File > Export > glTF 2.0 (.glb/.gltf)`.

    - Choose the export settings and save your new GLB file.

### Testing the Animation

Make sure to test the animations to ensure they play correctly. [Don McCurdy's gltf-viewer website](https://gltf-viewer.donmccurdy.com/) will display animated glTF files and their associated named animations. You can then [add your animated GLB to the ARENA](/content/overview/build#add-new-objects) and [activate its animations](/content/python/attributes/animation_mixer#animation-mixer).
