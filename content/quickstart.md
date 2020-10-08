---
title: Quick Start
nav_order: 1
layout: default
---

# Quick Start Tutorial

Most of the ARENA utilities and tools mentioned here are also listed on a set of quick links on the left side bar as [Source and Links](source.html).

## View the ARENA

To start, open your browser to the scene we will be using in this tutorial. This link will open in a new tab: [https://arena.andrew.cmu.edu/?scene=example](https://arena.andrew.cmu.edu/?scene=example){:target="\_blank"}. Since ARENA is a collaborative, multi-user environment, you may see other tutorial learners there. Say Hi!

{% include alert type="tip" content="
Feel free to use your own scene name if you want to save your work later.
"%}

![](../assets/img/tutorial/scene.png)

## Move around

When you first enter the ARENA, your perspective position in the scene will be at x, y, z coordinates (0, 1.6, 0) which is at the center of the ground plane at about 1.6 meters in the air. Take some time to familiarize yourself with movement and other controls, some of which are listed below. Most importantly:

- **Rotate**: Click and drag the screen.
- **Move**: Arrow keys, or W-A-S-D keys.

| Button                                                                                                                                                                                                           | Action             | Description                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| ![](../assets/img/icons/more.png){:height="32px" width="32px"} ![](../assets/img/icons/less.png){:height="32px" width="32px"}                                                                                    | **Settings**       | Expand/Collapse settings along the right.                                                                           |
| ![](../assets/img/icons/audio-on.png){:height="32px" width="32px"} ![](../assets/img/icons/audio-off.png){:height="32px" width="32px"}                                                                           | **Microphone**     | Speak into the ARENA, or remain silent.                                                                             |
| ![](../assets/img/icons/video-on.png){:height="32px" width="32px"} ![](../assets/img/icons/video-off.png){:height="32px" width="32px"}                                                                           | **Camera**         | Let your camera show you as a moving box with your camera image on it.                                              |
| ![](../assets/img/icons/avatar3-on.png){:height="32px" width="32px"} ![](../assets/img/icons/avatar3-off.png){:height="32px" width="32px"}                                                                       | **Facial Avatar**  | Let your camera recognize your facial features, and you will appear an animated head matching your facial movement. |
| ![](../assets/img/icons/flying-on.png){:height="32px" width="32px"} ![](../assets/img/icons/flying-off.png){:height="32px" width="32px"}                                                                         | **Flight**         | Movement defaults to walking along the ground, this will enable you to fly up or even down through the ground.      |
| ![](../assets/img/icons/speed-slow.png){:height="32px" width="32px"} ![](../assets/img/icons/speed-medium.png){:height="32px" width="32px"} ![](../assets/img/icons/speed-fast.png){:height="32px" width="32px"} | **Movement Speed** | Slow/Medium/Fast, defaults to Medium.                                                                               |
| ![](../assets/img/icons/screen-on.png){:height="32px" width="32px"}                                                                                                                                              | **Screenshare**    | Share your screen as a large panel in the ARENA.                                                                    |
| ![](../assets/img/icons/chat.png){:height="24px" width="24px"}                                                                                                                                                   | **Chat Messages**  | Open chat messaging.                                                                                                |
| ![](../assets/img/icons/user-list.png){:height="24px" width="24px"}                                                                                                                                              | **User List**      | Open list of present users.                                                                                         |
| ![](../assets/img/icons/logout.png){:height="32px" width="32px"}                                                                                                                                                 | **Sign Out**       | Exit the ARENA.                                                                                                     |

## Install the ARENA Python library

The easiest way to begin programming in the ARENA is to install the [Python library](python/) and create your first Python program. ARENA communications are a series of MQTT messages which govern all objects and their properties. This library is a wrapper which will allow you to easily send and receive those messages.

## Create a cube and observe

Now, create the simplest Python program you can below, which will generate a 1-meter cube. By default, objects are generated in white (#FFFFFF), with no rotation, at scene x, y, z position (0, 0, 0), and with no other properties applied. Some of the other properties you can add to objects are detailed in our [Python Examples](python/examples.html). Notice that cube seems stuck in the ground, which is due to the cube's origin at its center positioned at scene coordinates (0, 0, 0). If you enable Flying mode (see above), you can move below the ground plane and view the other half of the cube. Type Ctrl-C to end the program.

{% include alert type="tip" content="
Use the **Search ARENA Documentation** bar at the very top of every page on this site to find examples and information on anything you need.
"%}

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
arena.Object(objType=arena.Shape.cube)
arena.handle_events()
```

![](../assets/img/tutorial/cube.png)

## Clients and Scene Callbacks

As a web browser user of the ARENA, you are connecting to the ARENA MQTT broker as a one client connection, in which you are publishing your "camera" perspective as you move, and subscribing to changes in other objects and other users' "camera" moves. Everything time you run a Python program you are also connecting to the broker as another client connection, in which the above program published a message creating a cube, and also subscribes you other users "camera" moves, and objects.

Let's try observing some of those other messages but adding the following code to your Python program. Add the `scene_callback` function, and also alter your `arena.init()` call, to accept the new callback and allow you to observe all the messages you have subscribed to in this scene.

```python
def scene_callback(msg):
    print("scene_callback: ", msg)

arena.init("arena.andrew.cmu.edu", "realm", "example", scene_callback)
```

Move yourself around in the browser view and notice all the camera updates and positions and rotation changes as you move. This is way too much information to be human readable! However, you can filter out these messages for what you need, or even better, if you only need feedback for a specific object, like our cube, we'll cover that soon.

## Monitor network connections

Take a minute to view the ARENA network's connections as you move around in the ARENA on our [Network graph](https://arena.andrew.cmu.edu/network/). Clients connected <span style="background-color: black; color: orange;">(orange square)</span>, client subnets <span style="background-color: black; color: gray;">(gray box)</span>, MQTT topics <span style="background-color: black; color: DeepSkyBlue;">(blue circle)</span>, and their current relationships and throughput <span style="background-color: black; color: white;">(white arrow)</span> can be visualized.

Controls:

- **Pause/Play**: Stop or resume fetching graphs.
- **Forward/Back**: Step forward one or step back one previously fetched graph.
- **Scroll**: Zoom in and out of detail.

## Object callbacks

One way to reduce the flood of messages for your Python program is to define a callback specifically for one object, our cube for example. Update your program to comment out all messages subscribed in the scene, add a callback just for your cube object, and update the creation of your cube object with a click-listener (`clickable=True`) and the new `cube_callback`.

```python
def scene_callback(msg):
#    print("scene_callback: ", msg)

def cube_callback(msg):
    print("cube_callback: ", msg)

arena.Object(objType=arena.Shape.cube, clickable=True, callback=cube_callback)
```

Now, in your scene use your mouse to click on the cube and notice the messages you receive just from the cube. You have useful information like: what type of event - mouse up/down/enter/leave, the owner of the event, the position of the owner, the position of the click. You can use this information to programmatically decide how to respond and begin creating a rich, interactive, 3d experience for your users.

- What should `mousedown` do for this object? Change its color?
- What should `mouseenter` or `mouseleave` do? Change its opacity?
- Many more ideas are available in our [examples](python/examples.html).

## Animate a GLTF model

A more advanced manipulation of objects in the ARENA is using 3d models as [GLTF](3d-content/gltf-files.html). Here we are going to use a GLTF model of a duck and some animation rules to make it rotate.

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
arena.Object(objType=arena.Shape.gltf_model,
             objName="duck_1",
             location=(-1, 1, -3),
             data='{"animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000}}',
             url="models/Duck.glb")
arena.handle_events()
```

At your leisure, read more about methods to generate [3d content](3d-content/) and [animate](3d-content/animated-models.html) objects and models.

![](../assets/img/tutorial/animate.png)

## Use persistance, reload browser

Up until now, everything you have created has been non-persistent. That is, objects are only rendered in real-time for any browsers open to the `example` as MQTT messages are received. Now, if you refresh your browser, notice that all the objects we created are gone, new visitors to this scene will not see them. To backup your scene objects into our [persistance database](tools/persistance.html) you will have to specify `persist=True` in [Python definitions](python/definitions.html#persist), or `"persist": true` in the raw JSON formatted messages. Let's try an example of persisting object properties into our database in the next example.

## MQTT Messaging Format

This is a more raw method of generating messages from the the Mosquitto Publish client command line. Let's save this rotating duck into a scene name that you will come up with on your own. This message is a duplicate of the of the previous Python example in raw JSON form, but with one added attribute: `"persist": true`. Now, refresh your browser after this command and our duck comes back!

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/duck_1 -m '{ "object_id" : "duck_1", "action": "create", "type": "object", "data": {"object_type": "gltf-model", "position": {"x":-1, "y": 1, "z": -3}, "url": "models/Duck.glb", "animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000} }, "persist": true }'
```

Be sure to replace `[a scene name of your own]`.

{% include alert type="tip" content="
Make note of the structure of the `data` element in the above JSON. There are ways to support almost [any A-Frame feature](developer/aframe.html) using arbitrary JSON.
"%}

## Edit in Scene Builder
Let's take a look at what we've just saved in our [Scene Builder](https://arena.andrew.cmu.edu/build/) tool.
- [messaging](messaging/)
- [messaging/examples](messaging/examples.html)
- [messaging/definitions](messaging/definitions.html)
  ![](../assets/img/tutorial/builder.png)

{% include alert type="warning" title="Warning" content="Writing in progress...." %}

## Link your scene to the physical world

- [atlas](tools/atlas.html)
- [atlas](https://atlas.conix.io) (requires write permission)
  ![](../assets/img/tutorial/atlas.png)

## Upload python to file store

- [File store](https://arena.andrew.cmu.edu/storemng/) (requires read/write permission)

## Use Builder to add your program runtime

## Debug your program in ARTS

- [ARTS GUI](https://arena.andrew.cmu.edu/arts/)
- [arts](arts/)
  ![](../assets/img/tutorial/arts.png)

## Debug your scene with A-Frame Scene Inspector

![](../assets/img/tutorial/inspector.png)

## Visual edit/create content with ARB

- [authoring](tools/authoring.html)
