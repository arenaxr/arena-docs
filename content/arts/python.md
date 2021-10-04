---
title: Program Launch Example
nav_order: 9
layout: default
parent: ARENA Runtime Supervisor
---

Scene Edit/Program Launch Example
=================================

Quick Reference
---------------

* Scene [https://arenaxr.org/public/pytest](https://arenaxr.org/public/pytest) loads a Python program stored at the [file store](https://arenaxr.org/files), under folder boxes for user **wiselab**.
* Go to the [file store](https://arenaxr.org/files) and edit **boxes/boxes.py** to see the program code.
* Edit this scene in the [builder](https://arenaxr.org/build/), to see the program object stored.
* See the [ARTS gui](https://arenaxr.org/arts/) to see the runtimes and modules running.

Step by Step Example
--------------------

How to launch a program (e.g. **boxes/boxes.py**) in a [file store](https://arenaxr.org/files).

1\. Edit Scene: [https://arenaxr.org/build/](https://arenaxr.org/build/)

2\. Make sure the ARENA and MQTT host are **https://arenaxr.org/** and **arenaxr.org:8083**:

![](../../assets/img/arts-program/image4.png){:width="300px"}

(the ![](../../assets/img/arts-program/image5.png){:width="300px"} message indicates it successfully queried the persist db)

3\. Enter a name for your new scene (e.g. **pytest**)

![](../../assets/img/arts-program/image2.png){:width="400px"}

4\. Add a program. By selecting type “program” in the Add/Edit Object select:
![](../../assets/img/arts-program/image7.png){:width="200px"}

5\. Edit the program attributes. Make sure to assign a unique object ID (use ![](../../assets/img/arts-program/image8.png){:width="100px"}), and:

- **action** is “create”,
- **type** is “program” and
- **name** is in the form **<username in the arena store>/<folder in the ARENA store>** (e.g. **wiselab/boxes** for a program under folder **boxes** of the home folder for user **wiselab** in the ARENA store)
- **instantiate** indicates if a program instance is started for each viewer (browser) or single instance per scene
- **filename** is the program entry file (e.g. boxes.py)
- **filetype** is either Python or wasm, depending on your program
- Add environment variables and arguments as needed by the program (for example, the program might read environment variable SCENE to know its scene, then add an environment variable: SCENE=${scene}, where ${scene} will be replaced by the scene name)

{% include alert type="tip" title="note" content="
By convention, we pass programs environment variables that indicate the scene, realm and MQTT host. These are reflected in the default values of the form.
"%}

![](../../assets/img/arts-program/image6.png){:width="80%"}

6\. **Finalize by pressing the ![](../../assets/img/arts-program/image1.png){:width="150px"} button.** You should see the new program object in the scene object list:

![](../../assets/img/arts-program/image3.png){:width="80%"}

7\. Goto to the folder of the program in the [file store](https://arenaxr.org/files) and add your files there. These can be wasm programs or Python programs that use the **arena.py** library. See an example in **[wiselab/boxes](https://arenaxr.org/storemng/share/1KoiGaWq)**.

{% include alert type="warning" title="Authentication" content="
You also need to include a `requirements.txt` with your `.py` files providing the authentication version of the ARENA Python library that has at least the line:
```
arena-py
```
"%}

8\. Open the Scene using ![](../../assets/img/arts-program/image9.png){:width="200px"}at the top of the build page (the link should be something like https://arenaxr.org/[your username]/\[scene-name\])

9\. See ARTS GUI: [https://arenaxr.org/arts/](https://arenaxr.org/arts/)
