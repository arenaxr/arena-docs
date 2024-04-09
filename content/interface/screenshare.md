---
title: Screenshare
nav_order: 6
layout: tutorial
parent: Web Interface
---

# Screenshare

You can share your screen in the ARENA following the tips below.

## Screenshare on Primitive Objects

There are a few hints to help you establish objects to screenshare on.

- If you choose the name/ID of an already existing object in a scene, it will set the texture of that existing object to be your screen.
- If you choose an object that does not exist in a scene, it will spawn a new screen sharing plane with your chosen `object_id`. This object is not sent through the MQTT bus but is still created for all clients.
- Once you have selected your object name, it will open a new tab that allows you to choose which screen you want to share, and ARENA will automatically place that screen onto the object with an `object_id` you specified.
- You can do whatever you want the object you’re screen sharing on as if it were a normal arena object (change size, shape, attach children, etc). This also applies to the object `screenshare`; it's just a standard ARENA object with `object_id`: `screenshare`!
- When an object is dynamically created with the screen share button, it won't go away after you stop screen sharing. It will only go away if you refresh the page.
- You can no longer screenshare to every and any object. only objects with attribute `screenshareable=True` can be screen-shared on.
- Screen share button now gives a list of objects with `screenshareable=True` and lets you select from them. you are allowed to select multiple.
- An object with id screenshare will be created like before if there are no screenshareble objects in a scene.

## Screenshare Custom Flat Screen Example

If you want to create a custom screen with traditional flat properties, the below example is one way. Note the [`box`](/content/schemas/message/box) object type in use, adjusting the `depth, height, width` properties for the screen ratio we want. Applying the material texture to the outside of the box mesh (`"material": {"side": "front"}`) allows the screen to render from left to right on both sides since it is a `box` with 6 front planes and 6 back planes. The `plane` object, conversely, has 1 front plane and 1 back plane, and is another good primitive type to use.

```json
{
  "object_id": "screen-flat",
  "data": {
    "object_type": "box",
    "depth": 0.1,
    "height": 3,
    "width": 5.3,
    "position": {
      "x": 3,
      "y": 2.7,
      "z": 0
    },
    "material": {
      "color": "#ffffff",
      "shader": "flat",
      "side": "front"
    },
    "screenshareable": true
  }
}
```

## Screenshare Custom Curved Screen Example

If you want to create a custom screen with curved screen properties, the below example is one way which generally mimics the A-Frame [`a-curvedimage`](https://aframe.io/docs/1.5.0/primitives/a-curvedimage.html) primitive. Note the [`cylinder`](/content/schemas/message/cylinder) object type in use, adjusting the `radius, height, thetaStart, thetaLength, openEnded` properties for the screen ratio we want. Applying the material texture to the (`"material": {"side": "double", "repeat": {"x": -1, "y": 1}}`) allows the screen to render from left to right on both sides.

```json
{
  "object_id": "screen-curved",
  "data": {
    "object_type": "cylinder",
    "height": 5,
    "radius": 10,
    "position": {
      "x": 3,
      "y": 2.5,
      "z": 7
    },
    "material": {
      "color": "#ffffff",
      "side": "double",
      "shader": "flat",
      "repeat": {
        "x": -1,
        "y": 1
      }
    },
    "openEnded": true,
    "thetaLength": 60,
    "screenshareable": true,
    "thetaStart": 150
  }
}
```

## Screenshare Walkthrough

<!-- TODO: add setup to click Landmarks to see Screens as Landmarks -->

- Click the **More Options** icon: ![](/assets/img/icons/down-arrow.png){:height="32px" width="32px" style="background-color:#262626"}
- Click the **Screenshare** icon: ![](/assets/img/icons/screen-on.png){:height="32px" width="32px" style="background-color:#262626"}

<img src="/assets/img/overview/screenshare/ARENA-screenshare0.png" width="49%" />
<img src="/assets/img/overview/screenshare/ARENA-screenshare1.png" width="49%" />

- You will be asked to confirm if you intend to share your screen to the scene.

<img src="/assets/img/overview/screenshare/ARENA-screenshare2.png" width="100%" />

- You can enter multiple screen `object_id` comma-delimited to share to multiple screens.
- For a single screen share, the default `screenshare` id is typically a good option.

<img src="/assets/img/overview/screenshare/ARENA-screenshare3.png" width="100%" />

- Select screens or application sharing.

<img src="/assets/img/overview/screenshare/ARENA-screenshare4.png" width="100%" />

{% include alert type="warning" content="
**Mac OS users: You need to give permissions to Chrome in the System Preferences first.**

- Click **Screen Recording**
- Check **Google Chrome**
  "%}

<p align="center">
<img src="/assets/img/overview/screenshare/ARENA-screenshare5.png" width="50%" />
</p>

- ARENA will open a new tab showing which view is being shared.
- Click **Exit** to end screen sharing.

<img src="/assets/img/overview/screenshare/ARENA-screenshare6.png" width="100%" />

- The ARENA scene view will now show your screen mapped across each `object_id` chosen.

<img src="/assets/img/overview/screenshare/ARENA-screenshare7.png" width="100%" />

- Closeup view.

<img src="/assets/img/overview/screenshare/ARENA-screenshare8.png" width="100%" />

## Using PowerPoint

{% include alert type="tip" content="
**You can easily share just a screen in PowerPoint even in presenter mode.**
"%}

- **Slide Show** \-> **Setup Slide Show Options** \-> **Browsed by an individual**
- Right-click during presentation brings up cursor options
- Select **Browsed by an individual**
- Select **Slide Show**
- Select **Setup Slide Show**

### **Single Window Present**

- Select **Slide Show** tab
- Select **Setup Slide Show**
- Select **Browsed by an individual \(window\)**

<img src="/assets/img/overview/screenshare/ARENA-screenshare9.png" width="100%" />

- Right-click for Pointers.

<img src="/assets/img/overview/screenshare/ARENA-screenshare10.png" width="100%" />
