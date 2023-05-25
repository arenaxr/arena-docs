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
using UnityEngine.UI;

public class ArenaTestButton : MonoBehaviour
{
    /// <summary>
    /// Demonstrate basic usage of the ArenaUnity package.
    /// </summary>
    IEnumerator ArenaUnityBeginnerDemo()
    {
        // Only one singleton connection instance allowed per application.
        ArenaClientScene scene = ArenaClientScene.Instance;

        // Set the MQTT broker address, default: "arenaxr.org".
        scene.hostAddress = "arenaxr.org";

        // Set the namespace name for the scene, default: [your ARENA username].
        // For google authentication, this is set automatically on login and unnecessary when using your own username.
        // scene.namespaceName = "public";

        // Set the scene name for the scene, default: "example".
        scene.sceneName = "example";

        // Authenticate flow, MQTT connection flow, and Persistence download flow.
        // This will execute an asynchronous coroutine thread for these flows.
        scene.ConnectArena();
        yield return new WaitUntil(() => scene.mqttClientConnected);

        // Display the web browser GUI client URL, set after MQTT connection flow completes.
        Debug.Log($"Scene URL: {scene.sceneUrl}");

        // Create GameObject, and add ArenaObject script to manage updates, it will automatically send an MQTT create message
        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        ArenaObject arenaObject = cube.AddComponent(typeof(ArenaObject)) as ArenaObject;

        // Change the parent/name/transform, it will automatically send an MQTT update message
        cube.transform.rotation = UnityEngine.Random.rotation;

        // Publish a custom event under this client's "camera" object
        scene.PublishEvent(scene.camid, "my-custom-event-type", "{\"my-attribute\": \"my-custom-attribute\"}");

        // Publish a fully formed json object update message
        const string payload = "{\"object_id\":\"scene-options\",\"persist\":true,\"type\":\"scene-options\",\"action\":\"update\",\"data\":{\"env-presets\":{\"ground\":\"none\"}}}";
        scene.PublishObject("scene-options", payload);

        // Instantiate the callback for all messages.
        scene.OnMessageCallback = MessageCallback;
    }

    /// <summary>
    /// A delegate method used as a callback to go some special handling on incoming messages.
    /// </summary>
    public static void MessageCallback(string topic, byte[] message)
    {
        Debug.LogFormat("Message received on topic {0}: {1}", topic, System.Text.Encoding.UTF8.GetString(message));
    }

    /// <summary>
    /// Demonstrate advanced usage of the ArenaUnity package.
    /// </summary>
    IEnumerator ArenaUnityAdvancedDemo()
    {
        // Create a simple arena mqtt client and send receive messages.
        GameObject gobj = new GameObject("Arena Mqtt Client Advanced");
        MyArenaClient client = gobj.AddComponent(typeof(MyArenaClient)) as MyArenaClient;

        // Setup a connection using a custom namespace and anonymous authentication.
        client.hostAddress = "arenaxr.org";
        //client.authType = ArenaMqttClient.Auth.Manual;

        // Store any local jwt tokens here, before auth starts.
        // Derive the local path from the next line.
        // string localMqttPath = Path.Combine(client.appFilesPath, ".arena_mqtt_auth");

        // Authenticate flow, MQTT connection flow.
        client.ConnectArena();
        yield return new WaitUntil(() => client.mqttClientConnected);

        // Display the MQTT JWT permission payload/claims, set after authentication flow completes.
        Debug.Log($"Permissions: {client.permissions}");

        // Custom MQTT pub/sub
        string[] topics = new string[] { "my/custom/topic/#" };
        client.Subscribe(topics);

        yield return new WaitForSeconds(2);
        client.Publish("my/custom/topic/channel/device-888", System.Text.Encoding.UTF8.GetBytes("some payload"));
    }

    public class MyArenaClient : ArenaMqttClient
    {
        public void ConnectArena()
        {
            // start auth flow and MQTT connection
            StartCoroutine(Signin());
        }

        // Directly override the incoming message handler.
        protected override void DecodeMessage(string topic, byte[] message)
        {
            Debug.LogFormat("Message received on topic {0}: {1}", topic, System.Text.Encoding.UTF8.GetString(message));
        }
    }
}
```
