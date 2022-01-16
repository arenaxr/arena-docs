---
title: Editor Runtime
nav_order: 1
layout: default
parent: Unity Library
---

# ARENA-Unity Documentation

## Signin
In the Unity Editor, pressing `Play` will begin the signin authorization flow.

## Signout
Two options:
- **Editor:** Select the menu item `ARENA > Signout`.
- **Runtime:** Click the `Signout` button on the `ArenaClient` Component.

## Navigation
You can use the `Scene` or `Game` tabs to navigate.
- **Scene**: Use the [Unity controls](https://docs.unity3d.com/Manual/SceneViewNavigation.html).
- **Game**: Set the Unity Editor option `Camera Auto Sync` to true, enter the ARENA scene web page, then navigation in the ARENA will also move the `Game` view.

## Sorting Objects
1. Settings:`Edit > Preferences > General > Enable Alpha Numeric Sorting`
1. Change the sorting mode with top right button of the `Hierarchy` window.
    ![/assets/img/unity/alphanumeric-sort.png](/assets/img/unity/alphanumeric-sort.png)

## Exporting Unity Objects as GLTF

Since the ARENA uses GLTF models as a web-friendly format, it is useful to know how to export your Unity work as a GLTF model, which the ARENA web can render.
1. We recommend using 2 Scenes separately: a `Design View` scene and an `ARENA View` scene.
1. In scene `Design View`, use an available plug-in to [export your model](/content/3d-content/unity) to GLTF file format.
1. Store this model online, like the on the [ARENA File Store](/content/interface/filestore) or [Dropbox](/content/overview/build#add-new-objects).
1. In scene  `ARENA View` [load your ARENA scene](/content/unity).
1. Import your model, adding an ARENA object using the menu `GameObject > ARENA > GLTF Model` and provide your model URL.

## During Runtime (Play)

1. If objects are stored in the ARENA Persistence Database, they will be child objects of the `ARENA` GameObject.
1. You may create or change an object and if it is a child of the `ARENA` GameObject, its properties will be published to the ARENA Persistence Database.
1. Incoming authorized messages may also add/change/remove your ARENA Unity objects.

![/assets/img/unity/unity-desktop.png](/assets/img/unity/unity-desktop.png)

## ArenaClient Script

name | type | default | description
-- | -- | -- | --
Signout | button | -- | Manual button to signout from the ARENA and stop the Runtime.
Script | ArenaClient | -- | The script instance to manage the MQTT runtime.
Broker Address | string | arenaxr.org | Host name of the ARENA MQTT broker
Namespace Name | string | null | Namespace (automated with username), but can be overridden
Scene Name | string | example | Name of the scene, without namespace ('example', not 'username/example'
Scene Url | string | null | Browser URL for the scene
Camera For Display | Camera | MainCamera | Cameras for Display 1
Camera Auto Sync | bool | false | Synchronize camera display to first ARENA user in the scene
Log Mqtt Objects | bool | false | Console log MQTT object messages
Log Mqtt Users | bool | false | Console log MQTT user messages
Log Mqtt Events | bool | false | Console log MQTT client event messages
Log Mqtt Non Persist | bool | false | Console log MQTT non-persist messages
Transform Publish Interval | int | 30 | Publish per frames frequency to publish detected transform changes (0 to stop)
Email | string | null | Authenticated user email account
Permissions | string | null | MQTT JWT Auth Payload and Claims

## ArenaObject Script

name | type | default | description
-- | -- | -- | --
Publish Object Update | button | -- | Manual button to publish an object update (transform changes will update automatically)
Script | ArenaObject | -- | The script instance to manage an ARENA object runtime.
Message Type | string | object | Message type in persistance storage schema
Persist | bool | true | Persist this object in the ARENA server database (default true = persist on server)
Json Data | string | null | ARENA JSON-encoded message (debug only for now)
