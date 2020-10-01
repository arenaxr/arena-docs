---
title: Quick Start
nav_order: 1
layout: default
---

# Quick Start Tutorial

{% include alert type="warning" title="TODO" content="Write me." %}

## Open a browser, scene=hello

![](../assets/img/tutorial/scene.png)

## Move your camera

| Button | Action | Description |
| ------ | ------ | ----------- |
| ![](../assets/img/icons/more.png){:height="32px" width="32px"} ![](../assets/img/icons/less.png){:height="32px" width="32px"} | **Settings** | Expand/Collapse  |
| ![](../assets/img/icons/audio-on.png){:height="32px" width="32px"} ![](../assets/img/icons/audio-off.png){:height="32px" width="32px"} | **Microphone** | Enable/Disable |
| ![](../assets/img/icons/video-on.png){:height="32px" width="32px"} ![](../assets/img/icons/video-off.png){:height="32px" width="32px"} | **Camera** | Enable/Disable |
| ![](../assets/img/icons/avatar3-on.png){:height="32px" width="32px"} ![](../assets/img/icons/avatar3-off.png){:height="32px" width="32px"} | **Facial Avatar** | Enable/Disable |
| ![](../assets/img/icons/flying-on.png){:height="32px" width="32px"} ![](../assets/img/icons/flying-off.png){:height="32px" width="32px"} | **Flight** | Enable/Disable |
| ![](../assets/img/icons/speed-slow.png){:height="32px" width="32px"} ![](../assets/img/icons/speed-medium.png){:height="32px" width="32px"} ![](../assets/img/icons/speed-fast.png){:height="32px" width="32px"} | **Movement Speed** | Slow/Medium/Fast |
| ![](../assets/img/icons/screen-on.png){:height="32px" width="32px"} ![](../assets/img/icons/screen-off.png){:height="32px" width="32px"} | **Screenshare** | Enable/Disable |
| ![](../assets/img/icons/chat.png){:height="24px" width="24px"} | **Chat Messages** | Open chat messaging |
| ![](../assets/img/icons/user-list.png){:height="24px" width="24px"} | **User List** | Open list of present users |
| ![](../assets/img/icons/logout.png){:height="32px" width="32px"} | **Sign Out** | Exit the ARENA |


## Install arena python library
- [python](python/)

## Run hello world cube, hello.py

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", "example")
arena.Object(objType=arena.Shape.cube)
arena.handle_events()
```

![](../assets/img/tutorial/cube.png)

## Run hello world scene callback, too many msgs

```python
def scene_callback(msg):
    print("scene_callback: ", msg)

arena.init("arena.andrew.cmu.edu", "realm", "example", scene_callback)
```

## Monitor some network connections
- [Network graph](https://arena.andrew.cmu.edu/network/)

## Run hello world click listener callback

```python
def cube_callback(msg):
    print("cube_callback: ", msg)

arena.Object(objType=arena.Shape.cube, clickable=True, callback=cube_callback)
```

## Animate the cube, hello3.py
- [3d-content](3d-content/)
- [gltf-files](3d-content/gltf-files.html)
- [animated-models](3d-content/animated-models.html)

![](../assets/img/tutorial/animate.png)

## Use persistance, reload browser
- [persistance](tools/persistance.html)
- [python/examples](python/examples.html)
- [python/definitions](python/definitions.html)

```python
import arena
arena.init("arena.andrew.cmu.edu", "realm", [ a scene name of your own])
arena.Object(objType=arena.Shape.gltf_model,
             location=(-1, 1, -3),
             clickable=True,
             data='{"animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000}}',
             url="models/Duck.glb",
             persist=True)
arena.handle_events()
```

## Edit in Scene Builder page, change something
- [Scene builder](https://arena.andrew.cmu.edu/build/)
- [messaging](messaging/)
- [messaging/examples](messaging/examples.html)
- [messaging/definitions](messaging/definitions.html)
![](../assets/img/tutorial/builder.png)

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

## Debug your scene with A-Frame Scene Inspector
![](../assets/img/tutorial/inspector.png)

## Visual edit/create content with ARB
- [authoring](tools/authoring.html)
