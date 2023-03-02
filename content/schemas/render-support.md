---
title: PubSub Messages
nav_order: 6
layout: default
parent: ARENA Objects
---

# Rendering Support

The ARENA MQTT and Persistance system of communication and storage support the following entities and components for rendering and interaction. Version support for the [arena-web-core](https://github.com/arenaxr/arena-web-core) repository for **Web** browsers and the [arena-unity](https://github.com/arenaxr/arena-unity) repository for **Unity** builds are detailed here.

- [**Web Changelog**](https://github.com/arenaxr/arena-web-core/blob/master/CHANGELOG.md)
- [**Unity Changelog**](https://github.com/arenaxr/arena-unity/blob/main/CHANGELOG.md)

| ARENA Entity    | Web   | Unity  | Description                                        |
| --------------- | ----- | ------ | -------------------------------------------------- |
| `box`           | 1.0.0 | 0.0.1  | Box Geometry                                       |
| `circle`        | 1.0.0 | 0.0.11 | Circle Geometry                                    |
| `capsule`       | 1.0.0 | 0.0.12 | Capsule Geometry                                   |
| `cone`          | 1.0.0 | 0.0.11 | Cone Geometry                                      |
| `cylinder`      | 1.0.0 | 0.0.1  | Cylinder Geometry                                  |
| `dodecahedron`  | 1.0.0 | 0.0.12 | Dodecahedron Geometry                              |
| `entity`        | 1.0.0 | 0.0.1  | Entities are the base of all objects in the scene. |
| `gltf-model`    | 1.0.0 | 0.0.2  | Load a GLTF model                                  |
| `image`         | 1.0.0 | 0.0.7  | Display an image on a plane                        |
| `icosahedron`   | 1.0.0 | 0.0.11 | Icosahedron Geometry                               |
| `light`         | 1.0.0 | 0.0.5  | A light                                            |
| `line`          | 1.0.0 | 0.?.0  | Draw a line                                        |
| `octahedron`    | 1.0.0 | 0.0.11 | Octahedron Geometry                                |
| `pcd-model`     | 1.0.0 | -      | Load a PCD model                                   |
| `plane`         | 1.0.0 | 0.0.1  | Plane Geometry                                     |
| `prism`         | 1.0.0 | -      | Prism Geometry                                     |
| `program`       | N A   | N A    | ARENA program data                                 |
| `ring`          | 1.0.0 | 0.0.11 | Ring Geometry                                      |
| `roundedbox`    | 1.0.0 | -      | Rounded Box Geometry                               |
| `scene-options` | 1.0.0 | -      | ARENA scene options                                |
| `sphere`        | 1.0.0 | 0.0.1  | Sphere Geometry                                    |
| `tetrahedron`   | 1.0.0 | 0.0.12 | Tetrahedron Geometry                               |
| `text`          | 1.0.0 | 0.3.0  | Display text                                       |
| `thickline`     | 1.0.0 | 0.4.0  | Draw a line that can have a custom width           |
| `threejs-scene` | 1.0.0 | -      | Load a Three.js Scene                              |
| `torus`         | 1.0.0 | 0.0.11 | Torus Geometry                                     |
| `torusKnot`     | 1.0.0 | -      | Torus Knot Geometry                                |
| `triangle`      | 1.0.0 | 0.0.12 | Triangle Geometry                                  |
| `videosphere`   | 1.0.0 | N A    | Videosphere 360 Video                              |

| ARENA Component       | Web   | Unity | Description                                                                                                                |
| --------------------- | ----- | ----- | -------------------------------------------------------------------------------------------------------------------------- |
| `animation-mixer`     | 1.0.0 | 0.7.0 |                                                                                                                           |
| `arena-camera`        | 1.0.0 | 0.2.0 | Tracking camera movement in real time. Emits camera pose change and VIO change events.                                     |
| `arena-user`          | 1.0.0 | 0.3.0 | Another user’s camera in the ARENA. Handles Jitsi and display name updates.                                                |
| `arena-vive`          | 1.0.0 | -     | Tracking Vive controller movement in real time.                                                                            |
| `armarker`            | 1.0.0 | -     | ARMarker Component. Supports ARMarkers in a scene                                                                          |
| `armarker-system`     | 1.0.0 | -     | ARMarker System. Supports ARMarkers in a scene.                                                                            |
| `attribution-system`  | 1.0.0 | -     | Attribution Component/System. Add attribution message to any entity.                                                       |
| `attribution`         | 1.0.0 | -     | Attribution Component. Saves attribution data in any entity.                                                               |
| `click-listener`      | 1.0.0 | 0.8.0 | Keep track of mouse events and publish corresponding events                                                                |
| `collision-listener`  | 1.0.0 | -     | Listen for collisions, callback on event.                                                                                  |
| `gesture-detector`    | 1.0.0 | -     | Detect multi-finger touch gestures. Publish events accordingly.                                                            |
| `gltf-model-lod`      | 1.0.0 | -     | GLTF lod switching between models based on distance.                                                                       |
| `gltf-model-progress` | 1.0.0 | 0.0.5 | GLTF model loading progress system. Manage GLTF load messages.                                                             |
| `goto-url`            | 1.0.0 | -     | Load new URL when object is clicked                                                                                        |
| `hide-in-ar-mode`     | 1.0.0 | -     | Hide in AR component. When set to an entity, it will make the entity disappear when entering AR mode.                      |
| `impulse`             | 1.0.0 | -     | One physics feature is applying an impulse to an object to set it in motion.                                               |
| `jitsi-video`         | 1.0.0 | N/A   | Apply a jitsi video to a geometry                                                                                          |
| `landmark`            | 1.0.0 | -     | Component-System of teleport destination Landmarks                                                                         |
| `load-scene`          | 1.0.0 | 0.0.1 | Load scene from persistence.                                                                                               |
| `material-extras`     | 1.0.0 | -     | Allows to set extra material properties, namely texture encoding, whether to render the material’s color and render order. |
| `network-latency`     | 1.0.0 | -     | Publish with qos of 2 for network graph to update latency                                                                  |
| `press-and-move`      | 1.0.0 | -     | Press and move camera; User camera movement with the mouse                                                                 |
| `screenshareable`     | 1.0.0 | N/A   | Screenshare-able Component. Allows an object to be screenshared upon                                                       |
| `textinput`           | 1.0.0 | -     | Opens an HTML prompt when clicked. Sends text input as an event on MQTT                                                    |
| `threejs-scene`       | 1.0.0 | -     | Load a THREE.js scene.                                                                                                     |
| `ttl`                 | 1.0.0 | 0.4.0 | Time To Live (TTL) component.                                                                                              |
| `video-control`       | 1.0.0 | -     | Adds a video to an entity and controls its playback.                                                                       |
