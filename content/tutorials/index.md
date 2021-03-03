---
title: Overview
nav_order: 1
layout: default
has_children: true
---

## Background

Many have predicted the future of the Web to be the integration of Web content with the real-world through technologies such as augmented reality. This overlay of virtual content on top of the physical world, called the Spatial Web (in different contexts might be called AR Cloud, MetaVerse, Digital Twin), holds promise for dramatically changing the Internet as we see it today, and has broad application.

However, building pervasive mixed (virtual and augmented) reality applications is challenging for several reasons. First, applications require global instant-on localization and anchoring to the physical world. Second, supporting interaction across multiple users and with physical entities leads to tight latency requirements. It is extremely noticeable when physical and virtual objects don’t correctly track each other. Third, support of content across platforms needs to span a wide range of compute and interaction capabilities. For example, click inputs look different on a tablet and an AR headset. Applications might need to be hosted on the cloud, at the edge or perhaps even in the end devices. Fourth, applications require access control to compute, sensor and actuator access in potentially untrusted environments. Finally, authoring and programming workflows need to adapt to real-world input and potentially interface with other Internet connected systems.

The Augmented Reality Edge Networking Architecture (ARENA) was designed to address many of these challenges of building collaborative mixed reality applications.
{: .fs-5 .fw-300 }

