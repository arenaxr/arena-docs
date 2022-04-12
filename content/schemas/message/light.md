---
title: 
nav_order: 22
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Light
=====


A light. 

More properties at <a href='https://aframe.io/docs/1.3.0/components/light.html'>https://aframe.io/docs/1.3.0/components/light.html</a>

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Light Attributes
-----------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|A uuid or otherwise unique identifier for this object|string||Yes|
|persist|Persist this object in the database (default true = persist on server)|boolean|```true```|Yes|
|type|AFrame 3D Object|string; Must be: ```object```|```'object'```|Yes|
|action|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|Yes|
|data|Light Data|Light data||Yes|

### Light Data Attributes

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|3D object type.|string; Must be: ```light```|```light```|Yes|
|angle|Maximum extent of spot light from its direction (in degrees). NOTE: Spot light type only.|number|```60```|No|
|castShadow|castShadow (point, spot, directional)|boolean|```False```|No|
|color|Color|string|```#ffffff```|No|
|decay|Amount the light dims along the distance of the light. NOTE: Point and Spot light type only.|number|```1.0```|No|
|distance|Distance where intensity becomes 0. If distance is 0, then the point light does not decay with distance. NOTE: Point and Spot light type only.|number|```0.0```|No|
|groundColor|Light color from below. NOTE: Hemisphere light type only|string|```'#ffffff'```|No|
|intensity|Light strength.|number|```1```|No|
|light|These attributes (light, intensity, color, ...) can be set directly on the light object (instead of this light attribute inside the light object); dont use in new light objects|||No|
|penumbra|Percent of the spotlight cone that is attenuated due to penumbra. NOTE: Spot light type only.|number|```0.0```|No|
|shadowBias|shadowBias (castShadow=true)|number|```0```|No|
|shadowCameraBottom|shadowCameraBottom (castShadow=true)|number|```-5```|No|
|shadowCameraFar|shadowCameraFar (castShadow=true)|number|```500```|No|
|shadowCameraFov|shadowCameraFov (castShadow=true)|number|```90```|No|
|shadowCameraLeft|shadowCameraBottom (castShadow=true)|number|```-5```|No|
|shadowCameraNear|shadowCameraNear (castShadow=true)|number|```0.5```|No|
|shadowCameraRight|shadowCameraRight (castShadow=true)|number|```5```|No|
|shadowCameraTop|shadowCameraTop (castShadow=true)|number|```5```|No|
|shadowCameraVisible|shadowCameraVisible (castShadow=true)|boolean|```False```|No|
|shadowMapHeight|shadowMapHeight (castShadow=true)|number|```512```|No|
|shadowMapWidth|shadowMapWidth (castShadow=true)|number|```512```|No|
|shadowRadius|shadowRadius (castShadow=true)|number|```1```|No|
|target|Id of element the spot should point to. set to null to transform spotlight by orientation, pointing to it’s -Z axis. NOTE: Spot light type only.|string|```'None'```|No|
|type|One of ambient, directional, hemisphere, point, spot.|string; One of: ```['ambient', 'directional', 'hemisphere', 'point', 'spot']```|```directional```|No|
|animation|Animate and tween values. |[animation](animation)||No|
|armarker|A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.|[armarker](armarker)||No|
|click-listener|Object will listen for clicks|boolean||No|
|collision-listener|Name of the collision-listener, default can be empty string|string||No|
|dynamic-body|Physics type attached to the object. |[dynamic-body](dynamic-body)||No|
|goto-url|Goto given URL; Requires click-listener|[goto-url](goto-url)||No|
|hide-on-enter-ar|Hide object when entering AR. Remove component to *not* hide|boolean; Must be: ```True```|```True```|No|
|impulse|The force applied using physics. Requires click-listener|[impulse](impulse)||No|
|landmark|Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)|[landmark](landmark)||No|
|material-extras|Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. |[material-extras](material-extras)||No|
|parent|Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|string||No|
|position|3D object position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|No|
|rotation|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|No|
|scale|3D object scale|[scale](scale)|```{'x': 1, 'y': 1, 'z': 1}```|No|
|shadow|shadow|[shadow](shadow)||No|
|sound|The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. |[sound](sound)||No|
|url|Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|string||No|
|screenshareable|Whether or not a user can screenshare on an object|boolean|```True```|No|
|video-control|Video Control|[video-control](video-control)||No|
