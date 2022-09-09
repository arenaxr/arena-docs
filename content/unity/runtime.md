---
title: Runtime
nav_order: 2
layout: default
parent: Unity Library
---

# ARENA-Unity Runtime
The ArenaUnity package can be used to build new interfaces to collaboratively connect and edit ARENA scenes. Be sure to use the [project setup instructions](/content/unity) to install the package. For the `Editor` interface, see the [ARENA Unity Editor](/content/unity/editor) instructions.

## Architecture
- The `.NET 4.x` API level is required since ARENA JSON payloads are fluid, and we cannot keep up with schema serialization definitions by developers and users. So we use the `dynamic` object instantiations offered in the .Net 4 API to test for JSON attributes at runtime.
- **ArenaClientScene** is a Singleton class, meant to be instantiated only once to control the auth and MQTT communication flow.
- **ArenaObject** is a class for each GameObjects to publish to the ARENA, accessing the publish and subscribe MQTT methods through **ArenaClientScene.Instance**. `ArenaClientScene` will manage attaching `ArenaObject` to Unity GameObjects for you.

## Example
The example code below contains both synchronous and asynchronous APIs, so please plan your application events accordingly.

```csharp
using System.Collections;
using ArenaUnity;
using UnityEngine;

/// <summary>
/// Demonstrate basic usage of the ArenaUnity package.
/// </summary>
IEnumerator ArenaUnityBeginnerDemo()
{
    // Only one singleton connection instance allowed per application.
    ArenaClientScene scene = ArenaClientScene.Instance;

    // Set the MQTT broker address, default: "arenaxr.org".
    scene.hostAddress = "mqtt.arenaxr.org";

    // Set the namespace name for the scene, default: [your ARENA username].
    // For google authentication, this is set automatically on login and unnecessary when using your own username.
    // scene.namespaceName = "public";

    // Set the scene name for the scene, default: "example".
    scene.sceneName = "example";

    // Authenticate flow, MQTT connection flow, and Persistence download flow.
    // This will execute an asynchronous coroutine thread for these flows.
    scene.ConnectArena();
    yield return new WaitUntil(() => scene.mqttClientConnected);

    // create GameObject, and add ArenaObject script to manage updates, it will automatically send an MQTT create message
    GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
    ArenaObject arenaObject = cube.AddComponent(typeof(ArenaObject)) as ArenaObject;

    // change the parent/name/transform, it will automatically send an MQTT update message
    cube.transform.rotation = Random.rotation;
}

/// <summary>
/// Demonstrate advanced usage of the ArenaUnity package.
/// </summary>
IEnumerator ArenaUnityAdvancedDemo()
{
    // Only one singleton connection instance allowed per application.
    ArenaClientScene scene = ArenaClientScene.Instance;

    // Setup a connection using a custom namespace and anonymous authentication.
    scene.hostAddress = "mqtt.arenaxr.org";
    scene.namespaceName = "public";
    scene.sceneName = "example";
    scene.authType = ArenaMqttClient.Auth.Anonymous;

    // Authenticate flow, MQTT connection flow, and Persistence download flow.
    scene.ConnectArena();
    yield return new WaitUntil(() => scene.mqttClientConnected);

    // Display the MQTT JWT permission payload/claims, set after authentication flow completes.
    Debug.Log($"Permissions: {scene.permissions}");

    // Display the web browser GUI client URL, set after MQTT connection flow completes.
    Debug.Log($"Scene URL: {scene.sceneUrl}");

    // Custom MQTT pub/sub
    string[] topics = new string[] { "my/custom/topic/#" };
    scene.Subscribe(topics);
    scene.Publish("my/custom/topic/channel/device-888", System.Text.Encoding.UTF8.GetBytes("some payload"));
    scene.PublishEvent("{'some_attribute': 'some event data'}");
    scene.Unsubscribe(topics);

    // Disconnect from the MQTT broker, and remove local Persistence objects.
    scene.DisconnectArena();

    // Remove ARENA authentication.
    scene.SignoutArena();
}
```
