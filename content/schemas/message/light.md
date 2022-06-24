---
title: 
nav_order: 23
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

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||A uuid or otherwise unique identifier for this object|Yes|
|persist|boolean|```true```|Persist this object in the database (default true = persist on server)|Yes|
|type|string; Must be: ```object```|```'object'```|AFrame 3D Object|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|data|Light data||Light Data|Yes|

### Light Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_type|string; Must be: ```light```|```light```|3D object type.|Yes|
|angle|number|```60```|Maximum extent of spot light from its direction (in degrees). NOTE: Spot light type only.|No|
|castShadow|boolean|```False```|castShadow (point, spot, directional)|No|
|color|string|```#ffffff```|Color|No|
|decay|number|```1.0```|Amount the light dims along the distance of the light. NOTE: Point and Spot light type only.|No|
|distance|number|```0.0```|Distance where intensity becomes 0. If distance is 0, then the point light does not decay with distance. NOTE: Point and Spot light type only.|No|
|groundColor|string|```'#ffffff'```|Light color from below. NOTE: Hemisphere light type only|No|
|intensity|number|```1```|Light strength.|No|
|light|||These attributes (light, intensity, color, ...) can be set directly on the light object (instead of this light attribute inside the light object); dont use in new light objects|No|
|penumbra|number|```0.0```|Percent of the spotlight cone that is attenuated due to penumbra. NOTE: Spot light type only.|No|
|shadowBias|number|```0```|shadowBias (castShadow=true)|No|
|shadowCameraBottom|number|```-5```|shadowCameraBottom (castShadow=true)|No|
|shadowCameraFar|number|```500```|shadowCameraFar (castShadow=true)|No|
|shadowCameraFov|number|```90```|shadowCameraFov (castShadow=true)|No|
|shadowCameraLeft|number|```-5```|shadowCameraBottom (castShadow=true)|No|
|shadowCameraNear|number|```0.5```|shadowCameraNear (castShadow=true)|No|
|shadowCameraRight|number|```5```|shadowCameraRight (castShadow=true)|No|
|shadowCameraTop|number|```5```|shadowCameraTop (castShadow=true)|No|
|shadowCameraVisible|boolean|```False```|shadowCameraVisible (castShadow=true)|No|
|shadowMapHeight|number|```512```|shadowMapHeight (castShadow=true)|No|
|shadowMapWidth|number|```512```|shadowMapWidth (castShadow=true)|No|
|shadowRadius|number|```1```|shadowRadius (castShadow=true)|No|
|target|string|```'None'```|Id of element the spot should point to. set to null to transform spotlight by orientation, pointing to it’s -Z axis. NOTE: Spot light type only.|No|
|type|string; One of: ```['ambient', 'directional', 'hemisphere', 'point', 'spot']```|```directional```|One of ambient, directional, hemisphere, point, spot.|No|
|animation|[animation](animation)||Animate and tween values. |No|
|armarker|[armarker](armarker)||A location marker (such as an AprilTag, a lightAnchor, or an UWB tag), used to anchor scenes, or scene objects, in the real world.|No|
|click-listener|boolean||Object will listen for clicks|No|
|collision-listener|string||Name of the collision-listener, default can be empty string|No|
|dynamic-body|[dynamic-body](dynamic-body)||Physics type attached to the object. |No|
|goto-landmark|[goto-landmark](goto-landmark)||Teleports user to the landmark with the given name; Requires click-listener|No|
|goto-url|[goto-url](goto-url)||Goto given URL; Requires click-listener|No|
|hide-on-enter-ar|boolean; Must be: ```True```|```True```|Hide object when entering AR. Remove component to *not* hide|No|
|hide-on-enter-vr|boolean; Must be: ```True```|```True```|Hide object when entering VR. Remove component to *not* hide|No|
|impulse|[impulse](impulse)||The force applied using physics. Requires click-listener|No|
|landmark|[landmark](landmark)||Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them; You can define the behavior of the teleport: if you will be at a fixed or random distance, looking at the landmark, fixed offset or if it is contrained by a navmesh (when it exists)|No|
|material-extras|[material-extras](material-extras)||Define extra material properties, namely texture encoding, whether to render the material's color and render order. The properties set here access directly Three.js material component. |No|
|parent|string||Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.|No|
|position|[position](position)|```{'x': 0, 'y': 0, 'z': 0}```|3D object position|No|
|rotation|[rotation](rotation)|```{'x': 0, 'y': 0, 'z': 0}```|3D object rotation in degrees by default; Right-handed coordinate system. Switches to quaternion representation if 'w' is given|No|
|scale|[scale](scale)|```{'x': 1, 'y': 1, 'z': 1}```|3D object scale|No|
|shadow|[shadow](shadow)||shadow|No|
|sound|[sound](sound)||The sound component defines the entity as a source of sound or audio. The sound component is positional and is thus affected by the component's position. |No|
|url|string||Model URL. Store files paths under 'store/users/<username>' (e.g. store/users/wiselab/models/factory_robot_arm/scene.gltf); to use CDN, prefix with `https://arena-cdn.conix.io/` (e.g. https://arena-cdn.conix.io/store/users/wiselab/models/factory_robot_arm/scene.gltf)|No|
|screenshareable|boolean|```True```|Whether or not a user can screenshare on an object|No|
|video-control|[video-control](video-control)||Video Control|No|
