---
title: Platforms
nav_order: 2
layout: tutorial
parent: MR Experiences
---

# Supported Platforms

Mixed Reality experiences in ARENA require a WebXR-compatible browser, which currently includes Edge (desktop), Chrome (desktop and mobile), Firefox (desktop and mobile; not enabled by default), among others as shown [here](https://caniuse.com/webxr). Note that these include browsers that can run in many AR and VR headsets. For example, Oculus/Meta and Magic Leap's browsers are based on the open-source codebase of Chrome (Chromium) and include WebXR support. See below for a summary table of supported browsers and platforms.

Additionally, and to prototype the needs for future browser platforms, we are also maintaining **[XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989)**, a custom version of Firefox for iOS (based off [WebXRViewer](https://apps.apple.com/us/app/webxr-viewer/id1295998056)). Both [XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) and [WebXRViewer](https://apps.apple.com/us/app/webxr-viewer/id1295998056) support ARENA's computer vision pipeline. In addition, the team used [XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) to experiment with other features, such as [spoof-resilient AR anchors](https://wise.ece.cmu.edu/projects/glitter.html).

## Browser Support

The following table summarizes the browsers, platforms and support for ARENA's capabilities. Where available, the **details/settings** link provides more details about the specific browser and pltaforms.

| Browser                                           | MR Experiences (WebXR support)                  | ARENA CV (Optical Markers)<sup>1</sup>                                        |
| ------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------ |
| XRBrowser ([details/settings](#xrbrowser-ios)) <sup>ios</sup>             | Mobile/Tablet (iOS)                             | <span style="color:green">Supported</span>             |
| Mozilla WebXRViewer ([details/settings](#webxrviewer-ios)) | Mobile/Tablet (iOS)                             | <span style="color:green">Supported</span>             |
| Chrome ([details/settings](#chrome-android-and-more)) <sup>android</sup>    | Mobile/Tablet (Android) and desktop             | <span style="color:green">Supported</span><sup>2</sup>  |
| Mozilla Firefox                                   | Mobile/Tablet (Android) and desktop<sup>3</sup> | <span style="color:red">Not supported</span>           |
| Microsoft Edge ([details/settings](#edge))                                   | Mobile/Tablet, desktop and HoloLens         | <span style="color:green">Supported</span>           |
| Safari                                            | Desktop<sup>3</sup>                             | <span style="color:red">Not supported</span>           |
| Oculus Browser ([details/settings](#oculus-browser-quest-quest-2-and-more))                                    | Oculus headsets (e.g. Quest, Quest 2)           | <span style="color:red">Not supported</span>           |
| Helio ([details/settings](#oculus-browser-quest-quest-2-and-more))                                            | Magic Leap                                      | <span style="color:green">Supported</span>             |

<sup>1</sup> ARENA Computer Vision pipeline support is required for optical markers, and it will default to process the default camera facing the environment in each different device (the back camera in phones/tablets and the front camera facing the environement on AR headsets).<br/>
<sup>2</sup> Chrome Beta only.<br/>
<sup>3</sup> Not enabled by default.<br/>
<sup>ios</sup> Preferred iOS Browser. Our fork of Mozila's WebXRViewer.<br/>
<sup>android</sup> Preferred Android Browser.<br/>

### XRBrowser (iOS)

[XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) is the preferred Browser to use with ARENA in iOS. It can be installed from the [App Store](https://apps.apple.com/us/app/xr-browser/id1588029989).

This Browser is a fork of the experimental [Mozilla WebXRViewer (XR version of Firefox)](#webxrviewer-ios) that fixes several bugs and natively supports our computer vision pipeline.

### Chrome (Android, and more)

Currently (December 2021), only [Chrome Beta](https://www.google.com/chrome/beta/) has experimental support for [WebXR's raw camera access](https://chromestatus.com/feature/5759984304390144), which is required for ARENA's computer vision processing pipeline. We expect this feature to be rolled over into the stable release soon.

Make sure that the `chrome://flags/#webxr` (paste this into your URL bar) flag is enabled (since late 2019, Chrome v79, this should be enabled by default; please update chrome otherwise).

### WebXRViewer (iOS)

While we recommend using [XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) on iOS, for those who want to use the original Mozilla version, **you need to apply a few setting configuration updates**.

Mozilla's WebXRViewer viewer can be installed from the [App Store](https://apps.apple.com/us/app/webxr-viewer/id1295998056). After installing WebXRViewer, go to 'Settings -> XRViewer' and change:

##### WebXR Polyfill URL:  ```https://mrenaxr.org/webxrios.js``` or ```https://mrenaxr.org/vendor/webxr-webxrviewer-ios.js```

##### Always Allow World Sensing:```Yes```

![img](../../assets/img/localization/webxrviewer-settings.png)

### Edge

TBA

### Oculus Browser (Quest, Quest 2 and more)

To try ARENA in VR, you can use the Oculus Browser (*tested on the Quest 2*) and enter the scene URL. Be patient while the scene loads and the:
1. click “Enter” on the normal AV dialog box
2. Unmute mic BEFORE entering VR
3. Click the <button type="button" name="button" class="btn fs-3 ">VR</button> button in the lower right to enter immersive mode

##### Moving around: 
A forward push on the left hand rocker brings up the teleportation ring. Clicking the rocker left and right rotates.

<img src="/assets/img/mr/quest-2.png" width="500"/>

### Helio (Magic Leap)

Helio is Magic Leap’s web browser available on Magic Leap devices. Follow [these steps to open Helio and navigate to a website](https://developer.magicleap.com/en-us/learn/guides/debug-web-content), which we reproduce here for ease of access:

> 1. In the Magic Leap device, hold down the Home Button on the Control to show The Launcher. A circle of icons appear in the view.
>
> 2. Use the Control pointer or swipe on the touchpad to navigate to the Helio app in The Launcher. Press the trigger on the Control to select it. The Helio app launches.
>
> 3. Use the Control or swipe on the touchpad to navigate to the URL bar at the top of the Helio window.
> 
> 4. Press the trigger on the Control to select the URL bar. A virtual keyboard appears that you can use to enter a URL address. You can also use Magic Leap Mobile App to enter text from your mobile device. See [Magic Leap Mobile App for more information](https://developer.magicleap.com/en-us/learn/guides/magic-leap-mobile-app).
> 
> 5. Enter this page’s URL and see it display on the Magic Leap device.
