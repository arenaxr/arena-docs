---
title: Examples Index
nav_order: 1.5
layout: default
---

# ARENA Examples Index

An alphabetical glossary of every example of the ARENA's features.

## Support

Which **Web/Python/Unity** platform supports each of these features? Take a look at our version support for each type:

- [Rendering Features Support](/content/schemas/render-support)
- [Browser Support](/content/xr/requirements.html#supported-platforms)

## Examples

Thumbnail images can be clicked for a larger view.

| Example                 |               Thumbnail               | Description                                                             | Example Links                                                               |
| ----------------------- | :-----------------------------------: | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ARENAUI Button Panel    |   [![][i-ui-buttons]][i-ui-buttons]   | ARENAUI Button Panel                                                    | Wire,                                                                       |
| ARENAUI Card            |      [![][i-ui-card]][i-ui-card]      | ARENAUI Card                                                            | Wire,                                                                       |
| ARENAUI Prompt          |    [![][i-ui-prompt]][i-ui-prompt]    | ARENAUI Prompt                                                          | Wire,                                                                       |
| Box                     |          [![][i-box]][i-box]          | Box Geometry                                                            | Wire,                                                                       |
| Camera                  |       [![][i-camera]][i-camera]       | Camera is the pose and component data representing a user avatar.       | Wire,                                                                       |
| Capsule                 |      [![][i-capsule]][i-capsule]      | Capsule Geometry                                                        | Wire,                                                                       |
| Circle                  |       [![][i-circle]][i-circle]       | Circle Geometry                                                         | Wire,                                                                       |
| Cone                    |         [![][i-cone]][i-cone]         | Cone Geometry                                                           | Wire,                                                                       |
| Cube                    |         [![][i-cube]][i-cube]         | Cube (=Box) Geometry **(deprecated)**                                   | Wire,                                                                       |
| Cylinder                |     [![][i-cylinder]][i-cylinder]     | Cylinder Geometry                                                       | Wire,                                                                       |
| Dodecahedron            | [![][i-dodecahedron]][i-dodecahedron] | Dodecahedron Geometry                                                   | Wire,                                                                       |
| Entity (generic object) |       [![][i-entity]][i-entity]       | Entities are containers into which components can be attached.          | Wire,                                                                       |
| Event                   |        [![][i-event]][i-event]        | Events are ephemeral messages used for events like controller actions.  | Wire,                                                                       |
| Gaussian Splat          |        [![][i-splat]][i-splat]        | Load 3D Gaussian Splat                                                  | Wire,                                                                       |
| GLTF Model              |         [![][i-gltf]][i-gltf]         | GLTF Models afford consistent cross-platform rendering of 3D assets.    | Wire, [JSON][j-gltf], [Python][p-gltf], [Unity][u-gltf], [Tutorial][t-gltf] |
| Hand Left               |         [![][i-hand]][i-hand]         | Hand Left is the metadata pose and controller type of the user avatar.  | Wire,                                                                       |
| Hand Right              |         [![][i-hand]][i-hand]         | Hand Right is the metadata pose and controller type of the user avatar. | Wire,                                                                       |
| Icosahedron             |  [![][i-icosahedron]][i-icosahedron]  | Icosahedron Geometry                                                    | Wire,                                                                       |
| Image                   |        [![][i-image]][i-image]        | Display an image on a plane                                             | Wire,                                                                       |
| Landmark                |     [![][i-landmark]][i-landmark]     | Landmarks allow you to jump to certain places of interest in a scene.   | Prop, [JSON][j-landmark], [Tutorial][t-landmark]                            |
| Light                   |        [![][i-light]][i-light]        | A light                                                                 | Wire,                                                                       |
| Line                    |         [![][i-line]][i-line]         | Draw a line                                                             | Wire,                                                                       |
| Ocean                   |        [![][i-ocean]][i-ocean]        | Ocean                                                                   | Wire,                                                                       |
| Octahedron              |   [![][i-octahedron]][i-octahedron]   | Octahedron Geometry                                                     | Wire,                                                                       |
| PCD Model               |          [![][i-pcd]][i-pcd]          | Load a PCD model                                                        | Wire,                                                                       |
| Plane                   |        [![][i-plane]][i-plane]        | Plane Geometry                                                          | Wire,                                                                       |
| Program                 |      [![][i-program]][i-program]      | ARENA program data                                                      | Wire,                                                                       |
| Ring                    |         [![][i-ring]][i-ring]         | Ring Geometry                                                           | Wire,                                                                       |
| Rounded Box             |   [![][i-roundedbox]][i-roundedbox]   | Rounded Box Geometry                                                    | Wire,                                                                       |
| Scene Options           |    [![][i-scene-opt]][i-scene-opt]    | ARENA scene options                                                     | Wire,                                                                       |
| Sphere                  |       [![][i-sphere]][i-sphere]       | Sphere Geometry                                                         | Wire,                                                                       |
| Tetrahedron             |  [![][i-tetrahedron]][i-tetrahedron]  | Tetrahedron Geometry                                                    | Wire,                                                                       |
| Text                    |         [![][i-text]][i-text]         | Display text                                                            | Wire,                                                                       |
| Thickline               |    [![][i-thickline]][i-thickline]    | Draw a thick line that can have a custom width                          | Wire,                                                                       |
| Three.js Scene          |      [![][i-threejs]][i-threejs]      | Load a Three.js Scene                                                   | Wire,                                                                       |
| Torus                   |        [![][i-torus]][i-torus]        | Torus Geometry                                                          | Wire,                                                                       |
| Torus Knot              |    [![][i-torusKnot]][i-torusKnot]    | Torus Knot Geometry                                                     | Wire,                                                                       |
| Triangle                |     [![][i-triangle]][i-triangle]     | Triangle Geometry                                                       | Wire,                                                                       |
| Videosphere             |  [![][i-videosphere]][i-videosphere]  | Videosphere 360 Video                                                   | Wire,                                                                       |

<!-- image links-->

[i-landmark]: /assets/img/overview/build/landmark-list.png
{:width="60px"}
[i-gltf]: /assets/img/overview/build/mammuthus-primigenius-scene.png
{:width="100px"}

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
