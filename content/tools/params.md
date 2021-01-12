
---
title: URL Parameters
nav_order: 6
layout: default
parent: Tools
---

## URL Parameters

For advanced users, the ARENA accepts URL parameters to override some internal defaults. These are passed in the address bar, after the scene name, e.g.:
```https://arena.andrew.cmu.edu/public/scenename/?name=MyName&scene=AScene```

The following URL parameters are accepted:

| Parameter                 | Description                                                                                                                                                                       |    
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATLASurl (string)         | URL of ATLAS (e.g. ```ATLASurl=//atlas.conix.io```)                                                                                                                               |
| builder (bool)            | *Apriltag location solver parameter*. Will localize origin tag from a networked solver on pubsub, and all other tags that it finds with will be updated or created in the ATLAS   |
| cvRate (int)              | *Apriltag location solver parameter*. Throttle rate between 1 and 60 of frame processing. DEPRECATED - cvRate will auto adjust based on avg speed                                 |
| fixedCamera (string)      | Sets the camera name to the given value; ```fixedCamera=iPhone``` will set the camera name **exactly** to the given value (not add any prefix/suffix)                             |
| mqttServer (string)       | Override mqqt server address (e.g. ```mqttServer=arena.andrew.cmu.edu```)                                                                                                         |
| name (string)             | Set user name (e.g. ```name=MyName```)                                                                                                                                            |
| networkedTagSolver (bool) | *Apriltag location solver parameter*. When true, publishes tag detections and defers all tag solving of client camera to a solver sitting on pubsub                               |
| scene (string)            | Set scene name (e.g. ```scene=AScene```)                                                                                                                                          |
| startCoords (string)      | User starting coordinates                                                                                                                                                         |
| updateIntervalMs (string) | Minimum camera update interval in milliseconds (e.g. ```updateIntervalMs=100```)                                                                                                  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
