---
title: Animated Faces
layout: default
parent: 3D Content
---

# Performance Driven Animated Faces

Here are some notes gathered to understand how to understand and create facial animations for the ARENA with blendshapes and other model formats.

## Overview

- [Practice and Theory of Blendshape Facial Models](https://pdfs.semanticscholar.org/7856/4583ecf36802a77815e731b6721b57b50cd7.pdf) [[1]](#1). It's a good starting point, with a nice overview of how blendshape works.

## Blendshapes

- [Blend Shape Interpolation and FACS for Realistic Avatar](https://www.researchgate.net/publication/271596909_Blend_Shape_Interpolation_and_FACS_for_Realistic_Avatar) [[2]](#2) (**F**acial **A**ction **C**oding)
- [Face Scan App (developers)](https://www.bannaflak.com/face-scan/documentation.html)
- [Face Cap App (product)](https://www.bannaflak.com/face-cap/index.html)

## Exporting

How do we get models into the ARENA?

1. Models are ASCII FBX with text file for the rigging sequence.
1. Convert ASCII FBX -\> Binary FBX with: [https://www.autodesk.com/developer-network/platform-technologies/fbx-converter-archives](https://www.autodesk.com/developer-network/platform-technologies/fbx-converter-archives).
1. AutoDesk FAILED?! Use this instead: [https://overbits.herokuapp.com/fbxgltf/](https://overbits.herokuapp.com/fbxgltf/).
1. Convert Binary FBX to GLTF with blendshape animations: [https://github.com/facebookincubator/FBX2glTF](https://github.com/facebookincubator/FBX2glTF).

## Retargeting

How do we go from landmarks to expressions?

- [Feature points based facial animation retargeting](https://liris.cnrs.fr/Documents/Liris-3546.pdf) [[3]](#3)
- [Facial Landmark Detection: A Literature Survey](https://arxiv.org/pdf/1805.05563.pdf) [[4]](#4)

## FLAME

- **F**aces **L**earned with an **A**rticulated **M**odel and **E**xpressions: [https://flame.is.tue.mpg.de/](https://flame.is.tue.mpg.de/)
- Early Hao Li project on using ML to do face rigging.
- Very cool web demo: [https://flame.is.tue.mpg.de/interactivemodelviewer.html](https://flame.is.tue.mpg.de/interactivemodelviewer.html)


## References

<a id="1">[1]</a>
Lewis, J.P., Anjyo, K., Rhee, T., Zhang, M., Pighin, F.H., & Deng, Z. (2014). Practice and Theory of Blendshape Facial Models. *Eurographics*.

<a id="2">[2]</a>
Alkawaz, M.H., Mohamad, D.B., Basori, A.H., & Saba, T. (2015). Blend Shape Interpolation and FACS for Realistic Avatar. *3D Research*, 6, 1-10.

<a id="3">[3]</a>
Dutreve, L., Meyer, A., & Bouakaz, S. (2008). Feature points based facial animation retargeting. *Virtual Reality Software and Technology*.

<a id="4">[4]</a>
Wu, Y., & Ji, Q. (2018). Facial Landmark Detection: A Literature Survey. *International Journal of Computer Vision*, 127, 115-142.
