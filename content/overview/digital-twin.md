---
title: Digital Twins
nav_order: 7
layout: tutorial
parent: Tutorial
---

# Create a Digital Twin in the ARENA

Digital Twin, as term can be overloaded, meaning a digital **Data model** of sensor data relating to a physical space, or a digital **3D model** of a physical space. We will use the best of both of these perspectives to create a truly **Hybrid XR Digital Twin** in the ARENA.

## Stage Your Space
- avoid other people/movable objects in scene, pets
- monitors/screens dark
- turn on lights and lamps
- daytime, night (window captives)
- use origin apriltag
- [origin apriltag](/content/overview/localization.html#using-april-tags)
- Print out this PDF of the [default “zero” AprilTag](https://raw.githubusercontent.com/arenaxr/apriltag-gen/master/output/tag36_11_00000.pdf), and place it on the floor.

<img src="/assets/img/xr/scene-origin-tag.png"
style="width:3in;border:1px solid;" />

## Scan Your Space
- size of room matters
- scaniverse, or perhaps matterport
- [scaniverse](/content/3d-content/scaniverse)
- [photogrammetry](/content/overview/photogrammetry)
- [matterport](/content/3d-content/matterport)

![scanned room image](/ismar/images/space-annotated.png)

- size of model matters

## Upload Your Space

- upload to file store

<img src="/assets/img/overview/build/auto-upload.png"
style="width:3in;border:1px solid;" />

<img src="/assets/img/overview/twin/twin1.png"
style="border:1px solid;">

- def: build page, unity
- rotate/elevate: build, unity
- test in AR mode, make sure model lines up to apriltag and other landmarks

## Program Your Space
- videospheres
- mirror portals
- rendering data, text, contrast, suggest text color, arenaui themes


{% include alert type="goal" content="
Scan your space and add it to your scene using these techniques to create a replica of your physical space for virtual visitors.
The, run a Python application which provides a live feed of data, perhaps showing data which is inconvenient or impractical to display physically,
but useful to show/hide in XR in proximity to the physical world.
"%}
