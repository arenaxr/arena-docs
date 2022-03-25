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
- **ArenaClient** is a Singleton class, meant to be instantiated only once to control the auth and MQTT communication flow.
- **ArenaObject** is a class for each GameObjects to publish to the ARENA, accessing the publish and subscribe MQTT methods through **ArenaClient.Instance**. `ArenaClient` will manage attaching `ArenaObject` to Unity GameObjects for you.

## Example
The example code below contains both synchronous and asynchronous APIs, so please plan your application events accordingly.

```csharp
using ArenaUnity;

/// <summary>
/// Demonstrate usage of the ArenaUnity package.
/// </summary>
void ArenaUnityTestDemo()
{
    // Only one singleton connection instance allowed per application.
    ArenaClient scene = ArenaClient.Instance;

    // Set the MQTT broker address, default: "arenaxr.org".
    scene.brokerAddress = "arenaxr.org";

    // Set the namespace name for the scene, default: [your ARENA username].
    scene.namespaceName = "public";

    // Set the scene name for the scene, default: "example".
    scene.sceneName = "example";

    // Authenticate flow, MQTT connection flow, and Persistence download flow.
    // This will execute an asynchronous coroutine thread for these flows.
    // TODO: Check MQTT connection state with scene.mqttClientConnected.
    scene.ConnectArena();

    // Display the MQTT JWT permission payload/claims, set after authentication flow completes.
    Debug.Log($"Permissions: {scene.permissions}");

    // Display the MQTT broker connection state, true after MQTT connection flow completes.
    Debug.Log($"MQTT Connected?: {scene.mqttClientConnected}");

    // Display the web browser GUI client URL, set after MQTT connection flow completes.
    Debug.Log($"Scene URL: {scene.sceneUrl}");

    // Disconnect from the MQTT broker, and remove local Persistence objects.
    scene.DisconnectArena();

    // Remove ARENA authentication.
    scene.SignoutArena();
}
```
