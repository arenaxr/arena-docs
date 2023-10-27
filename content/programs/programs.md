---
title: Add Programs Example
nav_order: 1
layout: default
parent: ARENA Programs
---

## Adding a Hosted ARENA Program: Step by Step Example

The following instructions show how to host an ARENA program using a simple example python scripts called [**boxes.py**](https://arenaxr.org/store/users/wiselab/py/boxes/boxes.py).

## 1. Add the files.

Navigate to the [file store](https://arenaxr.org/files). You might be asked to login. In your home folder, create a folder called **programs** (the folder name can be anything; this is just for the sake of our example). Later, we will need refer to this folder in the form **\<username-or-namespace\>/\<folder-path\>**. You can see your username on the upper left, in this example, we would refer to the folder as **cmu/programs** (**cmu** is  the user in our example). **Add your program files (in this case, the `boxes.py` script) to this folder**.

<img src="/assets/img/programs/filestore-userhome.jpg"
style="border:1px solid;" />

{% include alert type="warning" title="Authentication" content="
You also need to include a `requirements.txt` with your `.py` files providing the authentication version of the ARENA Python library that has at least the line:
```
arena-py
```
"%}

## 2. Add a program object to your scene.

Open the [scene builder](/content/overview/build) and select the scene that you want to add the program to. Now, add a **Program** object by selecting type “program” in the Add/Edit Object select:

<img src="/assets/img/programs/image7.png"
style="width:3in;border:1px solid;" />

## 3. Edit the program attributes.

Make sure to assign a unique object ID (use ![](/assets/img/programs/image8.png){:width="100px"}), and:

- **action** is `create`
- **type** is `program`
- **name** is the program name in the form **\<username-or-namespace\>/\<program-name\>**
- **instantiate** indicates if a program instance is started for each viewer (browser) or single instance per scene;
- **filename** is the path to the program entry file in the form **\<username-or-namespace\>**/**\<path-to-program-entryfile\>**. In this example: **cmu/programs/boxes.py**
- **filetype** is either python (`PY`) or wasm (`WA`), depending on your program. In this case, `PY`.
- Add environment variables and arguments as needed by the program (for example, the program might read environment variable `SCENE` to know its scene, then add an environment variable: `SCENE=${scene}`, where `${scene}` will be replaced by the scene name)

{% include alert type="tip" title="note" content="
By convention, we pass programs environment variables that indicate the scene, realm and MQTT host. These are reflected in the default values of the form.
"%}

- **parent** is the runtime where the module should run; usually this is left blank, but due to current limitations of our deployment, this must be **pytest** (this is the name of the runtime that currently supports ARENA programs).

{% include alert type="tip" title="note" content="
Please set parent to **pytest** so that your programs are dispatched to this runtime.
"%}

<img src="/assets/img/programs/image6.png"
style="width=80%;border:1px solid;" />

This is the corresponding object JSON:

```json
{
  "object_id": "1c96947e-351c-47f5-8801-65e5cd0e778d",
  "action": "create",
  "persist": true,
  "type": "program",
  "data": {
    "name": "cmu/boxes",
    "instantiate": "single",
    "filename": "cmu/programs/boxes.py",
    "filetype": "PY",
    "parent": "pytest",
    "env": [
      "MID=${moduleid}",
      "SCENE=${scene}",
      "NAMESPACE=${namespace}",
      "MQTTH=${mqtth}",
      "REALM=realm"
    ]
  }
}
```

## 4. Save the program object.

**Finalize by pressing the "Add/Update Object" button.** You should see the new program object in the scene object list:

<img src="/assets/img/programs/image3.png"
style="width=80%;border:1px solid;" />

## 5. Open the scene

Open the Scene using ![](/assets/img/programs/image9.png){:width="200px"}at the top of the build page (the link should be something like https://arenaxr.org/[your username]/\[scene-name\])

## 6. See the details of the ARENA runtime

You can use the [ARENA runtime dashboard](https://arenaxr.org/programs/) to see details of the runtimes and programs running.
