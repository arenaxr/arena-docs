---
title: Troubleshooting
nav_order: 99
layout: default
---

# Troubleshooting
Here are some common situations which can help when programming and collaborating in the ARENA.

## Why can't I hear you?
- Don't forget to make sure your computer speakers are not Muted or have your Volume set too low.

## Can you hear/see me?
- Audio/video setups vary a lot between web browsers so this can be common.
- For **Chrome**, test your permissions and try different cameras/microphones: **chrome://settings/content/camera** and **chrome://settings/content/microphone**.
- For **Edge**, in Windows *Start > Settings > Privacy > Camera*, and toggle the switch. Try the *Microphone* setting here as well.
- For **Firefox**, test your permissions **about:preferences#privacy**, scroll down to *Permissions*, then *Camera/Microphone* and try different cameras/microphones:
- For **Safari**, navigate your menus to *Menu > Safari > Preferences... > Websites > Camera/Microphones* and try different cameras/microphones.
- Since we use WebRTC, try your browser at a third-party WebRTC test site [https://test.webrtc.org/](https://test.webrtc.org/).

## Where is my Object?
- Is the object's position below the ground? The "y" position will negative below the default visible floor.
- Is the object's scale too big/small? Models especially have wild differences in scale, try increasing/decreasing the order of magnitude of the scale. Try scale of 10, 1, 0.1, or 0.01.
- Does the scene name in the URL match the scene name/topic where the object was created? e.g. URL is `https://arenaxr.org/[your username]/example` and MQTT topic published to is `realm/s/[your username]/example/some_object_1`.
- Does the object appear in the left column of the [A-Frame Scene Inspector](https://aframe.io/docs/1.0.0/introduction/visual-inspector-and-dev-tools.html)?

## What does this scene error mean?
You may encounter an error condition due to limited hardware, memory, or network capacity. Some of these are detailed below with some troubleshooting steps.

### Error: Conference stream failed
You may encounter this error if some ports are blocked by a VPN, firewall, or other network filter. ARENA's video conferencing system is backed by Jitsi, and requires the opening of [additional ports](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart#setup-and-configure-your-firewall) to function. Our conferencing system requires the following **ports** to be open: **80, 443, 3478, 5349, 10000**. Steps to try:
- Switch to a different Wifi access point.
- Switch to an alternate VPN channel or provider if possible.
- Disable your VPN if one is in use.

### Error: Conference server connection failed
You may see this error if the network connection to the conferencing server has been lost. Steps to try:
- Move your wireless computer/device closer to your access point.
- Switch from wireless network connection to wired (or vice versa).
- Switch to a different Wifi access point.

## I have different problem, where can I get help?
We have a place for submitting issues and asking questions in most of our code repositories:
- [ARENA Docs issues](https://github.com/conix-center/ARENA/issues)
- [ARENA Website/Webserver issues](https://github.com/conix-center/ARENA-core/issues)
- [ARENA Python issues](https://github.com/conix-center/ARENA-py/issues)
- [ATLAS Scene Locator issues](https://github.com/conix-center/ATLAS/issues)
- [ARENA Persistence issues](https://github.com/conix-center/arena-persist/issues)
- [ARENA Authentication issues](https://github.com/conix-center/arena-account/issues)
- [ARENA Deployment Docker issues](https://github.com/conix-center/arena-services-docker/issues)
