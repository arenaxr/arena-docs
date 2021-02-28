---
title: Development Quick Start
nav_order: 2
layout: default
parent: ARENA Quick Start
---

# Quick Start for Developers

{% include alert type="warning" title="Warning" content="The code examples below are currently out of date and are being updated..." %}

Most of the ARENA utilities and tools mentioned here are also listed on a set of quick links on the left side bar as [Source and Links](../source).

## View the ARENA

To start, open your browser to the scene we will be using in this tutorial. This link will open in a new tab: [https://arena.andrew.cmu.edu/?scene=example](https://arena.andrew.cmu.edu/?scene=example){:target="\_blank"}. Since ARENA is a collaborative, multi-user environment, you may see other tutorial learners there. Say Hi!

{% include alert type="tip" content="
Feel free to use your own scene name if you want to save your work later.
"%}

![](../../../assets/img/tutorial/scene.png)

## Navigating
Our [User Guide](user-guide) will give you some pointers for navigation and video conferencing, but to start with, just using the arrows keys on your keyboard will get you started.

## Install the ARENA Python library

The easiest way to begin programming in the ARENA is to install the [Python library](../python) and create your first Python program. ARENA communications are a series of MQTT messages which govern all objects and their properties. This library is a wrapper which will allow you to easily send and receive those messages.

## Create a cube and observe

Now, create the simplest Python program you can below, which will generate a 1-meter cube. By default, objects are generated in white (#FFFFFF), with no rotation, at scene x, y, z position (0, 0, 0), and with no other properties applied. Some of the other properties you can add to objects are detailed in our [Python Examples](../python/examples). Notice that cube seems stuck in the ground, which is due to the cube's origin at its center positioned at scene coordinates (0, 0, 0). If you enable Flying mode (see above), you can move below the ground plane and view the other half of the cube. Type Ctrl-C to end the program.

{% include alert type="tip" content="
Use the **Search ARENA Documentation** bar at the very top of every page on this site to find examples and information on anything you need.
"%}

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
arena.Object(objType=arena.Shape.cube)
arena.handle_events()
```

![](../../../assets/img/tutorial/cube.png)

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

Take a minute to view the ARENA network's connections as you move around in the ARENA on our [Network graph](https://arena.andrew.cmu.edu/network). Clients connected <span style="background-color: black; color: orange;">(orange square)</span>, client subnets <span style="background-color: black; color: gray;">(gray box)</span>, MQTT topics <span style="background-color: black; color: DeepSkyBlue;">(blue circle)</span>, and their current relationships and throughput <span style="background-color: black; color: white;">(white arrow)</span> can be visualized.

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
- Many more ideas are available in our [examples](../python/examples).

## Animate a GLTF model

A more advanced manipulation of objects in the ARENA is using 3d models as [GLTF](../3d-content/gltf-files). Here we are going to use a GLTF model of a duck and some animation rules to make it rotate.

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

At your leisure, read more about methods to generate [3d content](../3d-content) and [animate](../3d-content/animated-models) objects and models.

![](../../../assets/img/tutorial/animate.png)

## Use persistence, reload browser

Up until now, everything you have created has been non-persistent. That is, objects are only rendered in real-time for any browsers open to the `example` as MQTT messages are received. Now, if you refresh your browser, notice that all the objects we created are gone, new visitors to this scene will not see them. To backup your scene objects into our [persistence database](../tools/persistence) you will have to specify `persist=True` in [Python definitions](../python/definitions), or `"persist": true` in the raw [JSON formatted messages](../messaging/examples#persisted-objects). Let's try an example of persisting object properties into our database in the next example.

## MQTT Messaging Format

This is a more raw method of generating messages from the the Mosquitto Publish client command line. The structure of our [messaging format](../messaging), [examples](../messaging/examples), and [definitions](../messaging/definitions) are available in more detail. For now, let's save this rotating duck into a scene name that you will come up with. This message is a duplicate of the of the previous Python example in raw JSON form, but with one added attribute: `"persist": true`. Now, refresh your browser after this command and our duck comes back! You may need to install the Mosquitto client on your system: [https://mosquitto.org/](https://mosquitto.org).

```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/[a scene name of your own]/duck_1 -m '{ "object_id" : "duck_1", "action": "create", "type": "object", "data": {"object_type": "gltf-model", "position": {"x":-1, "y": 1, "z": -3}, "url": "models/Duck.glb", "animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000} }, "persist": true }'
```

{% include alert type="danger" content="
Be sure to replace `[a scene name of your own]`.
"%}

{% include alert type="tip" content="
Make note of the structure of the `data` element in the above JSON. There are ways to support almost [any A-Frame feature](../developer/aframe) using arbitrary JSON.
"%}

## Link your scene to the physical world
You can make a scene you create linkable to the physical world by adding its coordinates to the [ATLAS tool](https://atlas.conix.io) (requires write permission to list coordinates). This will allow users in Augmented Reality (AR) to [discover your ARENA scene](../tools/atlas) when they are in physical range of it.

  ![](../../../assets/img/tutorial/atlas.png)

## Edit in Scene Builder
Let's take a look at what we've just saved in our [Scene Builder](https://arena.andrew.cmu.edu/build) tool. From here, you can also create/update/delete ARENA objects.

Select the `example` scene in the scene list and you will see that the `duck_1` object we used with persistence has been pulled out of the persistence DB to be listed here. Now, click on the edit button icon to the right of the `duck_1` model in the Scene Objects list. Notice that the Object JSON section in the right column has the full JSON you originally submitted.

Here you can change the position of the Duck model, for example, easily to anything you wish.

  ![](../../../assets/img/tutorial/builder.png)

## Store Your Program in the ARENA
You can use the ARENA RunTime Supervisor, [ARTS](../arts), to run your Python program in a scene without using the Python command-line. The general steps are:
* Upload a Python program to the [File Store](https://arena.andrew.cmu.edu/storemng).
* Edit your scene in the [Scene Builder](https://arena.andrew.cmu.edu/build), to add your program object from the File Store.
* Monitor your program's runtime in the [ARTS GUI](https://arena.andrew.cmu.edu/arts).

In more detail, there are step by step instructions to run your Python program like this in the [Scene Edit/Program Launch Example](../arts/python).

## Debug your program in ARTS
Once your program is running, use the [ARTS GUI](https://arena.andrew.cmu.edu/arts). You can select your program from all the [ARTS Modules](../arts) in the tree graph. After selecting your program, on the right side, you can monitor the WASM or Python module's `stdout` logging, migrate the module to another scene, remove the module completely, and perform other maintenance.

  ![](../../../assets/img/tutorial/arts.png)

## Debug your scene with A-Frame Scene Inspector
Since the ARENA's rendering uses the A-Frame web 3D rendering engine, you can open the [A-Frame Scene Inspector](https://aframe.io/docs/1.0.0/introduction/visual-inspector-and-dev-tools.html) on any scene to examine and manipulate any of the A-Frame elements in your scene.  Try this now from your example scene by typing `<ctrl> + <alt> + i` on most systems.

Examine the list of elements on the left side. Each element or object you select will show it's details and attributes on the right side. You may edit any attributes here you wish, however, remember that the A-Frame Scene Inspector will not persist any changes to the persistence database. We do have a way to visually manipulate objects and save changes that we will share next.

![](../../../assets/img/tutorial/inspector.png)

## AR Builder, visual content authoring
We also have a Python program, [AR Builder (ARB)](../tools/authoring), which you can use to create and edit objects for your scene. You can use it in VR (virtual reality) as a way to edit your scene and save changes to the persistence database. Importantly, you can use it in AR (augmented reality) in combination with [AR-supported browsers](https://createwebxr.com/webAR.html) and [localization techniques](../localization) to anchor scene objects in physical space.

{% include alert type="note" title="note" content="
AR-supported browsers still need customization from our lab to support visual localization tags.
" %}

In either case, ARB allows any user in the scene to edit, so it can be used collaboratively by multiple users remotely as VR, in person as AR, or as XR (mixed reality), a combination of both.

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bYantKzkTFk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
