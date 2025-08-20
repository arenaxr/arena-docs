---
title: Build
nav_order: 4
layout: default
parent: Unity Library
---

# Build Notes

## For All Platforms Debug Notes
1. Follow the [startup project setup](https://github.com/arenaxr/arena-unity#library-usage).
1. `Edit > Project Settings > Player`: Create a meaningful Package Name like `com.companyname.appname`...
    - `Company Name`: `companyname` (sample)
    - `Product Name`: `appname` (sample)
1. `Edit > Project Settings > Player > Graphics > Video`:
    - `Always Included Shaders` to include:
        - `Standard`
        - `Unlit/Color`
        - `glTF/PbrMetallicRoughness`
        - `glTF/PbrSpecularGlossiness`
        - `glTF/Unlit`


## Mobile Platforms Debug Notes
1. Install a good device debug logging package to your project like [LunarConsole](https://assetstore.unity.com/packages/tools/gui/lunar-mobile-console-free-82881).


## Android Debug Notes
Tested on Android 10 (API 29).

1. `Edit > Project Settings > Player > iOS > Identification`: Override default if desired:
    - `Package Name`: `com.companyname.appname` (sample)
1. `Edit > Project Settings > Player > Android > Other Settings > Identification`:
    - `Minimum API Level`: at least API 24 (for XR/ARCore).
1. `Edit > Project Settings > Player > Android > Other Settings > Configuration:`:
    - `Install Location` to: `Automatic` or `Force Internal`.
    - `Internet Access` to: `Require`.
    - `Write Permission` to: `Internal`.
1. Switch platform to `Android` and `Build and Run` the app to generate the proper Android app data files folder.


## iOS Debug Notes
Tested on iOS 15.

1. `Edit > Project Settings > Player > iOS > Identification`: Override default if desired:
    - `Bundle Identifier`: `com.companyname.appname` (sample)
1. `Edit > Project Settings > Player > iOS > Other Settings > Configuration:`:
    - `Camera Usage Description`: something like `Using iOS camera for ARENA AR`.
    - `Target minimum iOS Version`: to `11.0`.
    - `Requires ARKit support`: to Yes.
1. Switch platform to `iOS` and `Build and Run` the app to generate the proper iOS app data files folder.
