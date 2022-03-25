---
title: Unity Library
nav_order: 7
layout: default
has_children: true
---

# ARENA-unity
Unity C# library for editing scenes and creating applications for the ARENA.

<img alt="" src="/assets/img/unity/arena-unity-demo.gif">

## Library Usage:
1. Open a new or existing Unity project. **Unity 2019.4+ supported.**
1. `Edit > Project Settings > Player > PC, Mac & Linux Standalone > Other Settings > Configuration`:
    - `Api Compatibility Level` to: `.NET 4.x`.
1. `Edit > Project Settings > Player > PC, Mac & Linux Standalone > Other Settings > Script Compilation`:
    - `Scripted Define Symbols` to include:
        - `SSL`
1. You may need to install [`git`](https://git-scm.com/) if it doesn't come preinstalled on your OS (Windows 10).
1. Open `Window > Package Manager` and `+ > Add package from git URL...`, use this link:
    ```
    https://github.com/conix-center/ARENA-unity.git#0.0.13
    ```
1. Create an empty GameObject to use as ARENA client root, rename it to something meaningful, like: `ARENA`.
1. Select the `ARENA` GameObject and press `Add Component` to add the `ArenaClient` script.
1. Modify the the inspector variables for the `ArenaClient` script to change **host, scene, namespace** as you wish.
1. Press **Play**.
1. The auth flow will open a web browser page for you to login, if you haven't yet.

## Runtime (Play)
See [operational documentation](/content/unity/runtime).
