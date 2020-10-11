---
title: Troubleshooting
nav_order: 99
layout: default
---

# Troubleshooting
Here are some common situations which can help when programming and collaborating in the ARENA.

## Where is my Object?
- Is the object's position below the ground? The "y" position will negative below the default visible floor.
- Is the object's scale too big/small? Models especially have wild differences in scale, try increasing/decreasing the order of magnitude of the scale. Try scale of 10, 1, 0.1, or 0.01.
- Does the scene name in the URL match the scene name/topic where the object was created? e.g. URL is `https://arena.andrew.cmu.edu/?scene=example` and MQTT topic published to is `realm/s/example/some_object_1`.

## Can you see me? Can you hear me?
- Audio/video setups vary a lot between web browsers so this can be common.
- Don't forget to make sure your computer speakers are not Muted or have your Volume set too low.
- For **Chrome**, test your permissions and try different cameras/microphones: **chrome://settings/content/camera** and **chrome://settings/content/microphone**.
- For **Edge**, test your permissions and try different cameras/microphones: **edge://settings/content/camera** and **edge://settings/content/microphone**.
- For **Firefox**, test your permissions **about:preferences#privacy**, scroll down to *Permissions*, then *Camera/Microphone* and try different cameras/microphones: 
- For **Safari**, navigate your menus to *Menu > Safari > Preferences... > Websites > Camera/Microphones* and try different cameras/microphones.
- Since we use WebRTC, try your browser at a third-party WebRTC test site [https://test.webrtc.org/](https://test.webrtc.org/).

## I have different problem, where can I get help?
We have a place for submitting issues and asking questions in most of our code repositories:
- [ARENA Docs issues](https://github.com/conix-center/ARENA/issues)
- [ARENA Website/Webserver issues](https://github.com/conix-center/ARENA-core/issues)
- [ARENA Python issues](https://github.com/conix-center/ARENA-py/issues)
- [ATLAS Scene Locator issues](https://github.com/conix-center/ATLAS/issues)
- [ARENA Persistance issues](https://github.com/conix-center/arena-persist/issues)
- [ARENA Authentication issues](https://github.com/conix-center/ARENA-auth/issues)
- [ARENA Deployment Docker issues](https://github.com/conix-center/arena-services-docker/issues)
