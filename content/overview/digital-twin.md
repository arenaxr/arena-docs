---
title: Digital Twins
nav_order: 7
layout: tutorial
parent: Tutorial
---

# Create a Digital Twin in the ARENA

**Digital Twin**, as term can be overloaded. It can mean a digital **Data model** of sensor data relating to a physical space, or a digital **3D model** of a physical space. We will use the best of both of these perspectives to create a truly **Hybrid XR Digital Twin** in the ARENA.

## Stage Your Space For Scanning

Pick a room you want to **Twin**, and prepare it for scanning. Most of these recommendations are to ensure your scan is as **clean** as possible, with the least amount of visual artifacts.

- **<u>Doors</u>**: Close any doors in the room possible, it will reduce **trailing, incomplete** model sections.
- **<u>People/Pets</u>**: Make sure the room has no other people or pets in it, this will reduce **phantom partial** objects which the scan may pick up. Make sure you don't scan **your own feet** as well!
- **<u>Fans/Machines</u>**: Similar to People/Pets, moving objects will create phantoms you may not want.
- **<u>Screens</u>**: Consider turning off, TVs, computer monitors, and other screens that may have moving pictures or text. **Bonus**: empty screens give you a nice canvas to replace your own digital twin content.
- **<u>Lights</u>**: Turn on lights and lamps in the room, they will only help highlight features in the room and give your scan **better details**.
- **<u>AprilTag</u>**: Place the [origin AprilTag](/content/overview/localization.html#using-april-tags) from the last section in a central place on the floor to include in your scan. Choose a location where it can remain, undisturbed.

<img src="/assets/img/xr/scene-origin-tag.png"
style="width:4in;border:1px solid;" />

## Scan Your Space

There are a range of scanning cameras and software to scan a room-scale 3D model, and a few techniques to keep in mind as you scan.

1. **Scan software** depends on size and expense. For beginners we recommend using Scaniverse on a iPad/iPhone:
    - **Small** room, **less** expensive: [Scaniverse](/content/3d-content/scaniverse)
    - **Small/Medium** room, **more** expensive: [Photogrammetry](/content/overview/photogrammetry)
    - **Large** room, **most** expensive: [Matterport](/content/3d-content/matterport)

1. **Start** your scan standing on top the the **origin AprilTag**, in this way your scan model's internal origin point will be as close as possible to the AprilTag, reducing later adjustments to the model's 3d-world pose.

1. **Export** your scan as a **.GLB** file. Check the options for export quality and, after testing your model in the ARENA, you may want to repeat this step choosing different options to improve rendering time. The size of the model matters, but is also hard to predict.

1. For Scaniverse, you can save the file locally on your iPad/iPhone.

![scanned room image](/ismar/images/space-annotated.png)

## Upload Your Space

open build page, open new scene


There are multiple paths to upload files on the [ARENA File Store and Dropbox](/content/interface/filestore), which you can review.
Currently we will use the simplest method, the **\[Upload Model to File Store and Scene\]** or
**\[ <img src="/assets/img/overview/build/3dobj-icon.png" width="10"/>↑ \]**.
Select the model and it will be uploaded for you automatically.

<img src="/assets/img/overview/build/auto-upload.png" style="width:3in;border:1px solid;" />

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
