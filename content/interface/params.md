---
title: URL Parameters
nav_order: 6
layout: default
parent: Web Interface
---

## URL Parameters

For advanced users, the ARENA accepts URL parameters to override some internal defaults. These are passed in the address bar, after the scene name, e.g.:
```https://arenaxr.org/public/scenename/?name=MyName&scene=AScene```

The following URL parameters are accepted.

| Parameter                    | Description                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATLASurl (string)            | URL of ATLAS (e.g. ```ATLASurl=//atlas.conix.io```)                                                                                                                               |
| camUpdateIntervalMs (string) | Minimum camera update interval in milliseconds (e.g. ```camUpdateIntervalMs=100```)                                                                                               |
| fixedCamera (string)         | Sets the camera name to the given value **and** enables VIO output to ```realm/vio/scene-name/camera-name``` ; ```fixedCamera=iPhone``` will set the camera name **exactly** to the given value (not add any prefix/suffix)|
| lat (float)                  | Override device location; (e.g. ```lat=40.4427```)                                                                                                                                |
| long (float)                 | Override device location; (e.g. ```long=79.9430```)                                                                                                                               |
| mqttHost (string)            | Override MQTT host address (e.g. ```mqttHost=arenaxr.org```)                                                                                                             |
| name (string)                | Set user name (e.g. ```name=MyName```)                                                                                                                                            |
| scene (string)               | Set scene name (e.g. ```scene=AScene```)                                                                                                                                          |
| startCoords (string)         | User starting x, y, z coordinates in the 3D environment (e.g. ```startCoords=0,1.6,0```)                                                                                          |
| skipav (bool)                | Skips the webcam, speaker, microphone setup modal. Attempts to use previously selected devices, or system defaults                                                                |
| startLastPos (bool)          | User starts at the last position recorded on this browser (saved per heartbeat in localStorage)                                                                                    |
| noname (bool)                | Handles display of user name on the screen. False: (default) display the user name. True: Do not display the user name. |
| noreticle (bool)                | In AR, changes the reticle ring to transparent when true, gray when false (default). |
| armode (bool)                | Instantly enter AR mode. |
| ar (bool)                | Do not load models with hide-on-enter-ar (allows to open scenes with large models that are not visible in AR). |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|