---
title: URL Parameters
nav_order: 7
layout: tutorial
parent: Web Interface
---

# URL Parameters

For **advanced** users, the ARENA accepts URL parameters to override some internal defaults. These are passed in the address bar, after the scene name, e.g.:
`https://arenaxr.org/public/scenename/?name=MyName&scene=AScene`

## URL Beginner

The `Scenes` page includes a set of easy checkboxes to change more common URL parameters you may want to use: [https://arenaxr.org/scenes](https://arenaxr.org/scenes).

1. Click `My Scenes` and select your scene name.
1. Click `Scene URL Options` and check the boxes you need.
1. Change `scene permissions` if needed.
1. Use the buttons to enter the scene or copy the scene link with parameters to share with others.

<img src="/assets/img/interface/url-options1.png" width="50%" />

## URL Advanced

The following URL parameters are accepted, beginner or **advanced**. The **advanced** parameters may have performance consequences that beginners may want to avoid.

| Parameter | Type | Level | Description |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| armode | bool | beginner | Instantly enter AR mode, *and* Do not load models with hide-on-enter-ar (allows opening scenes with large models that are not visible in AR). |
| ATLASurl | string | **advanced** | URL of ATLAS (e.g. `ATLASurl=//atlas.conix.io`) |
| auth | string | beginner | Save the authentication method for the browser session (e.g. `auth=anonymous`, or `auth=google`) |
| camUpdateIntervalMs | string | **advanced** | Minimum camera update interval in milliseconds (e.g. `camUpdateIntervalMs=100`) |
| confstats | bool | **advanced** | Enable logging to MQTT of conference quality stats. |
| hudstats | bool | **advanced** | Render a HUD of performance/memory stats. |
| fixedCamera | string | **advanced** | Sets the camera name to the given value **and** enables VIO output to `realm/vio/scene-name/camera-name` ; `fixedCamera=iPhone` will set the camera name **exactly** to the given value (not add any prefix/suffix) |
| lat | float | **advanced** | Override device location; (e.g. `lat=40.4427`) |
| long | float | **advanced** | Override device location; (e.g. `long=79.9430`) |
| mqttHost | string | **advanced** | Override MQTT host address (e.g. `mqttHost=mqtt.arenaxr.org`) |
| name | string | **advanced** | Set user name (e.g. `name=MyName`) |
| noav | bool | beginner | Disables videoconferencing for this browser only. |
| noname | bool | beginner | Handles display of user name on the screen. False: (default) display the user name. True: Do not display the user name. |
| noreticle | bool | beginner | In AR, change the reticle ring to transparent when true, gray when false (default). |
| scene | string | **advanced** | Set scene name (e.g. `scene=AScene`) |
| skipav | bool | beginner | Skips the webcam, speaker, microphone setup modal. Attempts to use previously selected devices, or system defaults |
| startCoords | string | **advanced** | User starting x, y, z coordinates in the 3D environment (e.g. `startCoords=0,1.6,0`) |
| startLastPos | bool | beginner | User starts at the last position recorded on this browser (saved per heartbeat in localStorage) |
| vr | bool | beginner | Do not load models with hide-on-enter-vr (allows opening scenes with large models that are not visible in VR). |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
