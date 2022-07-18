---
title: Blender Add-on
layout: default
parent: 3D Content
---

# ARENA Blender Add-on

You can use the [ARENA Blender add-on](https://github.com/arenaxr/blender-addon) to import/export scenes. *For now, only exports.*. 

The Add-on exports the root objects in a scene into separate GLTF files and creates a JSON file describing the scene in a format that ARENA can import. The folder created for the exported scene can then be uploaded to [ARENA filestore](http://arenaxr.org/files) (typically at '<filestore-home>/blender-exports/exported-bolder') and imported using the [build webpage](https://arenaxr.org/build/).
  
# Install

1. Download [`blender-arena-export.py`](https://raw.githubusercontent.com/arenaxr/blender-addon/main/blender-arena-export.py)
2. In Blender, go to Edit -> Preferences. In the **Add-ons** section, use the **Install…** button and Browse the filesystem to select the `blender-arena-export.py` add-on file and press **Install**.
3. Once installed, don't forget **to enable the add-on**:
<img src="https://user-images.githubusercontent.com/3504501/138316257-56ac2bfb-73db-4877-a4d3-cdfaf2138bd6.png" width="500">
4. You can confirm the Add-on is installed by seeing the new menu entry at File -> Export -> Export to ARENA.

# Use the Add-on

## Export

The Add-on exports the root objects in a scene into seperate GLTF files. For example, exporting the folowing scene:
<img src="https://user-images.githubusercontent.com/3504501/138322830-0ca41b10-e1bd-4610-aa07-caf02b456e27.png" width="300">

Will create three GLTF files, one for each of the objects at the root of the scene and a `scene.json` that describes the scene in a format that ARENA can import.

Once you have a scene to export, navigate to File -> Export -> Export to ARENA. This will present you with a file browser window to select a folder where the scene files are going to be exported.
![image](https://user-images.githubusercontent.com/3504501/138319900-dcb1a377-d987-4777-ae1a-67ed6bd08331.png)
  
In this window, you have some options to control the ARENA export:
1. **Format**: The exported GLTFs format. Can be GLB, single GLTF with all files embedded, or GLTF with seperate (.gltf + .bin + textures) files.
2. **ARENA Username**: The ARENA username is used to set paths to assets. When this field is edited, the filestore path (option below) is also updated.
2. **ARENA Realm**: The ARENA realm to include in the output file (not used at the moment).
3. **Export Selection**: Export selected objects only.
4. **Export Animations**: Exports active actions and NLA tracks as glTF animations.
5. **Export Extras**: Export custom properties as glTF extras.
6. **Draco Compression**: Compress mesh using Draco.
7. **Filestore Path**: ARENA filestore path for assets (derived automatically from the username, but can be edited).

Pressing **Export to Folder** will create a folder with the name provided and output the files according to your scene structure. 
  
<img src="https://user-images.githubusercontent.com/3504501/138321649-4c9b835d-5399-48cf-aec7-616b4334b890.png" width="400">

Now, copy the folder output by the exporter to the [ARENA filestore](http://arenaxr.org/files). **The location of the files is important as the assets will be assumed to be at this location. At the bottom left of the Blender window, you can see a note about where the files should be uploaded to.**
  
![image](https://user-images.githubusercontent.com/3504501/138322032-e3898cfc-7a2d-4be7-b1dd-5536c63f9d97.png)

### Import to ARENA
Finally, go to the [build webpage](https://arenaxr.org/build/) and import the `scene.json` file inside the folder uploaded to the ARENA filestore by pressing the import button:

<img src="https://user-images.githubusercontent.com/3504501/138899495-a3c6c481-21d4-4e38-9e7a-aebc8f580757.png" width="600">
  
Then, provide either the full path to the .json file on the filestore (e.g. `/store/users/<username>/blender-exports/untitled-scene/scene.json`), or simply the scene name (e.g. `untitled-scene`) if you placed the exported folder under the default filestore path (`/store/users/<username>/blender-exports/`): 

<img src="https://user-images.githubusercontent.com/3504501/138899694-e1dfbcf6-dfb6-497d-a587-31210b201b2c.png" width="600">

You can either add the objects in the JSON file to the current scene in the build webpage (the default) or create a new scene.
  
### Export format

The `scene.json` file format is an array of objects as given from a MongoDB dump, similar to  the python [import/export script](/content/tools/import-export):
```
[
   {
      "_id":{
         "$oid":"605d0cb6cab49fe1bf55d9c7"
      },
      "namespace":"public",
      "object_id":"lobby-model",
      "attributes":{
         "object_type":"gltf-model",
         "url":"/store/users/wiselab/room_models/lobby/lobby-v2.glb",
         "position":{
            "x":0,
            "y":-2,
            "z":0
         },
         "rotation":{
            "x":0,
            "y":0,
            "z":0,
            "w":1
         },
         "scale":{
            "x":0.05,
            "y":0.05,
            "z":0.05
         }
      },
      "type":"object",
      "realm":"realm",
      "sceneId":"lobby"
   }
  {...}
]
```  
  