See a summary of the main features in the [introduction](/index.html#key-features).

## Main Concepts

Let us see the types of devices that can be part of the architecture. Then, explain the idea of an ARENA <b>Realm</b>, <b>Scene</b>, and the geographic content lookups made by <b>ATLAS</b>. Along the way, we will also try to understand the role of some important ARENA system services.

This is an overview of the ARENA architecture that we will describe.

![img](/assets/img/overview/architecture.png){: style="float: left"}


<br/><br/>
### Edge Devices

We distinguish two main types of devices at the edge: (i) <b>viewer devices</b> and (ii) and <b>other (headless) devices</b>.

#### Viewer (Edge) devices

Devices with capability to display content to a user (phones, tablets, AR/VR headsets) are assumed to run a WebXR-capable browser that and runs a web application application-based stack as detailed below. This is an important aspect of our architecture to support very different platforms and interaction modalities.

![img](/assets/img/overview/browser-stack.png){: style="float: left"}


<br/><br/>
#### (Non-Viewer) Edge Devices
Non-viewer devices are assumed to be capable of executing sandboxed ARENA programs (more details XXXXX).

### ARENA Realm

A Realm is a group of coordinating services including web servers for static content, an MQTT Publish-Subscribe (PubSub) messaging bus for real-time data distribution and a resource manager that can dispatch ARENA applications. The Realm defines a local instance of the ARENA along with any programs, devices or users that connect to the same PubSub bus.

Realms (and scenes) are found through geographic lookups made to ATLAS.

### ARENA Scene

A Scene is an abstraction that contains a group of related virtual assets like 3D objects, configuration parameters, applications with shared end-points that allow users interactions. Scenes exist within a tree-like hierarchy, with configurable access control and are often attached to a physical location. Using a web analogy, the Realm is like a (local) web server and the Scene is like a particular web application. Scenes are loaded akin to web applications within a web browser with the capability to render the content and interact with location services. However, unlike most standard web browsers, it is possible to view a composition of multiple scenes simultaneously. For example, in a public space there might be multiple scenes that each contain various applications (and other users). A user might have access to one or more scenes in the same physical space that can be layered with an XR browser session. Since a Scene is the most basic unit of access control, this can be used to enable read and/or write to particular assets. Users are provided with access tokens that define their read and write access within the Scene structure.

#### Scene Loading

It is important to distinguish how scenes are loaded and subsequently updated in real-time:
<img src="/assets/img/overview/scene-load.png" width="350"/>

Once a user connects to a Realm and loads a particular Scene, a browser is given all of the 3D objects that are within the scene. This content is initially requested from a Persistence Data Store that tracks the latest state of any persistent objects (not all objects need to be persistent).


#### Real-time Networked Updates
Once loaded, each of the 3D assets in a scene are then updated in real-time over the Realm’s local MQTT bus.  For example, if an application changes the color of a cube, this would be captured in a message over the bus. When a user moves their camera or clicks on an object, these updates and events are also transmitted as messages. Each object in a Scene is managed by an end-point on the PubSub bus making them implicitly networked. This network transparency allows any number of applications and users running from different devices to all seamlessly interact within the 3D environment.   Users can even see an avatar representation of other users in AR/VR since their camera pose is continuously published into a scene.


# Entering ARENA for the First Time

## Before you Start

For the best ARENA performance, you need a couple of things:
- **Chrome Web Browser** (FireFox also works, but sometimes FireFox doesn’t send video)
- No ad blockers (some blockers are okay, others cause issues)
- **Headphones highly recommended**. They provide directional sound and stop echo. Please stay on mute when not speaking if you don’t have headphones.
- A fast machine to handle all the processing and 3D graphics is also recommended

## Opening a Scene

Let us have a look at the **lobby** scene: [https://arena.andrew.cmu.edu/lobby](https://arena.andrew.cmu.edu/lobby){:target="\_blank"}.

The link above will open in a new tab. Since ARENA is a collaborative, multi-user environment, you may see other people there. Say Hi!

{% include alert type="note" content="
ARENA uses the concept of **scenes** to separate content. In a Virtual Reality (VR) environment, you can imagine each scene as a separate room.
"%}

## Signing In

When you first enter the ARENA, there will be a screen asking you to sign in. You can use your Google account, which will automatically set your name to the name used in your Google account (you can change this later).

![](../../assets/img/tutorial/userguide/a1.jpg)

{% include alert type="tip" content="
You can also choose to sign in anonymously; you'll have to enter a name to use in the ARENA."%}

## Permissions

You'll be asked to give location, microphone, and camera access to the ARENA site. If you do not select "yes", you won't be able to use voice, video, or the face tracking avatar.

![](../../assets/img/tutorial/userguide/a3.png)

## Moving Around

Once inside the ARENA, you should see the lobby scene. You might have to wait for all the scene to load until it looks something like this:

![](../../assets/img/tutorial/userguide/a4.png)

To move, use the arrow keys. More advanced movement can be done by a combination of ‘W’, ‘A’, ‘S’, ‘D’ (to go forward/back and stride) and the mouse (to look around/change direction).  You can also mix and match any combination of these motions.  Definitely try clicking and dragging with the mouse.

![](../../assets/img/tutorial/userguide/m1.png)

## Buttons

The buttons around the screen give access to several options, such as: your sound and video settings, you display name, chat, or find other people and places. **Note that everyone starts with audio and video off**.

| Button                                                                                                                                                                                                           | Action             | Description                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| ![](../../assets/img/icons/more.png){:height="32px" width="32px"} ![](../../assets/img/icons/less.png){:height="32px" width="32px"}                                                                                    | **Settings**       | Expand/Collapse settings along the right.                                                                           |
| ![](../../assets/img/icons/audio-on.png){:height="32px" width="32px"} ![](../../assets/img/icons/audio-off.png){:height="32px" width="32px"}                                                                           | **Microphone**     | Speak into the ARENA, or remain silent.                                                                             |
| ![](../../assets/img/icons/video-on.png){:height="32px" width="32px"} ![](../../assets/img/icons/video-off.png){:height="32px" width="32px"}                                                                           | **Camera**         | Let your camera show you as a moving box with your camera image on it.                                              |
| ![](../../assets/img/icons/avatar3-on.png){:height="32px" width="32px"} ![](../../assets/img/icons/avatar3-off.png){:height="32px" width="32px"}                                                                       | **Facial Avatar**  | Let your camera recognize your facial features, and you will appear an animated head matching your facial movement. |
| ![](../../assets/img/icons/flying-on.png){:height="32px" width="32px"} ![](../../assets/img/icons/flying-off.png){:height="32px" width="32px"}                                                                         | **Flight**         | Movement defaults to walking along the ground, this will enable you to fly up or even down through the ground.      |
| ![](../../assets/img/icons/speed-slow.png){:height="32px" width="32px"} ![](../../assets/img/icons/speed-medium.png){:height="32px" width="32px"} ![](../../assets/img/icons/speed-fast.png){:height="32px" width="32px"} | **Movement Speed** | Slow/Medium/Fast, defaults to Medium.                                                                               |
| ![](../../assets/img/icons/screen-on.png){:height="32px" width="32px"}                                                                                                                                              | **Screenshare**    | Share your screen as a large panel in the ARENA.                                                                    |
| ![](../../assets/img/icons/chat.png){:height="24px" width="24px"}                                                                                                                                                   | **Chat Messages**  | Open chat messaging.                                                                                                |
| ![](../../assets/img/icons/user-list.png){:height="24px" width="24px"}                                                                                                                                              | **User List**      | Open list of present users.                                                                                         |
| ![](../../assets/img/icons/logout.png){:height="32px" width="32px"}                                                                                                                                                 | **Sign Out**       | Exit the ARENA.                                                                                                     |

## Audio/Video Capabilities
The ARENA experience includes audio and video capabilities. Users can share their video and see other users as floating cubes. One interesting feature is that sound is spatial in the ARENA (will fade as users get further away and comes from the direction where the user is).

![](../../assets/img/tutorial/userguide/a6.png)

## Chat, Find People and Places
You can send messages to other users, find users (and place yourself in front of them) and find places, such as meeting points and posters (and place yourself in front of them), using the buttons at the bottom of the screen.

![](../../assets/img/tutorial/userguide/a5.png)

{% include alert type="note" content="
The landmarks button only appears in scenes that have landmarks.
"%}

## Additional Settings

The settings menu is collapsed by default; clicking the arrow underneath the face tracking icon will expand the menu. When clicked, you will see additional icons, your name and authentication options in a pop up next to the icons. It shows the authenticator (Google or anonymous), the email used for Google authentication, and your display name. The display name can be changed here. It is initially set to the name from your Google account or the name chosen when signing in anonymously. If you click the X on the settings box and it disappears, you will need to collapse and re-open the icons to show the options again.
