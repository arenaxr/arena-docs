---
title: Build
nav_order: 4
layout: default
parent: Unity Library
---

# Build Notes

## For All Platforms Debug Notes
1. Follow the [startup project setup](https://github.com/conix-center/ARENA-unity#library-usage).
1. `Edit > Project Settings > Player`: Create a meaningful Package Name like `com.companyname.appname`...
    - `Company Name`: `companyname` (sample)
    - `Product Name`: `appname` (sample)
1. `Edit > Project Settings > Player > Graphics > Video`:
    - `Always Included Shaders` to include:
        - `Standard`
        - `Unlit/Color`
        - `GLTFUtility/Standard (Metallic)`
        - `GLTFUtility/Standard Transparent (Metallic)`
        - `GLTFUtility/Standard (Specular)`
        - `GLTFUtility/Standard Transparent (Specular)`


## Mobile Platforms Debug Notes
1. Install a good device debug logging package to your project like [LunarConsole](https://assetstore.unity.com/packages/tools/gui/lunar-mobile-console-free-82881).


## Android Debug Notes
Tested on Android 10 (API 29).

1. `Edit > Project Settings > Player > iOS > Identification`: Override default if desired:
    - `Package Name`: `com.companyname.appname` (sample)
1. `Edit > Project Settings > Player > Android > Other Settings > Identification`:
    - `Minimum API Level`: at least API 24 (for XR/ARCore).
1. `Edit > Project Settings > Player > Android > Other Settings > Configuration:`:
    - `Api Compatibility Level` to: `.NET 4.x`.
    - `Install Location` to: `Automatic` or `Force Internal`.
    - `Internet Access` to: `Require`.
    - `Write Permission` to: `Internal`.
1. `Edit > Project Settings > Player > Android > Other Settings > Script Compilation`:
    - `Scripted Define Symbols` to include:
        - `SSL`
1. Switch platform to `Android` and `Build and Run` the app to generate the proper Android app data files folder.
1. **[Daily Temporary]**: Switch platform to `PC, Mac & Linux Standalone`.
1. **[Daily Temporary]**: Click the `Play` button to update the MQTT Token for the desktop.
1. **[Daily Temporary]**: Either...
    - Run the bash script `./Tests/Auth/android-add-auth.sh com.companyname.appname` to copy the desktop MQTT auth token to the Android app file storage.
    - Use `Windows Explorer` or `MacOS Android File Transfer` to copy the file `.arena_mqtt_auth` from desktop path`~/.arena/unity/arenaxr.org/s/.arena_mqtt_auth` to device path `/storage/emulated/0/Android/data/com.companyname.appname/files/.arena_mqtt_auth`.
1. Switch platform to `Android` and `Build and Run` the app.
1. The library will use a local file if it exists for auth at: `/storage/emulated/0/Android/data/com.companyname.appname/files/.arena_mqtt_auth`.
1. **[Eventually]**: To use the default Android-only auth flow, remove this local token from the device with `./Tests/Auth/android-remove-auth.sh com.companyname.appname`.


## iOS Debug Notes
Tested on iOS 15. **NOTE: iOS builds are currently non-functional at runtime due to use of `dynamic` objects as they won't cross-compile. Status: https://github.com/conix-center/ARENA-unity/issues/22.**

1. `Edit > Project Settings > Player > iOS > Identification`: Override default if desired:
    - `Bundle Identifier`: `com.companyname.appname` (sample)
1. `Edit > Project Settings > Player > iOS > Other Settings > Configuration:`:
    - `Api Compatibility Level` to: `.NET 4.x`.
    - `Camera Usage Description`: something like `Using iOS camera for ARENA AR`.
    - `Target minimum iOS Version`: to `11.0`.
    - `Requires ARKit support`: to Yes.
1. `Edit > Project Settings > Player > iOS > Other Settings > Script Compilation`:
    - `Scripted Define Symbols` to include:
        - `SSL`
1. Switch platform to `iOS` and `Build and Run` the app to generate the proper iOS app data files folder.
1. **[Daily Temporary]**: Switch platform to `PC, Mac & Linux Standalone`.
1. **[Daily Temporary]**: Click the `Play` button to update the MQTT Token for the desktop.
1. **[Daily Temporary]**: Use `iTunes File Sharing` or `Windows Explorer` or `MacOS Finder` to copy the file `.arena_mqtt_auth` from desktop path`~/.arena/unity/arenaxr.org/s/.arena_mqtt_auth` to device path `appname/.arena_mqtt_auth`.
1. Switch platform to `iOS` and `Build and Run` the app.
1. The library will use a local file if it exists for auth at the iOS `appname` Files path: `appname/.arena_mqtt_auth`.
1. **[Eventually]**: To use the default iOS-only auth flow, remove this local token from the device by using `Windows Explorer` or `MacOS Finder` to delete this entire folder `appname` from your device.
