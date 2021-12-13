---
title: ARENA Screenshare
nav_order: 5
layout: tutorial
parent: Web Interface
---

# ARENA Screenshare

You can share your screen in the ARENA following the tips below.

## Screenshare on Primitive Objects

There are a few hints to help you establish objects to screenshare on.

- If you choose the name/ID of an already existing object in a scene, it will set the texture of that existing object to be your screen.
- If you choose an object that does not exist in a scene, it will spawn a new screen sharing plane with your chosen `object_id`. This object is not sent through the MQTT bus but is still created for all clients.
- Once you have selected your object name, it will open a new tab that allows you to choose which screen you want to share, and ARENA will automatically place that screen onto the object with an `object_id` you specified.
- You can do whatever you want the object you’re screen sharing on as if it were a normal arena object (change size, shape, attach children, etc). This also applies to the object `screenshare`; it's just a standard ARENA object with `object_id`: `screenshare`!
- When an object is dynamically created with the screen share button, it won't go away after you stop screen sharing. It will only go away if you refresh the page.

<!-- TODO: integrate this guidance...
- you can no longer screenshare to every and any object. only objects with attribute screenshareable=True can be screen share’d on.
- screen share button now gives a list of objects with screenshareable=True and lets you select from them. you are allowed to select multiple.
- an object with id screenshare will be created like before iff there are no screenshareble objects in a scene.
-->

## Screenshare Walkthrough

<!-- TODO: add setup to click Landmarks to see Screens as Landmarks -->

- Click the **More Options** icon: ![](../../assets/img/icons/more.png){:height="24px" width="24px"}
- Click the **Screenshare** icon: ![](../../assets/img/icons/screen-on.png){:height="24px" width="24px"}

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
