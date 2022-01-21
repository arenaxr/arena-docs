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

## Hierarchy Window: Arena Client Runtime
Here, any ARENA objects are highlighted in <span style="color: green;">green text</span>, and the **Play** button should open the list of ARENA objects automatically.
### Sorting Objects
1. Settings:`Edit > Preferences > General > Enable Alpha Numeric Sorting`
1. Change the sorting mode with top right button of the `Hierarchy` window.
    ![/assets/img/unity/alphanumeric-sort.png](/assets/img/unity/alphanumeric-sort.png)

## Game Window
This is a display of the currently focused Camera in the scene.
### Navigation
Set the `Inspector`: `ArenaClient` object option `Camera Auto Sync` to true, enter the ARENA scene web page, then navigation in the ARENA will also move the `Game` view.
### Other Cameras
In the `Inspector`: `ArenaClient` object option `Camera For Display`, select from other cameras present on the MQTT bus. **Caution**: Some GLTF models also come with embedded Camera objects which may show up here.

## Scene Window
This is the editor's view of the scene, allowing you to manipulate object Transforms graphically using toolbar options.
### Navigation
Use the [Unity controls](https://docs.unity3d.com/Manual/SceneViewNavigation.html).

## Project Window
Any imported models, images or other resources are stored locally here in the `Assets/ArenaUnity` folder, mimicking their own URL structure. You can review sub-elements of GLTF models here and their animations. To save space and download time, any video and audio files are not yet imported.

## Console Window
The Console will output status, warning, and error logging here as well as MQTT messages you specify here according to the **Log Mqtt** options specified in the next section.

## Inspector Window: ArenaClient
The `ArenaClient` Script controls the connection and authentication to the ARENA MQTT broker, as well as some client-side ARENA scene state.

name | type | default | description
-- | -- | -- | --
**Signout** | button | -- | Manual button to signout from the ARENA and stop the Runtime.
Script | ArenaClient | -- | The script instance to manage the MQTT runtime.
**Broker Address** | string | arenaxr.org | Host name of the ARENA MQTT broker
**Namespace Name** | string | null | Namespace (automated with username), but can be overridden
**Scene Name** | string | example | Name of the scene, without namespace ('example', not 'username/example'
**Scene Url** | string | null | Browser URL for the scene
**Camera For Display** | Camera | MainCamera | Cameras for Display 1
**Camera Auto Sync** | bool | false | Synchronize camera display to first ARENA user in the scene
**Log Mqtt Objects** | bool | false | Console log MQTT object messages
**Log Mqtt Users** | bool | false | Console log MQTT user messages
**Log Mqtt Events** | bool | false | Console log MQTT client event messages
**Log Mqtt Non Persist** | bool | false | Console log MQTT non-persist messages
**Transform Publish Interval** | int | 30 | Publish per frames frequency to publish detected transform changes (0 to stop)
**Email** | string | null | Authenticated user email account
**Permissions** | string | null | MQTT JWT Auth Payload and Claims

## Inspector Window: ArenaObject
The `ArenaObject` Script monitors Transform and Name changes to an ARENA object, as well as a few other requests, like delete. It also allows the user to manually edit and update ARENA object JSON message data.

name | type | default | description
-- | -- | -- | --
**Publish Unity Data** | button | -- | Manual button to publish an object update. Enabled only for ARENA message type `object` (transform changes will update automatically).
Script | ArenaObject | -- | The script instance to manage an ARENA object runtime.
**Message Type** | string | object | Message type in persistance storage schema
**Persist**| bool | true | Persist this object in the ARENA server database (default true = persist on server)
**Json Data** | string | null | ARENA JSON-encoded message `data` attributes.
**Publish Json Data** | button | -- | Manual button to publish edited `Json Data`. Enabled when `Json Data` is well formatted.

## ARENA Mesh Tool

The ARENA Mesh Tool is a Unity `CustomTool` which allows you to manipulate the `Mesh` dimensions of ARENA primitive geometries without having to modify the `Scale` component to chang the size of an object and risk inheriting that scale for any child objects.

<img alt="" src="/assets/img/unity/arena-mesh-tool.gif">
