---
title: Examples Index
nav_order: 1.5
layout: default
---

# ARENA Examples Index

An alphabetical glossary of every example of the ARENA's features. These examples are all configurable by sending or storing the wire-format messages for the ARENA protocol.

## Support

Which **Web/Python/Unity** platform supports each of these features? Take a look at our version support for each type:

- [Rendering Features Support](/content/schemas/render-support)
- [Browser Support](/content/xr/requirements.html#supported-platforms)

## Examples

Thumbnail images can be clicked for a larger view. Multiple links are provided to examples of each feature.

| Example                 |               Thumbnail               | Description                                                             | Example Links                                                                         |
| ----------------------- | :-----------------------------------: | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Box                     |          [![][i-box]][i-box]          | Box Geometry                                                            | [Object][wobj],                                                                       |
| Camera                  |       [![][i-camera]][i-camera]       | Camera is the pose and component data representing a user avatar.       | [Object][wobj],                                                                       |
| Capsule                 |      [![][i-capsule]][i-capsule]      | Capsule Geometry                                                        | [Object][wobj],                                                                       |
| Circle                  |       [![][i-circle]][i-circle]       | Circle Geometry                                                         | [Object][wobj],                                                                       |
| Cone                    |         [![][i-cone]][i-cone]         | Cone Geometry                                                           | [Object][wobj],                                                                       |
| Cube                    |         [![][i-cube]][i-cube]         | Cube (=Box) Geometry **(deprecated)**                                   | [Object][wobj],                                                                       |
| Cylinder                |     [![][i-cylinder]][i-cylinder]     | Cylinder Geometry                                                       | [Object][wobj],                                                                       |
| Dodecahedron            | [![][i-dodecahedron]][i-dodecahedron] | Dodecahedron Geometry                                                   | [Object][wobj],                                                                       |
| Entity (generic object) |       [![][i-entity]][i-entity]       | Entities are containers into which components can be attached.          | [Object][wobj],                                                                       |
| Event                   |        [![][i-event]][i-event]        | Events are ephemeral messages used for events like controller actions.  | [Object][wobj],                                                                       |
| Gaussian Splat          |        [![][i-splat]][i-splat]        | Load 3D Gaussian Splat                                                  | [Object][wobj],                                                                       |
| GLTF Model              |         [![][i-gltf]][i-gltf]         | GLTF Models afford consistent cross-platform rendering of 3D assets.    | [Object][wobj], [JSON][j-gltf], [Python][p-gltf], [Unity][u-gltf], [Tutorial][t-gltf] |
| Hand Left               |         [![][i-hand]][i-hand]         | Hand Left is the metadata pose and controller type of the user avatar.  | [Object][wobj],                                                                       |
| Hand Right              |         [![][i-hand]][i-hand]         | Hand Right is the metadata pose and controller type of the user avatar. | [Object][wobj],                                                                       |
| Icosahedron             |  [![][i-icosahedron]][i-icosahedron]  | Icosahedron Geometry                                                    | [Object][wobj],                                                                       |
| Image                   |        [![][i-image]][i-image]        | Display an image on a plane                                             | [Object][wobj],                                                                       |
| Landmark                |     [![][i-landmark]][i-landmark]     | Landmarks allow you to jump to certain places of interest in a scene.   | [Property][oatt], [JSON][j-landmark], [Tutorial][t-landmark]                          |
| Light                   |        [![][i-light]][i-light]        | A light                                                                 | [Object][wobj],                                                                       |
| Line                    |         [![][i-line]][i-line]         | Draw a line                                                             | [Object][wobj],                                                                       |
| Ocean                   |        [![][i-ocean]][i-ocean]        | Ocean                                                                   | [Object][wobj],                                                                       |
| Octahedron              |   [![][i-octahedron]][i-octahedron]   | Octahedron Geometry                                                     | [Object][wobj],                                                                       |
| PCD Model               |          [![][i-pcd]][i-pcd]          | Load a PCD model                                                        | [Object][wobj],                                                                       |
| Plane                   |        [![][i-plane]][i-plane]        | Plane Geometry                                                          | [Object][wobj],                                                                       |
| Program                 |      [![][i-program]][i-program]      | ARENA program data                                                      | [Object][wobj],                                                                       |
| Ring                    |         [![][i-ring]][i-ring]         | Ring Geometry                                                           | [Object][wobj],                                                                       |
| Rounded Box             |   [![][i-roundedbox]][i-roundedbox]   | Rounded Box Geometry                                                    | [Object][wobj],                                                                       |
| Scene Options           |    [![][i-scene-opt]][i-scene-opt]    | ARENA scene options                                                     | [Object][wobj],                                                                       |
| Sphere                  |       [![][i-sphere]][i-sphere]       | Sphere Geometry                                                         | [Object][wobj],                                                                       |
| Tetrahedron             |  [![][i-tetrahedron]][i-tetrahedron]  | Tetrahedron Geometry                                                    | [Object][wobj],                                                                       |
| Text                    |         [![][i-text]][i-text]         | Display text                                                            | [Object][wobj],                                                                       |
| Thickline               |    [![][i-thickline]][i-thickline]    | Draw a thick line that can have a custom width                          | [Object][wobj],                                                                       |
| Three.js Scene          |      [![][i-threejs]][i-threejs]      | Load a Three.js Scene                                                   | [Object][wobj],                                                                       |
| Torus                   |        [![][i-torus]][i-torus]        | Torus Geometry                                                          | [Object][wobj],                                                                       |
| Torus Knot              |    [![][i-torusKnot]][i-torusKnot]    | Torus Knot Geometry                                                     | [Object][wobj],                                                                       |
| Triangle                |     [![][i-triangle]][i-triangle]     | Triangle Geometry                                                       | [Object][wobj],                                                                       |
| UI Button Panel         |   [![][i-ui-buttons]][i-ui-buttons]   | ARENAUI Button Panel                                                    | [Object][wobj],                                                                       |
| UI Card                 |      [![][i-ui-card]][i-ui-card]      | ARENAUI Card                                                            | [Object][wobj],                                                                       |
| UI Prompt               |    [![][i-ui-prompt]][i-ui-prompt]    | ARENAUI Prompt                                                          | [Object][wobj],                                                                       |
| Videosphere             |  [![][i-videosphere]][i-videosphere]  | Videosphere 360 Video                                                   | [Object][wobj],                                                                       |

## Wire Format Types

### 3D Object

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### 3D Object Property

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Program Option

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Scene Option

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Renderer Setting

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Post Processing Setting

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!-- image links-->

[i-box]: /favicon.ico
{:width="100px"}
[i-camera]: /favicon.ico
{:width="100px"}
[i-capsule]: /favicon.ico
{:width="100px"}
[i-circle]: /favicon.ico
{:width="100px"}
[i-cone]: /favicon.ico
{:width="100px"}
[i-cube]: /favicon.ico
{:width="100px"}
[i-cylinder]: /favicon.ico
{:width="100px"}
[i-dodecahedron]: /favicon.ico
{:width="100px"}
[i-entity]: /favicon.ico
{:width="100px"}
[i-event]: /favicon.ico
{:width="100px"}
[i-splat]: /favicon.ico
{:width="100px"}
[i-gltf]: /assets/img/overview/build/mammuthus-primigenius-scene.png
{:width="100px"}
[i-hand]: /favicon.ico
{:width="100px"}
[i-hand]: /favicon.ico
{:width="100px"}
[i-icosahedron]: /favicon.ico
{:width="100px"}
[i-image]: /favicon.ico
{:width="100px"}
[i-landmark]: /favicon.ico
{:width="100px"}
[i-light]: /favicon.ico
{:width="100px"}
[i-line]: /favicon.ico
{:width="100px"}
[i-ocean]: /favicon.ico
{:width="100px"}
[i-octahedron]: /favicon.ico
{:width="100px"}
[i-pcd]: /favicon.ico
{:width="100px"}
[i-plane]: /favicon.ico
{:width="100px"}
[i-program]: /favicon.ico
{:width="100px"}
[i-ring]: /favicon.ico
{:width="100px"}
[i-roundedbox]: /favicon.ico
{:width="100px"}
[i-scene-opt]: /favicon.ico
{:width="100px"}
[i-sphere]: /favicon.ico
{:width="100px"}
[i-tetrahedron]: /favicon.ico
{:width="100px"}
[i-text]: /favicon.ico
{:width="100px"}
[i-thickline]: /favicon.ico
{:width="100px"}
[i-threejs]: /favicon.ico
{:width="100px"}
[i-torus]: /favicon.ico
{:width="100px"}
[i-torusKnot]: /favicon.ico
{:width="100px"}
[i-triangle]: /favicon.ico
{:width="100px"}
[i-ui-buttons]: /favicon.ico
{:width="100px"}
[i-ui-card]: /favicon.ico
{:width="100px"}
[i-ui-prompt]: /favicon.ico
{:width="100px"}
[i-videosphere]: /favicon.ico
{:width="100px"}
[i-landmark]: /assets/img/overview/build/landmark-list.png
{:width="60px"}

<!-- json links-->

[j-landmark]: /content/schemas/message/landmark
[j-gltf]: /content/schemas/message/gltf

<!-- python links-->

[p-gltf]: /content/python/objects#gltf

<!-- tutorial links-->

[t-landmark]: /content/overview/build#add-landmarks
[t-gltf]: /content/overview/build#add-new-objects

<!-- unity links-->

[u-gltf]: /content/unity/editor#exporting-unity-objects-as-gltf

<!-- wire type links-->

[wobj]: #3d-object
[oatt]: #3d-object-property
[prog]: #program-option
[sopt]: #scene-option
[rend]: #renderer-setting
[pprc]: #post-processing-setting