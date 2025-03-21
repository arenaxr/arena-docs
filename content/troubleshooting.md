---
title: Troubleshooting
nav_order: 90
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
- Since we use WebRTC, try your browser at a third-party WebRTC test site [https://test.8x8.vc/](https://test.8x8.vc/).

## Where is my Object?
- Is the object's position below the ground? The **y** position will be negative below the default visible floor.
- Is the object's scale too big/small? Models especially have wild differences in scale, try increasing/decreasing the order of magnitude of the scale. Try a scale of **10, 1, 0.1, or 0.01**.
- Does the scene name in the URL match the scene name/topic where the object was created? e.g. URL is `https://arenaxr.org/[your username]/example` and MQTT topic published to is `realm/s/[your username]/example/o/some_object_1`.
- Does the object appear in the left column of the [A-Frame Scene Inspector](https://aframe.io/docs/1.5.0/introduction/visual-inspector-and-dev-tools.html)?

## Unity Library `arena-unity` Errors
While using the ARENA **Unity library**, You may encounter an error condition. Some of these are detailed below with some troubleshooting steps.

### Unity: HTTP Error 426 Upgrade Required
The ARENA web site will be updated from time to time, and some updates may require older versions of the `arena-unity` Unity client to be updated to communicate.
- Use the Unity app menu `Window > Package Manager` and `+ > Add package from git URL...`, use this link for the latest:
    ```
    https://github.com/arenaxr/arena-unity.git
    ```

## Python Library `arena-py` Errors
While using the ARENA **Python library**, You may encounter an error condition. Some of these are detailed below with some troubleshooting steps.

### Python: HTTP Error 426 Upgrade Required
The ARENA web site will be updated from time to time, and some updates may require older versions of the `arena-py` Python client to be updated to communicate.
- Use the `pip` Python package manager package manager to upgrade:
    ```bash
    pip install arena-py --upgrade
    ```

### Python: MQTT connect error to arenaxr.org, port=8883
If your internet connection uses a VPN or other firewall that may block port **8883**, then the secure, encrypted TLS connection for ARENA MQTT will be prevented. To resolve:
- Switch to another VPN, WiFi access point, or network connection that allows port 8883.
- Use a SSH terminal connection to another server you operate that allows port 8883.

### Python: Disconnected! Result code=1.
This means the socket connection to the ARENA MQTT broker has ended. Some possible reasons for this:
- Your network connection has ended for a variety of reasons: power dip, signal loss, or other network events. Is the server still reachable using `ping arenaxr.org`?
- Your program main thread is blocking MQTT keep-alive messages, commonly from using infinite loops like `while True:` in the main thread. Considering spawning a new thread to run your `while True:` code.

### Python: Unable to get local issuer certificate
It seems some distributions of Python may not have any certificate roots installed for SSL, especially Mac OS. To resolve, some useful troubleshooting can be found online:
- [https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)

## Web Browser Scene Errors
While visiting an ARENA scene in a **web browser**, you may encounter an error condition. Some of these are detailed below with some troubleshooting steps.

### Error: Network speed is too slow
Some elements of the scene may not have loaded if at all. You may see this error if the network speed of your current connection is too slow for the ARENA to operate. Most fixes involve switching to another network connection which may have improved bandwidth or latency. Steps to try:
- Switch to a different Wifi access point.
- Switch from wireless network connection to wired (or vice versa).
- Switch to another VPN or disable your VPN connection.

### Error: Conference stream failed
You may see other users moving in 3d, but unable to see/hear their video or audio. You may encounter this error if some ports are blocked by a VPN, firewall, or other network filter. ARENA's video conferencing system is backed by Jitsi, and requires the opening of [additional ports](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart#setup-and-configure-your-firewall) to function. Our conferencing system requires the following **ports** to be open: **80, 443, 3478, 5349, 10000**. Steps to try:
- Switch to a different Wifi access point.
- Switch to an alternate VPN channel or provider if possible.
- Disable your VPN if one is in use.

### Error: Conference server connection failed
Other users may have stopped moving completely. You may see this error if the network connection to the conferencing server has been lost. Steps to try:
- Move your wireless computer/device closer to your access point.
- Switch from wireless network connection to wired (or vice versa).
- Switch to a different Wifi access point.

### Warning: Events Publish Behavior is too high
You may see this warning when using [AR Builder (ARB)](tools/authoring) or other editor tools to edit the scene in 3d. It is a reminder that the scene's `scene-options` object is set to publish mouse events for every client and object in the scene, instead of only those chosen per object. This can lead to unnecessarily high MQTT events publish rates for complex scenes with many users.
- Scene owners, remember to restore scene options to `{"scene-options": { "clickableOnlyEvents": true }}`.
- In ARB this can be done by toggling the `edit` button off.

## I have a different problem, where can I get help?
We have a place for submitting issues and asking questions in most of our code repositories:
- [ARENA Docs issues](https://github.com/arenaxr/arena-docs/issues)
- [ARENA Website/Webserver issues](https://github.com/arenaxr/arena-web-core/issues)
- [ARENA Python issues](https://github.com/arenaxr/arena-py/issues)
- [ARENA Unity issues](https://github.com/arenaxr/arena-unity/issues)
- [ATLAS Scene Locator issues](https://github.com/arenaxr/ATLAS/issues)
- [ARENA Persistence issues](https://github.com/arenaxr/arena-persist/issues)
- [ARENA Authentication issues](https://github.com/arenaxr/arena-account/issues)
- [ARENA Deployment Docker issues](https://github.com/arenaxr/arena-services-docker/issues)
