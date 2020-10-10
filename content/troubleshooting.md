---
title: Troubleshooting
nav_order: 99
layout: default
---

# Troubleshooting
Here are some common situations which can help when programming in the ARENA.

## Where is my Object?
- Is the object's position below the ground? The "y" position will negative below the default visible floor.
- Is the object's scale too big/small? Models especially have wild differences in scale, try increasing/decreasing the order of magnitude of the scale. Try scale of 10, 1, 0.1, or 0.01.
- Does the scene name in the URL match the scene name/topic where the object was created? e.g. URL is `https://arena.andrew.cmu.edu/?scene=example` and MQTT topic published to is `realm/s/example/some_object_1`.

## I have different problem, where can I get help?
We have a place for submitting issues and asking questions in most of our code repositories:
- [ARENA Docs issues](https://github.com/conix-center/ARENA/issues)
- [ARENA Website/Webserver issues](https://github.com/conix-center/ARENA-core/issues)
- [ARENA Python issues](https://github.com/conix-center/ARENA-py/issues)
- [ATLAS Scene Locator issues](https://github.com/conix-center/ATLAS/issues)
- [ARENA Persistance issues](https://github.com/conix-center/arena-persist/issues)
- [ARENA Authentication issues](https://github.com/conix-center/ARENA-auth/issues)
- [ARENA Deployment Docker issues](https://github.com/conix-center/arena-services-docker/issues)
