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
We have a longer [list of 3d scanning tools](/content/3d-content/scan-tools) available for LiDAR, NERF, and Photogrammerty options.

1. **Scan software** depends on room size and expense. For beginners we recommend using Scaniverse on a iPad/iPhone:

   - **Small** room, **free** with iPhone: use [Scaniverse](/content/3d-content/scaniverse)
   - **Small/Medium** room, **more** expensive: use [Photogrammetry](/content/overview/photogrammetry)
   - **Large** room, **most** expensive: use [Matterport](/content/3d-content/matterport)

1. **Start** your scan standing on top the the **origin AprilTag**, in this way your scan model's internal origin point will be as close as possible to the AprilTag, reducing later adjustments to the model's 3d-world pose.

1. **Export** your scan as a **.GLB** file. Check the options for export quality and, after testing your model in the ARENA, you may want to repeat this step choosing different options to improve rendering time. The size of the model matters, but is also hard to predict.

1. For Scaniverse, you can save the file locally on your iPad/iPhone.

![scanned room image](/ismar/images/space-annotated.png)

## Upload Your Space

We are going to use the scene you created in the Building a Scene tutorial, and add your room scale model to it.

1. From your phone, enter the [build page](https://arenaxr.org/build) for your scene.

1. There are multiple paths to upload files on the [ARENA File Store and Dropbox](/content/interface/filestore), which you can review.
   Currently we will use the simplest method, under **Add/Edit Object**, select **Type: GLTF Model**, then click **\[Upload File & Publish\]**.
   Select the model and it will be uploaded for you automatically. - Make sure the option for **Room-scale digital twin model? Hide in AR**, **<u>is unchecked</u>**. We don't want to hide it before we finish aligning the model in space.

<img src="/assets/img/overview/build/auto-upload.png" style="width:5in;border:1px solid;" />

1. Now, you will have to update `position` and `rotation` a little, then update the object by pressing the **\[+ Add/Update Object\]** button.
   The model's `position` y-axis will need be elevated a bit to account for the distance between your camera and the floor AprilTag, perhaps 1.5m.
   The model's `rotation` y-axis (Euler) you will have to experiment with, to match the default rotation of your model. - **Position**: 0, `1.5`, 0, (x, y, z) - **Rotation**: 0, `??`, 0, (x, y, z)

1. Try using your iPad/iPhone to test the `position` and `rotation ` entering your scene in AR mode as we did in the [localization tutorial](/content/overview/localization), to make sure your model lines up to the AprilTag.

1. Once your model is in place, disable the view in AR, by adding the **Hide in AR** property, this time set it to **<u>checked</u>** and press the **\[+ Add/Update Object\]** button again.

<img src="/assets/img/overview/twin/twin1.png" style="border:1px solid;" />

## Program Your Space

All this so far helps you Twin your physical space in 3D, but now, let us add some interactivity the Twinned data. Your experience in previous [Python tutorials](/content/overview/dev-guide) will help you generate interactions from buttons and other objects. Here is some guidance when building a digital twin application.

- **Data**: What data is useful in proximity to your space? What useful displays or controls were previously **impractical or inappropriate**? Consider these data classes:
  - Sensor data embedded in walls or machines: network, electric, compute, pipes and filtration.
  - Sensors which cannot be blocked for light access: foliage, plants, solar panels.
  - System components which are hidden for aesthetics, but difficult to find for maintenance.
- **Text I/O**: There are multiple ways to **render text, data,** and allow **user input**. Try these strategies:
  - [ARENA UI Panels](/content/3d-content/ui)
  - [Text Display](/content/python/objects/text)
  - [Text Input](/content/python/attributes/textinput)
  - [Object Click Events](/content/python/events#click-events)
- **Text Color**: Pay attention to the overall colors of your room model, you want any text you display to be **well contrasted**. ARENA UI Panels have **light or dark themes**, and text in general can be **any color**.
- **Portal/Videosphere**: [Videospheres and Portals](/content/overview/panoramic) are a nice to have for hybrid interaction and can align well to a 3D model twin, but consider your goal. Do you want to host a hybrid meeting, or provide an XR interaction of your valuable data?

{% include alert type="goal" content="
Scan your space and add it to your scene using these techniques to create a replica of your physical space for virtual visitors.
Then, run a Python application which provides a live feed of data, perhaps showing data which is **inconvenient or impractical** to display physically,
but useful to show/hide/control in XR in proximity to the physical world.
"%}

## Example Use Cases

### Remote Teacher and Physical Student Reality Capture

This use case works best for a space where one or more remote participants or observers need to observe the physical space or ac tions of 1-2 people in a physical space from multiple angles. Some scenarios are Teacher/Student, Coach/Athlete.

#### ARENA Scene

- GLTF/Splat Model: Scanned space model matching Student Room (`hide-in-ar`)
- Entity: Landmark for Student Fixed View
- Box: Invisible orbit box (optional)
- Program: Laser-pointer
- Others: Clickable models that are pertinent

#### Student Room

- 4 calibrated cameras, PC running Reality Capture
- Flat screen monitor, mounted webcam (landscape), laptop or Mac Mini acting as a Portal
- **Student Screen Left Side:**
  - Chrome: `https://arenaxr.org/[scene]?disableRenderFusion=1`
  - Display Name: Student Fixed View
  - Presence: Portal
  - Mirrored 3D Scene: checked
  - Camera: on
  - Microphone: on
- **Student Screen Right Side**:
  - Chrome (Incognito): `https://arenaxr.org/[scene]?reprojectMovement=1`
  - Display Name: Student Moving View
  - Presence: Standard

#### Teacher Room

- 360 camera mounted on table/desk
- Flat screen monitor, laptop
- **Teacher Screen** (mirror laptop view)
  - Chrome: `https://arenaxr.org/[scene]?reprojectMovement=1`
  - Chrome (orbit option): `https://arenaxr.org/[scene]?reprojectMovement=1&orbit=orbit`
  - Display Name: Teacher Moving View
  - Presence: Standard
  - Camera: on
  - Microphone: on
