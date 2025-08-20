---
title: Unity Library
nav_order: 7
layout: default
has_children: true
---

# arena-unity
Unity C# library for editing scenes and creating applications for the ARENA.
- [**arena-unity**](https://github.com/arenaxr/arena-unity) Unity repository

<img alt="" src="/assets/img/unity/arena-unity-demo.gif">

## Library Usage:
1. Open a new or existing Unity project. **Unity 2022.3+ supported.**
1. `Edit > Project Settings > Player > PC, Mac & Linux Standalone > Resolution and Presentation > Resolution`:
    - `Run In Background` set to true.
1. You may need to install [`git`](https://git-scm.com/) if it doesn't come preinstalled on your OS (Windows 10).
1. Open `Window > Package Manager` and `+ > Add package from git URL...`, use this link for the latest:
    ```
    https://github.com/arenaxr/arena-unity.git
    ```
1. Create an empty GameObject to use as ARENA client root, rename it to something meaningful, like: `ARENA`.
1. Select the `ARENA` GameObject and press `Add Component` to add the `ArenaClientScene` script.
1. Modify the the inspector variables for the `ArenaClientScene` script to change **host, scene, namespace** as you wish.
1. Press **Play**.
1. The auth flow will open a web browser page for you to login, if you haven't yet.

## Runtime (Play)
See [operational documentation](/content/unity/runtime).
