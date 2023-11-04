---
title: 3D Scanner Tools
layout: default
parent: 3D Content
---

#  List of 3D Scanner Tools

There are a number of tools and technologies to choose from to capture 3D scans of reality.
We've tried to share our experiences here.

## **LiDAR**

 [LiDAR](https://wikipedia.org/wiki/Lidar) or "light/laser detection and ranging" is a method for determining ranges to an object or a surface with a laser and measuring the time for the reflected light to return to the receiver. This can be powerful when combined with visual light from a camera to capture RGBD images.

| App Name | Quality / 10 | Time to Use | Difficulty / 10 | Other notes |
| -- | -- | -- | -- | -- |
| [Polycam](https://poly.cam/) | 3/10, gives good idea of room but very choppy | 5 min | 0/10 |  Can only do 360 picture, can't do room scan without lidar sensor (needs iphone 12 pro/promax) |
| [Scaniverse](https://scaniverse.com/) | 4/10 not great, depends on room but gives good idea of size | 8 min | 0/10 |  Can do room scan & objects. [Scaniverse room scan](/content/3d-content/scaniverse) write up. |
| [3D Scanner App](https://3dscannerapp.com/) | Obj:7/10, Room: 4/10 | Obj: 15 min, Room: 5 min | 0/10 | Works best with small/medium sized objects, not rooms. There is a home scan mode that only works indoors, should be better with lidar sensor. The small object is difficult to export out of app |
| [KIRI Engine](https://www.kiriengine.com/) |  |  | 0/10 |  Has free & paid version, requires phone with lidar sensor |
| [Matterport](https://matterport.com) |  |  |  | [Matterport room scan](/content/3d-content/matterport) write up. |

## **NeRF**

[NeRF](https://wikipedia.org/wiki/Neural_radiance_field) or "neural radiance field" is an AI-based method of building s 3D model from 2D images.

| App Name | Quality / 10 | Time to Use | Difficulty / 10 | Other notes |
| -- | -- | -- | -- | -- |
| [3Dpresso](https://3dpresso.ai/) |  |  | 0/10 | Film video and it turns it into 3d model, doesn't do rooms |
| [Luma AI](https://lumalabs.ai/) | 2/10 | 40 min | 0/10 |  |
| [Nerfstudio](https://docs.nerf.studio/) |8/10, can capture 360 of outdoors pretty well but not super clear |  | 8/10, based on description |  |
| [Volinga](https://volinga.ai/) |  |  |  | Have to create account, has licenses |

## **Photogrammetry**

[Photogrammetry](https://wikipedia.org/wiki/Photogrammetry) is the process of recording models through photography and other electromagnetic radiant data.

| App Name | Quality / 10 | Time to Use | Difficulty / 10 | Other notes |
| -- | -- | -- | -- | -- |
| [AliceVision](https://alicevision.org/) (Meshroom) | 7/10, depends on object, and equipment to take pictures | Depends how many images & what the object is | 4/10 |Better for models, not room scan. Can be difficult for certain objects |
| [Agisoft Metashape](https://www.agisoft.com/) | 10/10, looks good |  |  | Have to pay, Works for room scan (also does satellite image processing & satellite image processing) |
| [RealityCapture](https://www.capturingreality.com/) (Unreal Engine) | 10/10, looks good |  |  |Have to pay |
| [RealityScan](https://www.unrealengine.com/en-US/realityscan) (Unreal Engine) | Obj: 8/10 | 10 min | 0/10 easy | Scans models, not room |
