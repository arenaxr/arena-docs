---
title: URL Parameters
nav_order: 7
layout: tutorial
parent: Web Interface
---

# URL Parameters

For advanced users, the ARENA accepts URL parameters to override some internal defaults. These are passed in the address bar, after the scene name, e.g.:
`https://arenaxr.org/public/scenename/?name=MyName&scene=AScene`

The following URL parameters are accepted.

| Parameter | Type | Description |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| armode | bool | Instantly enter AR mode, *and* Do not load models with hide-on-enter-ar (allows opening scenes with large models that are not visible in AR). |
| ATLASurl | string | URL of ATLAS (e.g. `ATLASurl=//atlas.conix.io`) |
| auth | string | Save the authentication method for the browser session (e.g. `auth=anonymous`, or `auth=google`) |
| camUpdateIntervalMs | string | Minimum camera update interval in milliseconds (e.g. `camUpdateIntervalMs=100`) |
| confstats | bool | Enable logging to MQTT of conference quality stats. |
| fixedCamera | string | Sets the camera name to the given value **and** enables VIO output to `realm/vio/scene-name/camera-name` ; `fixedCamera=iPhone` will set the camera name **exactly** to the given value (not add any prefix/suffix) |
| lat | float | Override device location; (e.g. `lat=40.4427`) |
| long | float | Override device location; (e.g. `long=79.9430`) |
| mqttHost | string | Override MQTT host address (e.g. `mqttHost=mqtt.arenaxr.org`) |
| name | string | Set user name (e.g. `name=MyName`) |
| noname | bool | Handles display of user name on the screen. False: (default) display the user name. True: Do not display the user name. |
| noreticle | bool | In AR, change the reticle ring to transparent when true, gray when false (default). |
| scene | string | Set scene name (e.g. `scene=AScene`) |
| skipav | bool | Skips the webcam, speaker, microphone setup modal. Attempts to use previously selected devices, or system defaults |
| startCoords | string | User starting x, y, z coordinates in the 3D environment (e.g. `startCoords=0,1.6,0`) |
| startLastPos | bool | User starts at the last position recorded on this browser (saved per heartbeat in localStorage) |
| vr | bool | Do not load models with hide-on-enter-vr (allows opening scenes with large models that are not visible in VR). |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
