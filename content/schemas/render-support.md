---
title: Rendering Support
nav_order: 6
layout: default
parent: ARENA Objects
---

# Rendering Support

The ARENA MQTT and Persistance system of communication and storage support the following entities and components for rendering and interaction. Version support for the [arena-web-core](https://github.com/arenaxr/arena-web-core) repository for **Web** browsers and the [arena-unity](https://github.com/arenaxr/arena-unity) repository for **Unity** builds are detailed here.

- [**Web Changelog**](https://github.com/arenaxr/arena-web-core/blob/master/CHANGELOG.md)
- [**Unity Changelog**](https://github.com/arenaxr/arena-unity/blob/main/CHANGELOG.md)

| ARENA Entity    | Web    | Unity  | Description                                        |
| --------------- | ------ | ------ | -------------------------------------------------- |
| `box`           | 1.0.0  | 0.0.1  | Box geometry                                       |
| `circle`        | 1.0.0  | 0.0.11 | Circle geometry                                    |
| `capsule`       | 1.11.0 | 0.0.12 | Capsule geometry                                   |
| `cone`          | 1.0.0  | 0.0.11 | Cone geometry                                      |
| `cylinder`      | 1.0.0  | 0.0.1  | Cylinder geometry                                  |
| `dodecahedron`  | 1.0.0  | 0.0.12 | Dodecahedron geometry                              |
| `entity`        | 1.0.0  | 0.0.1  | Entities are the base of all objects in the scene. |
| `gltf-model`    | 1.0.0  | 0.0.2  | Load a GLTF model                                  |
| `image`         | 1.0.0  | 0.0.7  | Display an image on a plane                        |
| `icosahedron`   | 1.0.0  | 0.0.11 | Icosahedron geometry                               |
| `light`         | 1.0.0  | 0.0.5  | A light                                            |
| `line`          | 1.0.0  | 0.8.1  | Draw a line                                        |
| `octahedron`    | 1.0.0  | 0.0.11 | Octahedron geometry                                |
| `pcd-model`     | 1.0.0  | -      | Load a PCD model                                   |
| `plane`         | 1.0.0  | 0.0.1  | Plane geometry                                     |
| `prism`         | 1.0.0  | -      | Prism geometry                                     |
| `program`       | N/A    | N/A    | ARENA program data                                 |
| `ring`          | 1.0.0  | 0.0.11 | Ring geometry                                      |
| `roundedbox`    | 1.14.0 | -      | Rounded Box geometry                               |
| `scene-options` | 1.0.0  | -      | ARENA scene options                                |
| `sphere`        | 1.0.0  | 0.0.1  | Sphere geometry                                    |
| `tetrahedron`   | 1.0.0  | 0.0.12 | Tetrahedron geometry                               |
| `text`          | 1.0.0  | 0.3.0  | Display text                                       |
| `thickline`     | 1.0.0  | 0.4.0  | Draw a line that can have a custom width           |
| `threejs-scene` | 1.0.0  | -      | Load a `three.js` Scene                            |
| `torus`         | 1.0.0  | 0.0.11 | Torus geometry                                     |
| `torusKnot`     | 1.0.0  | -      | Torus Knot geometry                                |
| `triangle`      | 1.0.0  | 0.0.12 | Triangle geometry                                  |
| `videosphere`   | 1.10.0 | N/A    | Videosphere 360 video                              |

| ARENA Component       | Web   | Unity  | Description                                                                                                         |
| --------------------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------- |
| `animation-mixer`     | 1.0.0 | 0.7.0  | A list of available animations in model file will play by default.                                                  |
| `animation`           | 1.0.0 | -      | Animate and tween values.                                                                                           |
| `arena-camera`        | 1.0.0 | 0.2.0  | Tracking camera movement in real time. Emits camera pose change and VIO change events.                              |
| `arena-user`          | 1.0.0 | 0.3.0  | Another user’s camera in the ARENA. Handles Jitsi and display name updates.                                         |
| `arena-vive`          | 1.0.0 | -      | Tracking Vive controller movement in real time.                                                                     |
| `armarker-system`     | 1.0.0 | -      | ARMarker System. Supports ARMarkers in a scene.                                                                     |
| `armarker`            | 1.0.0 | -      | A location marker used to anchor scenes, or scene objects, in the real world.                                       |
| `attribution-system`  | 1.0.0 | -      | Attribution Component/System. Add attribution message to any entity.                                                |
| `attribution`         | 1.0.0 | -      | Attribution Component. Saves attribution data in any entity.                                                        |
| `buffer`              | 1.0.0 | N/A    | Transform geometry into a BufferGeometry to reduce memory usage at the cost of being harder to manipulate.          |
| `click-listener`      | 1.0.0 | 0.8.0  | Keep track of mouse events and publish corresponding events                                                         |
| `collision-listener`  | 1.0.0 | -      | Listen for collisions, callback on event.                                                                           |
| `dynamic-body`        | 1.0.0 | -      | Physics type attached to the object.                                                                                |
| `gesture-detector`    | 1.0.0 | -      | Detect multi-finger touch gestures. Publish events accordingly.                                                     |
| `gltf-model-lod`      | 1.0.0 | -      | GLTF lod switching between models based on distance.                                                                |
| `gltf-model-progress` | 1.0.0 | 0.0.5  | GLTF model loading progress system. Manage GLTF load messages.                                                      |
| `goto-landmark`       | 1.0.0 | -      | Teleports user to the landmark with the given name; Requires click-listener                                         |
| `goto-url`            | 1.0.0 | -      | Goto given URL; Requires click-listener                                                                             |
| `hide-in-ar-mode`     | 1.0.0 | -      | Hide in AR component. When set to an entity, it will make the entity disappear when entering AR mode.               |
| `hide-on-enter-ar`    | 1.0.0 | -      | Hide object when entering AR. Remove component to _not_ hide                                                        |
| `hide-on-enter-vr`    | 1.8.0 | -      | Hide object when entering VR. Remove component to _not_ hide                                                        |
| `impulse`             | 1.0.0 | -      | The force applied using physics. Requires click-listener                                                            |
| `jitsi-video`         | 1.0.0 | N/A    | Apply a Jitsi video source to the geometry                                                                          |
| `landmark`            | 1.0.0 | -      | Define entities as a landmark; Landmarks appears in the landmark list and you can move (teleport) to them.          |
| `load-scene`          | 1.0.0 | 0.0.1  | Load scene from persistence.                                                                                        |
| `material-extras`     | 1.0.0 | -      | Define extra material properties, namely texture encoding, whether to render the material's color and render order. |
| `material`            | 1.0.0 | 0.0.10 | The material properties of the object’s surface.                                                                    |
| `multisrc`            | 1.0.0 | -      | Define multiple visual sources applied to an object.                                                                |
| `network-latency`     | 1.0.0 | -      | Publish with qos of 2 for network graph to update latency                                                           |
| `parent`              | 1.0.0 | 0.0.7  | Parent's object_id. Child objects inherit attributes of their parent, for example scale and translation.            |
| `position`            | 1.0.0 | 0.0.1  | 3D object position                                                                                                  |
| `press-and-move`      | 1.0.0 | -      | Press and move camera; User camera movement with the mouse                                                          |
| `rotation`            | 1.0.0 | 0.0.1  | 3D object rotation in quaternion representation; Right-handed coordinate system.                                    |
| `scale`               | 1.0.0 | 0.0.1  | 3D object scale                                                                                                     |
| `screenshareable`     | 1.0.0 | N/A    | Screenshare-able Component. Allows an object to be screenshared upon                                                |
| `shadow`              | 1.0.0 | 0.0.10 | Whether the entity cast/receives shadows onto the surrounding scene.                                                |
| `skipCache`           | 1.0.0 | -      | Disable retrieving the shared geometry object from the cache.                                                       |
| `sound`               | 1.0.0 | -      | The sound component defines the entity as a source of sound or audio.                                               |
| `textinput`           | 1.0.0 | -      | Opens an HTML prompt when clicked. Sends text input as an event on MQTT. Requires click-listener.                   |
| `threejs-scene`       | 1.0.0 | -      | Load a THREE.js scene.                                                                                              |
| `ttl`                 | 1.0.0 | 0.4.0  | Time To Live (TTL) component.                                                                                       |
| `url`                 | 1.0.0 | 0.0.2  | Model URL.                                                                                                          |
| `video-control`       | 1.0.0 | -      | Adds a video to an entity and controls its playback.                                                                |
