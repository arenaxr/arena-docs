---
title: Debugging Programs
nav_order: 1
layout: default
parent: ARENA Programs
---

# Python Console Interface

There is a console interface to the `arena-py` library. This is designed to have a way to inspect the program from the console, without having to send a heartbeat or write your own command/response interface.

Enable it with the environment variable:
``` shell
ENABLE_INTERPRETER=1
```

A session looks like this (look for lines starting with `#`):
``` shell
Using Scene from 'scene' input parameter: example
Using Host from 'host' input parameter: arenaxr.org
=====
Using local MQTT token.
ARENA Token Username: cli
ARENA Token valid for: 183 days, 23:25:18.051479h
Fetching ARENA configuration...
=====
Loading: https://arenaxr.org/cli/example, realm=realm
Connecting to the ARENA... Connected!
=====
Type help or ? to list available commands.

# help

Documented commands (type help <topic>):
========================================
exit  get  help  quit  show

# show
Display scene attributes: ['config_data', 'scene', 'users', 'auth', 'all_objects', 'msg_io']
# show config_data
{
    "ARENADefaults": {
        "ATLASurl": "//atlas.conix.io",
        "camHeight": 1.6,
        "camUpdateIntervalMs": 100,
        "graphTopic": "$NETWORK",
        "headModelPath": "/media/models/avatars/robobit.glb",
        "jitsiHost": "jitsi0.andrew.cmu.edu:8443",
        "latencyTopic": "$NETWORK/latency",
        "mqttHost": "arenaxr.org",
        "mqttPath": [
            "/mqtt/",
            "/mqtt1/",
            "/mqtt2/"
        ],
        "namespace": "public",
        "persistHost": "arenaxr.org",
        "persistPath": "/persist/",
        "realm": "realm",
        "sceneName": "lobby",
        "startCoords": {
            "x": 0,
            "y": 0,
            "z": 0
        },
        "userName": "Anonymous",
        "vioTopic": "/topic/vio/"
    }
}
# exit
This will terminate the ARENA program. Are you sure [Y/N]? y
Exiting...
```

You can also interact with it from `/programs`:

![](/assets/img/programs/cli-interpreter.png)
