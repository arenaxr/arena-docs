---
title: Unity Developers
nav_order: 10
layout: default
parent: Unity Library
---

# Unity Developers

## Architecture
- The `.NET 4.x` API level is required since ARENA JSON payloads are fluid, and we cannot keep up with schema serialization definitions by developers and users. So we use the `dynamic` object instantiations offered in the .Net 4 API to test for JSON attributes at runtime.
- **ArenaClient** is a Singleton class, meant to be instantiated only once to control the auth and MQTT communication flow.
- **ArenaObject** is a class for each GameObjects to publish to the ARENA, accessing the publish and subscribe MQTT methods through **ArenaClient.Instance**. `ArenaClient` will manage attaching `ArenaObject` to Unity GameObjects for you.

## Library Development:
Almost all steps to develop the library are the same, just prepare a development project using the [Library Usage](#library-usage) steps, except import the `ARENA Unity` package locally instead of from a Git URL.
1. Clone this repo locally.
1. Open `Window > Package Manager` and `+ > Add package from disk...`, use your local repo location.
1. Create changes on a development fork or branch and submit a Pull Request.

## Debugging in VS Code
1. Install the extension https://marketplace.visualstudio.com/items?itemName=Unity.unity-debug.
1. Add a `.vscode/launch.json` file inside your local copy of this repo with at least:
    ``` json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Unity Editor",
                "type": "unity",
                "request": "launch"
            }
        ]
    }
    ```
1. Set breakpoints and run debug configuration `Unity Editor`.
1. Press **Play**.
1. Other useful setup here: https://code.visualstudio.com/docs/other/unity.
