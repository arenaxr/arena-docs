---
title: URL Parameters
nav_order: 6
layout: default
parent: Tools
---

## URL Parameters

For advanced users, the ARENA accepts URL parameters to override some internal defaults. These are passed in the address bar, after the scene name, e.g.:
```https://arena.andrew.cmu.edu/public/scenename/?name=MyName&scene=AScene```

The following URL parameters are accepted.

| Parameter                    | Description                                                                                                                                                                       |    
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATLASurl (string)            | URL of ATLAS (e.g. ```ATLASurl=//atlas.conix.io```)                                                                                                                               |
| builder (bool)               | *Apriltag location solver parameter*. Will localize origin tag from a networked solver (sets ```networkedTagSolver=true```). All other tags found will be updated or created in the ATLAS (e.g ```builder=true```)     |
| camUpdateIntervalMs (string) | Minimum camera update interval in milliseconds (e.g. ```camUpdateIntervalMs=100```)                                                                                               |
| cvRate (int)                 | *Apriltag location solver parameter*. Throttle rate between 1 and 60 of frame processing. DEPRECATED - cvRate will auto adjust based on avg speed (e.g ```cvRate=1```)            |
| fixedCamera (string)         | Sets the camera name to the given value **and** enables VIO output to ```realm/vio/scene-name/camera-name``` ; ```fixedCamera=iPhone``` will set the camera name **exactly** to the given value (not add any prefix/suffix)|
| lat (float)                  | Override device location; (e.g. ```lat=40.4427```)                                                                                                                                |
| long (float)                 | Override device location; (e.g. ```long=79.9430```)                                                                                                                               |
| mqttHost (string)            | Override mqqt host address (e.g. ```mqttHost=arena.andrew.cmu.edu```)                                                                                                             |
| name (string)                | Set user name (e.g. ```name=MyName```)                                                                                                                                            |
| networkedTagSolver (bool)    | *Apriltag location solver parameter*. When true, publishes tag detections (to ```realm/g/a/camera-name```) **and defers all tag solving of client camera to a solver sitting on pubsub**|
| publishDetections (bool)     | *Apriltag location solver parameter*. Ignored if ```networkedTagSolver=true```. When true, publishes tag detections (to ```realm/g/a/camera-name```); **still processes the tag and relocalizes accordingly**|
| scene (string)               | Set scene name (e.g. ```scene=AScene```)                                                                                                                                          |
| startCoords (string)         | User starting x, y, z coordinates in the 3D environment (e.g. ```startCoords=0,1.6,0```)                                                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
