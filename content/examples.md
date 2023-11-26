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
- [Browser Support](/content/xr/requirements#supported-platforms)

## Examples

Thumbnail images can be clicked for a larger view. Multiple links are provided to examples of each feature.

<!-- Examples Table Editing -->
<!-- Table Design:
     - Use markdown reference links to make editing,  formatting easier.
     - Use Prettier or other formatter to sync column width.
     - Consider turning off word wrap for this file in your IDE,  so you can read it all in one line.
     - The "Links" column can be expanded/reduced with formatting by exchanging " period" with " pipe period".
-->

| Example               |                Thumbnail                | Description                                                            | Type              . Links .                   |
| :-------------------- | :-------------------------------------: | :--------------------------------------------------------------------- | :---------------- | --------------------------- | ---------------------------- | --------------------------- | ------------------------ |
| Animation             |     [![][i-animation]][i-animation]     | Animate and tween values.                                              | [Attribute][obja] . [Schema][s-animation]     . [Message][m-animation]     . [Python][p-animation]     .                        |
| Animation Mixer       | [![][i-animation-mix]][i-animation-mix] | Control playing animations stored in a GLTF model.                     | [Attribute][obja] . [Schema][s-animation-mix] . [Message][m-animation-mix] . [Python][p-animation-mix] .                        |
| AR Hide/Show          |   [![][i-ar-hideshow]][i-ar-hideshow]   | Hide/Show object when entering AR.                                     | [Attribute][obja] .                           .                            .                           .                        |
| AR Marker             |      [![][i-armarker]][i-armarker]      | A location marker used to anchor scenes/objects, in the real world     | [Attribute][obja] . [Schema][s-armarker]      .                            .                           .                        |
| Attribution           |   [![][i-attribution]][i-attribution]   | Attribution Component. Saves attribution data in any entity            | [Attribute][obja] . [Schema][s-attribution]   .                            .                           .                        |
| Blip                  |          [![][i-blip]][i-blip]          | When the object is created or deleted, it will animate in/out          | [Attribute][obja] . [Schema][s-blip]          .                            .                           .                        |
| Box Collision         | [![][i-box-collision]][i-box-collision] | Listen for bounding-box collisions with user camera and hands          | [Attribute][obja] . [Schema][s-box-collision] .                            .                           .                        |
| Buffer Geometry       |        [![][i-buffer]][i-buffer]        | Reduce geometry memory usage while being harder to manipulate          | [Attribute][obja] .                           .                            .                           .                        |
| Click                 |         [![][i-click]][i-click]         | Object will listen for clicks                                          | [Attribute][obja] . [Schema][s-click]         . [Message][m-click]         . [Python][p-clickable]     .                        |
| Collision             |     [![][i-collision]][i-collision]     | Collisions trigger click events                                        | [Attribute][obja] . [Schema][s-collision]     .                            .                           .                        |
| GLTF LOD              |      [![][i-gltf-lod]][i-gltf-lod]      | Switch between default and detailed GLTF models                        | [Attribute][obja] . [Schema][s-gltf-lod]      .                            .                           .                        |
| GLTF Morph            |    [![][i-gltf-morph]][i-gltf-morph]    | Target and control a GLTF model's morphTargets created in Blender      | [Attribute][obja] . [Schema][s-gltf-morph]    .                            . [Python][p-gltf-morph]    .                        |
| Go to Landmark        | [![][i-goto-landmark]][i-goto-landmark] | Teleports user to the landmark with the given name                     | [Attribute][obja] . [Schema][s-goto-landmark] .                            .                           .                        |
| Go to URL             |      [![][i-goto-url]][i-goto-url]      | Goto given URL                                                         | [Attribute][obja] . [Schema][s-goto-url]      . [Message][m-goto-url]      . [Python][p-goto-url]      .                        |
| GTLF Model Update     |   [![][i-modelUpdate]][i-modelUpdate]   | Allows translation of named GLTF model sub-components.                 | [Attribute][obja] . [Schema][s-modelUpdate]   . [Message][m-modelUpdate]   .                           .                        |
| Impulse               |       [![][i-impulse]][i-impulse]       | The force applied using physics.                                       | [Attribute][obja] . [Schema][s-impulse]       . [Message][m-dynamic-body]  . [Python][p-impulse]       .                        |
| Jitsi Video           |   [![][i-jitsi-video]][i-jitsi-video]   | Apply Jitsi video source to the geometry                               | [Attribute][obja] . [Schema][s-jitsi-video]   .                            .                           .                        |
| Landmark              |      [![][i-landmark]][i-landmark]      | Landmarks allow you to jump to certain places of interest in a scene   | [Attribute][obja] . [Schema][s-landmark]      . [Message][m-landmark]      .                           . [Tutorial][t-landmark] |
| Look At               |       [![][i-look-at]][i-look-at]       | Dynamically rotate or face towards another entity or position          | [Attribute][obja] . [Schema][s-look-at]       . [Message][m-look-at]       .                           .                        |
| Material              |      [![][i-material]][i-material]      | The material properties of the object’s surface.                       | [Attribute][obja] . [Schema][s-material]      . [Message][m-color]         . [Python][p-material]      .                        |
| Material Extras       |  [![][i-material-ext]][i-material-ext]  | Define extra material properties: texture encoding, render order       | [Attribute][obja] . [Schema][s-material-ext]  .                            .                           .                        |
| Multi-Src             |      [![][i-multisrc]][i-multisrc]      | Define multiple visual sources applied to an object.                   | [Attribute][obja] . [Schema][s-multisrc]      . [Message][m-multisrc]      .                           .                        |
| Parent                |        [![][i-parent]][i-parent]        | Parent's object_id. Child objects inherit scale and translation        | [Attribute][obja] . [Schema][s-parent]        . [Message][m-parent]        . [Python][p-parent]        .                        |
| Particle System       |  [![][i-particle-sys]][i-particle-sys]  | Particle system component for A-Frame.                                 | [Attribute][obja] . [Schema][s-particle-sys]  .                            .                           .                        |
| Particles (SPE)       | [![][i-spe-particles]][i-spe-particles] | GPU based particle systems in A-Frame.                                 | [Attribute][obja] . [Schema][s-spe-particles] . [Message][m-spe-particles] .                           .                        |
| Physics               |  [![][i-dynamic-body]][i-dynamic-body]  | Physics type attached to the object.                                   | [Attribute][obja] . [Schema][s-dynamic-body]  . [Message][m-dynamic-body]  . [Python][p-physics]       .                        |
| Position              |      [![][i-position]][i-position]      | 3D object position                                                     | [Attribute][obja] . [Schema][s-position]      . [Message][m-position]      . [Python][p-position]      .                        |
| Remote Render         | [![][i-remote-render]][i-remote-render] | Whether or not an object should be remote rendered [Experimental]      | [Attribute][obja] . [Schema][s-remote-render] .                            .                           .                        |
| Rotation              |      [![][i-rotation]][i-rotation]      | 3D object rotation in quaternions; Right-handed coordinates            | [Attribute][obja] . [Schema][s-rotation]      . [Message][m-rotation]      . [Python][p-rotation]      .                        |
| Scale                 |         [![][i-scale]][i-scale]         | 3D object scale                                                        | [Attribute][obja] . [Schema][s-scale]         . [Message][m-scale]         . [Python][p-scale]         .                        |
| Screenshareable       |   [![][i-screenshare]][i-screenshare]   | Whether or not a user can screen share on an object                    | [Attribute][obja] . [Schema][s-screenshare]   .                            .                           .                        |
| Shadow                |        [![][i-shadow]][i-shadow]        | shadow                                                                 | [Attribute][obja] . [Schema][s-shadow]        .                            .                           .                        |
| Skip Cache            |     [![][i-skipCache]][i-skipCache]     | Disable retrieving the shared geometry object from the cache           | [Attribute][obja] . [Schema][s-skipCache]     .                            .                           .                        |
| Sound                 |         [![][i-sound]][i-sound]         | Positional sound is thus affected by the component's position          | [Attribute][obja] . [Schema][s-sound]         . [Message][m-sound]         . [Python][p-sound]         .                        |
| Text Input            |     [![][i-textinput]][i-textinput]     | Opens an HTML prompt when clicked. Sends text xas an event on MQTT     | [Attribute][obja] . [Schema][s-textinput]     .                            . [Python][p-textinput]     .                        |
| Video Control         | [![][i-video-control]][i-video-control] | Video Control                                                          | [Attribute][obja] . [Schema][s-video-control] .                            . [Python][p-video-control] .                        |
| VR Hide/Show          |   [![][i-vr-hideshow]][i-vr-hideshow]   | Hide/Show object when entering VR.                                     | [Attribute][obja] .                           .                            .                           .                        |
| Action (Message)      |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Data Block            |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Null                  |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Object ID             |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Overwrite             |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Persist               |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| TTL                   |                                         |                                                                        | [Graph][grph]     .                           .                            .                           .                        |
| Box                   |           [![][i-box]][i-box]           | Box Geometry (Unity Cube)                                              | [Object][obj3]    . [Schema][s-box]           . [Message][m-box]           . [Python][p-box]           . [Tutorial][t-box]      |
| Camera                |        [![][i-camera]][i-camera]        | Camera is the pose and component data representing a user avatar       | [Object][obj3]    . [Schema][s-camera]        . [Message][m-camera]        . [Python][p-camera]        .                        |
| Capsule               |       [![][i-capsule]][i-capsule]       | Capsule Geometry                                                       | [Object][obj3]    . [Schema][s-capsule]       .                            .                           .                        |
| Circle                |        [![][i-circle]][i-circle]        | Circle Geometry                                                        | [Object][obj3]    . [Schema][s-circle]        .                            . [Python][p-circle]        .                        |
| Cone                  |          [![][i-cone]][i-cone]          | Cone Geometry                                                          | [Object][obj3]    . [Schema][s-cone]          .                            . [Python][p-cone]          .                        |
| Cube                  |          [![][i-cube]][i-cube]          | Cube Geometry (**deprecated**, see Box)                                | [Object][obj3]    . [Schema][s-cube]          .                            .                           .                        |
| Cylinder              |      [![][i-cylinder]][i-cylinder]      | Cylinder Geometry                                                      | [Object][obj3]    . [Schema][s-cylinder]      .                            . [Python][p-cylinder]      .                        |
| Dodecahedron          |  [![][i-dodecahedron]][i-dodecahedron]  | Dodecahedron Geometry                                                  | [Object][obj3]    . [Schema][s-dodecahedron]  .                            . [Python][p-dodecahedron]  .                        |
| Entity                |        [![][i-entity]][i-entity]        | Entities are containers into which components can be attached          | [Object][obj3]    . [Schema][s-entity]        .                            . [Python][p-entity]        .                        |
| Event                 |         [![][i-event]][i-event]         | Events are ephemeral messages used for events like controller actions  | [Object][obj3]    . [Schema][s-event]         . [Message][m-event]         . [Python][p-event]         .                        |
| Gaussian Splat        |         [![][i-splat]][i-splat]         | Load 3D Gaussian Splat                                                 | [Object][obj3]    . [Schema][s-splat]         .                            .                           .                        |
| GLTF Model            |          [![][i-gltf]][i-gltf]          | GLTF Models afford consistent cross-platform rendering of 3D assets    | [Object][obj3]    . [Schema][s-gltf]          . [Message][m-gltf]          . [Python][p-gltf]          . [Tutorial][t-gltf]     |
| Hand Left             |          [![][i-hand]][i-hand]          | Hand Left is the metadata pose and controller type of the user avatar  | [Object][obj3]    . [Schema][s-hand]          .                            . [Python][p-hands]         .                        |
| Hand Right            |          [![][i-hand]][i-hand]          | Hand Right is the metadata pose and controller type of the user avatar | [Object][obj3]    . [Schema][s-hand]          .                            . [Python][p-hands]         .                        |
| Icosahedron           |   [![][i-icosahedron]][i-icosahedron]   | Icosahedron Geometry                                                   | [Object][obj3]    . [Schema][s-icosahedron]   .                            . [Python][p-icosahedron]   .                        |
| Image                 |         [![][i-image]][i-image]         | Display an image on a plane                                            | [Object][obj3]    . [Schema][s-image]         . [Message][m-image]         . [Python][p-image]         .                        |
| Light                 |         [![][i-light]][i-light]         | A light                                                                | [Object][obj3]    . [Schema][s-light]         . [Message][m-light]         . [Python][p-light]         .                        |
| Line                  |          [![][i-line]][i-line]          | Draw a line                                                            | [Object][obj3]    . [Schema][s-line]          . [Message][m-line]          . [Python][p-line]          .                        |
| Ocean                 |         [![][i-ocean]][i-ocean]         | Ocean                                                                  | [Object][obj3]    . [Schema][s-ocean]         .                            .                           .                        |
| Octahedron            |    [![][i-octahedron]][i-octahedron]    | Octahedron Geometry                                                    | [Object][obj3]    . [Schema][s-octahedron]    .                            . [Python][p-octahedron]    .                        |
| PCD Model             |           [![][i-pcd]][i-pcd]           | Load a Point-Cloud data (PCD) model                                    | [Object][obj3]    . [Schema][s-pcd]           .                            .                           .                        |
| Plane                 |         [![][i-plane]][i-plane]         | Plane Geometry (Unity Quad/Plane)                                      | [Object][obj3]    . [Schema][s-plane]         .                            . [Python][p-plane]         .                        |
| Ring                  |          [![][i-ring]][i-ring]          | Ring Geometry                                                          | [Object][obj3]    . [Schema][s-ring]          .                            . [Python][p-ring]          .                        |
| Rounded Box           |    [![][i-roundedbox]][i-roundedbox]    | Rounded Box Geometry                                                   | [Object][obj3]    . [Schema][s-roundedbox]    .                            .                           .                        |
| Sphere                |        [![][i-sphere]][i-sphere]        | Sphere Geometry                                                        | [Object][obj3]    . [Schema][s-sphere]        .                            . [Python][p-sphere]        .                        |
| Tetrahedron           |   [![][i-tetrahedron]][i-tetrahedron]   | Tetrahedron Geometry                                                   | [Object][obj3]    . [Schema][s-tetrahedron]   .                            . [Python][p-tetrahedron]   .                        |
| Text                  |          [![][i-text]][i-text]          | Display text                                                           | [Object][obj3]    . [Schema][s-text]          . [Message][m-text]          . [Python][p-text]          .                        |
| Thickline             |     [![][i-thickline]][i-thickline]     | Draw a thick line that can have a custom width                         | [Object][obj3]    . [Schema][s-thickline]     . [Message][m-thickline]     . [Python][p-thickline]     .                        |
| Three.js Scene        |       [![][i-threejs]][i-threejs]       | Load a Three.js Scene                                                  | [Object][obj3]    . [Schema][s-threejs]       .                            .                           .                        |
| Torus                 |         [![][i-torus]][i-torus]         | Torus Geometry                                                         | [Object][obj3]    . [Schema][s-torus]         .                            . [Python][p-torus]         .                        |
| Torus Knot            |     [![][i-torusKnot]][i-torusKnot]     | Torus Knot Geometry                                                    | [Object][obj3]    . [Schema][s-torusKnot]     . [Message][m-torusKnot]     . [Python][p-torusKnot]     .                        |
| Triangle              |      [![][i-triangle]][i-triangle]      | Triangle Geometry                                                      | [Object][obj3]    . [Schema][s-triangle]      .                            . [Python][p-triangle]      .                        |
| UI Button Panel       |    [![][i-ui-buttons]][i-ui-buttons]    | ARENAUI Button Panel                                                   | [Object][obj3]    . [Schema][s-ui-buttons]    .                            . [Python][p-ui-buttons]    .                        |
| UI Card               |       [![][i-ui-card]][i-ui-card]       | ARENAUI Card                                                           | [Object][obj3]    . [Schema][s-ui-card]       .                            . [Python][p-ui-card]       .                        |
| UI Prompt             |     [![][i-ui-prompt]][i-ui-prompt]     | ARENAUI Prompt                                                         | [Object][obj3]    . [Schema][s-ui-prompt]     .                            . [Python][p-ui-prompt]     .                        |
| Videosphere           |   [![][i-videosphere]][i-videosphere]   | Video sphere 360 video bubble                                          | [Object][obj3]    . [Schema][s-videosphere]   . [Message][m-videosphere]   .                           .                        |
| Program               |       [![][i-program]][i-program]       | ARENA program data                                                     | [Program][prog]   .                           . [Message][m-program]       .                           . [Tutorial][t-program]  |
| Nav Mesh              |      [![][i-nav-mesh]][i-nav-mesh]      | Invisible 3d model surface for users to move upon.                     | [Scene][sopt]     .                           .                            .                           .                        |
| Start/Spawn Position  |                                         |                                                                        | [Scene][sopt]     .                           .                            .                           .                        |
| Audio                 |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Chat                  |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Controller Navigation |   [![][i-nav-control]][i-nav-control]   |                                                                        | [User][user]      .                           .                            .                           .                        |
| Display Name          |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Flight/Fly            |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Keyboard Navigation   |      [![][i-nav-keys]][i-nav-keys]      |                                                                        | [User][user]      .                           .                            .                           .                        |
| Landmark List         |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Speed                 |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| User List             |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Video                 |                                         |                                                                        | [User][user]      .                           .                            .                           .                        |
| Child                 |                                         | See Parent.                                                            | Concept           .                           .                            .                           .                        |
| Command Line (CLI)    |                                         |                                                                        | Concept           .                           .                            .                           .                        |
| Geometry              |                                         |                                                                        | Concept           .                           .                            .                           .                        |
| Mesh                  |                                         |                                                                        | Concept           .                           .                            .                           .                        |
| Segment               |                                         |                                                                        | Concept           .                           .                            .                           .                        |

## Wire Format Types

### User Option

User preferences to alter default behavior. For reference, a list of [some user settings](/content/overview/user-guide#buttons).

### Graph Property

A property of the entity as it relates to the scene graph.

### Object (3D)

Base 3D entity to which multiple components can be attached. For reference, a list of [all 3D Objects](/content/schemas/message).

### Attribute (3D Object)

A component or effect which can be optionally added to an entity.

### Program

ARENA remote runtime, Python or WebAssembly (WASM). For reference, a list of [all program attributes](/content/schemas/message/arena-program#program-data-attributes)

### Scene Option

ARENA Scene Options. For reference, a list of [all scene options](/content/schemas/message/scene-options#scene-options-attributes)

### Environment Setting

A-Frame Environment presets. More properties at repo [supermedium/aframe-environment-component](https://github.com/supermedium/aframe-environment-component#readme).

### Renderer Setting

These settings are fed into three.js WebGLRenderer properties. For reference, a list of [all renderer settings](/content/schemas/message/renderer-settings#renderer-settings-attributes)

### Post-Processing Effect

These effects are enabled in desktop and XR views. For reference, a list of [all post-processing effects](/content/schemas/message/post-processing#post-processing-effects-attributes)

<!-- image links -->
<!-- Ideally,  create new images and store them in /assets/img/examples/objects/,  /assets/img/examples/attributes/,  etc.|.. -->
<!-- Temporarily,  use "/" for links without images,  if we want a tag,  and not have the unlinked code tag rendered. -->

[i-box]: /assets/img/overview/devguide/box.png
{:width="100px"}
[i-camera]: /assets/img/overview/userguide/a6.png
{:width="100px"}
[i-capsule]: /
{:width="100px"}
[i-circle]: /
{:width="100px"}
[i-cone]: /
{:width="100px"}
[i-cube]: /assets/img/overview/userguide/cube.png
{:width="100px"}
[i-cylinder]: /
{:width="100px"}
[i-dodecahedron]: /
{:width="100px"}
[i-entity]: /
{:width="100px"}
[i-event]: /
{:width="100px"}
[i-splat]: /
{:width="100px"}
[i-gltf]: /assets/img/overview/build/mammuthus-primigenius-scene-landmark.png
{:width="100px"}
[i-hand]: /assets/img/xr/quest-2.png
{:width="100px"}
[i-hand]: /assets/img/xr/quest-2.png
{:width="100px"}
[i-icosahedron]: /
{:width="100px"}
[i-image]: /
{:width="100px"}
[i-landmark]: /
{:width="100px"}
[i-light]: /
{:width="100px"}
[i-line]: /
{:width="100px"}
[i-ocean]: /
{:width="100px"}
[i-octahedron]: /
{:width="100px"}
[i-pcd]: /
{:width="100px"}
[i-plane]: /
{:width="100px"}
[i-program]: /
{:width="100px"}
[i-ring]: /
{:width="100px"}
[i-roundedbox]: /
{:width="100px"}
[i-scene-opt]: /
{:width="100px"}
[i-sphere]: /
{:width="100px"}
[i-tetrahedron]: /
{:width="100px"}
[i-text]: /
{:width="100px"}
[i-thickline]: /
{:width="100px"}
[i-threejs]: /
{:width="100px"}
[i-torus]: /
{:width="100px"}
[i-torusKnot]: /
{:width="100px"}
[i-triangle]: /
{:width="100px"}
[i-ui-buttons]: /assets/img/3dcontent/ui-button-panel.png
{:width="60px"}
[i-ui-card]: /assets/img/3dcontent/ui-card.png
{:width="100px"}
[i-ui-prompt]: /assets/img/3dcontent/ui-prompt.png
{:width="100px"}
[i-videosphere]: /assets/img/overview/videosphere2.png
{:width="100px"}
[i-animation]: /
{:width="100px"}
[i-animation-mix]: /
{:width="100px"}
[i-armarker]: /
{:width="100px"}
[i-attribution]: /assets/img/3dcontent/credits.png
{:width="100px"}
[i-blip]: /assets/img/examples/attributes/blip.gif
{:width="100px"}
[i-box-collision]: /
{:width="100px"}
[i-buffer]: /
{:width="100px"}
[i-click]: /
{:width="100px"}
[i-collision]: /
{:width="100px"}
[i-dynamic-body]: /
{:width="100px"}
[i-gltf-lod]: /
{:width="100px"}
[i-gltf-morph]: /
{:width="100px"}
[i-goto-landmark]: /
{:width="100px"}
[i-goto-url]: /
{:width="100px"}
[i-impulse]: /
{:width="100px"}
[i-jitsi-video]: /
{:width="100px"}
[i-landmark]: /assets/img/overview/build/landmark-list.png
{:width="60px"}
[i-look-at]: /
{:width="100px"}
[i-material]: /
{:width="100px"}
[i-material-ext]: /assets/img/examples/attributes/transparent-occluder.gif
{:width="100px"}
[i-modelUpdate]: /
{:width="100px"}
[i-multisrc]: /
{:width="100px"}
[i-parent]: /
{:width="100px"}
[i-particle-sys]: /
{:width="100px"}
[i-position]: /
{:width="100px"}
[i-remote-render]: /
{:width="100px"}
[i-rotation]: /
{:width="100px"}
[i-scale]: /
{:width="100px"}
[i-screenshare]: /assets/img/examples/attributes/screenshare1.png
{:width="100px"}
[i-shadow]: /
{:width="100px"}
[i-skipCache]: /
{:width="100px"}
[i-sound]: /
{:width="100px"}
[i-spe-particles]: /
{:width="100px"}
[i-textinput]: /
{:width="100px"}
[i-video-control]: /
{:width="100px"}
[i-ar-hideshow]: /
{:width="100px"}
[i-vr-hideshow]: /
{:width="100px"}
[i-nav-mesh]: /assets/img/nav-mesh/nav-demo.gif
{:width="100px"}
[i-nav-keys]: /assets/img/overview/userguide/m1.png
{:width="100px"}
[i-nav-control]: /
{:width="100px"}

<!-- json schema links-->

[s-box]: /content/schemas/message/box
[s-camera]: /content/schemas/message/camera
[s-capsule]: /content/schemas/message/capsule
[s-circle]: /content/schemas/message/circle
[s-cone]: /content/schemas/message/cone
[s-cube]: /content/schemas/message/cube
[s-cylinder]: /content/schemas/message/cylinder
[s-dodecahedron]: /content/schemas/message/dodecahedron
[s-entity]: /content/schemas/message/entity
[s-event]: /content/schemas/message/event
[s-splat]: /content/schemas/message/gaussian-splat
[s-gltf]: /content/schemas/message/gltf-model
[s-hand]: /content/schemas/message/hand
[s-hand]: /content/schemas/message/hand
[s-icosahedron]: /content/schemas/message/icosahedron
[s-image]: /content/schemas/message/image
[s-light]: /content/schemas/message/light
[s-line]: /content/schemas/message/line
[s-ocean]: /content/schemas/message/ocean
[s-octahedron]: /content/schemas/message/octahedron
[s-pcd]: /content/schemas/message/pcd-model
[s-plane]: /content/schemas/message/plane
[s-ring]: /content/schemas/message/ring
[s-roundedbox]: /content/schemas/message/roundedbox
[s-sphere]: /content/schemas/message/sphere
[s-tetrahedron]: /content/schemas/message/tetrahedron
[s-text]: /content/schemas/message/text
[s-thickline]: /content/schemas/message/thickline
[s-threejs]: /content/schemas/message/threejs-scene
[s-torus]: /content/schemas/message/torus
[s-torusKnot]: /content/schemas/message/torusKnot
[s-triangle]: /content/schemas/message/triangle
[s-ui-buttons]: /content/schemas/message/arenaui-button-panel
[s-ui-card]: /content/schemas/message/arenaui-card
[s-ui-prompt]: /content/schemas/message/arenaui-prompt
[s-videosphere]: /content/schemas/message/videosphere
[s-animation]: /content/schemas/message/animation
[s-animation-mix]: /content/schemas/message/animation-mixer
[s-armarker]: /content/schemas/message/armarker
[s-attribution]: /content/schemas/message/attribution
[s-blip]: /content/schemas/message/blip
[s-box-collision]: /content/schemas/message/box-collision-listener
[s-click]: /content/schemas/message/click-listener
[s-collision]: /content/schemas/message/collision-listener
[s-gltf-lod]: /content/schemas/message/gltf-model-lod
[s-gltf-morph]: /content/schemas/message/gltf-morph
[s-goto-landmark]: /content/schemas/message/goto-landmark
[s-goto-url]: /content/schemas/message/goto-url
[s-modelUpdate]: /content/schemas/message/modelUpdate
[s-impulse]: /content/schemas/message/impulse
[s-jitsi-video]: /content/schemas/message/jitsi-video
[s-landmark]: /content/schemas/message/landmark
[s-look-at]: /content/schemas/message/look-at
[s-material]: /content/schemas/message/material
[s-material-ext]: /content/schemas/message/material-extras
[s-multisrc]: /content/schemas/message/multisrc
[s-parent]: /content/schemas/message/parent
[s-particle-sys]: /content/schemas/message/particle-system
[s-spe-particles]: /content/schemas/message/spe-particles
[s-dynamic-body]: /content/schemas/message/dynamic-body
[s-position]: /content/schemas/message/position
[s-remote-render]: /content/schemas/message/remote-render
[s-rotation]: /content/schemas/message/rotation
[s-scale]: /content/schemas/message/scale
[s-screenshare]: /content/schemas/message/screenshareable
[s-shadow]: /content/schemas/message/shadow
[s-skipCache]: /content/schemas/message/skipCache
[s-sound]: /content/schemas/message/sound
[s-textinput]: /content/schemas/message/textinput
[s-video-control]: /content/schemas/message/video-control

<!-- full message example links-->

[m-null]: /content/schemas/message-examples#messaging-format-overview
[m-null]: /content/schemas/message-examples#sample-publishsubscribe
[m-null]: /content/schemas/message-examples#sample-scene-earth-and-moon-with-markers
[m-null]: /content/schemas/message-examples#publish-a-scene-object-message
[m-null]: /content/schemas/message-examples#subscribe-to-scene-object-messages
[m-null]: /content/schemas/message-examples#create-models
[m-null]: /content/schemas/message-examples#create-marker-objects
[m-null]: /content/schemas/message-examples#define-animation-and-movement
[m-null]: /content/schemas/message-examples#add-a-click-listener
[m-null]: /content/schemas/message-examples#messaging-format-reference
[m-null]: /content/schemas/message-examples#formatting-pubsub-messages
[m-videosphere]: /content/schemas/message-examples#360-video
[m-animation]: /content/schemas/message-examples#animate
[m-animation-mix]: /content/schemas/message-examples#animating-gltf-models
[m-environemnt]: /content/schemas/message-examples#background-themes
[m-Look-at]: /content/schemas/message-examples#camera-look-at
[m-color]: /content/schemas/message-examples#color
[m-box]: /content/schemas/message-examples#draw-a-cube
[m-click]: /content/schemas/message-examples#events
[m-event]: /content/schemas/message-examples#events-1
[m-goto-url]: /content/schemas/message-examples#goto-url
[m-image]: /content/schemas/message-examples#images
[m-multisrc]: /content/schemas/message-examples#images-on-objects
[m-landmark]: /content/schemas/message-examples#landmark
[m-light]: /content/schemas/message-examples#lights
[m-line]: /content/schemas/message-examples#lines
[m-gltf]: /content/schemas/message-examples#models
[m-position]: /content/schemas/message-examples#move
[m-rotation]: /content/schemas/message-examples#rotate
[m-scale]: /content/schemas/message-examples#images
[m-user]: /content/schemas/message-examples#move-camera
[m-torusKnot]: /content/schemas/message-examples#other-primitives-torusknot
[m-parent]: /content/schemas/message-examples#parentchild-linking
[m-spe-particles]: /content/schemas/message-examples#particles
[m-persist]: /content/schemas/message-examples#persisted-objects
[m-dynamic-body]: /content/schemas/message-examples#physics
[m-camera]: /content/schemas/message-examples#relocalize-camera-rig
[m-delete]: /content/schemas/message-examples#remove
[m-stats]: /content/schemas/message-examples#scene-settings
[m-sound]: /content/schemas/message-examples#sound
[m-ttl]: /content/schemas/message-examples#temporary-objects-ttl
[m-text]: /content/schemas/message-examples#text
[m-thickline]: /content/schemas/message-examples#thicklines
[m-transparency]: /content/schemas/message-examples#transparency
[m-occlusion]: /content/schemas/message-examples#transparent-occlusion
[m-modelUpdate]: /content/schemas/message/modelUpdate#gltf-model-update-example
[m-object]: /content/schemas/definitions#object-message
[m-event]: /content/schemas/definitions#event-message
[m-program]: /content/schemas/definitions#program-message
[m-scene]: /content/schemas/definitions#scene-options-message

<!-- python links-->

[p-box]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/box.py
[p-circle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/circle.py
[p-cone]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cone.py
[p-cylinder]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cylinder.py
[p-dodecahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/dodecahedron.py
[p-gltf]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/gltf.py
[p-hands]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/hands.py
[p-icosahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/icosahedron.py
[p-image]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/image.py
[p-landmarks]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/landmarks.py
[p-light]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/light.py
[p-line]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/line.py
[p-octahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/octahedron.py
[p-plane]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/plane.py
[p-ring]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ring.py
[p-sphere]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/sphere.py
[p-tetrahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/tetrahedron.py
[p-text]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/text.py
[p-thickline]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/thickline.py
[p-torus]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus.py
[p-torusKnot]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus_knot.py
[p-triangle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/triangle.py
[p-ui-buttons]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-ui-card]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-ui-prompt]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-animation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation.py
[p-animation-mix]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation_mixer.py
[p-color]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/color.py
[p-clickable]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/clickable.py
[p-goto-url]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_url.py
[p-material]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/material.py
[p-gltf-morph]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/morph.py
[p-physics]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[p-impulse]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[p-position]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/position.py
[p-rotation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/rotation.py
[p-scale]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/scale.py
[p-sound]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/sound.py
[p-textinput]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/text_input.py
[p-video-control]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/video_control.py
[p-parent]: https://github.com/arenaxr/arena-py/blob/master/examples/earth-moon.py
[p-camera]: /content/python/objects#camera
[p-event]: /content/python/events#generating-events-with-arena-py-scenes
[p-entity]: /content/python/objects#generic-object

<!-- tutorial links-->

[t-gltf]: /content/overview/build#add-new-objects
[t-landmark]: /content/overview/build#add-landmarks
[t-program]: /content/programs/programs
[t-action]: /content/schemas/definitions#actions
[t-ui-prompt]: /content/3d-content/ui#arenaui-prompt
[t-ui-buttons]: /content/3d-content/ui#arenaui-button-panel
[t-ui-card]: /content/3d-content/ui#arenaui-card---a-text-and-image-panel
[t-spawn]: /content/3d-content/mesh-nav#navmesh-snapping-via-landmark-teleports-or-starting-positions
[t-navmesh]: /content/3d-content/mesh-nav#navigation-meshes
[t-gltf-lod]: /content/3d-content/gltf-files#gltf-model-lod-level-of-detail
[t-attribution]: /content/3d-content/gltf-files#attribution-metadata
[t-animation]: /content/3d-content/animated-models#animated-models
[t-navigation]: /content/xr/requirements#moving-around
[t-armarker]: /content/xr/optical-markers#dynamic-marker
[t-armarker]: /content/xr/optical-markers#attaching-an-armarker-component-to-scene-objects
[t-origin]: /content/xr/optical-markers#fixed-origin-marker
[t-screenshare]: /content/interface/screenshare
[t-filestore]: /content/interface/filestore
[t-inspector]: /content/overview/debug#debug-your-scene-with-a-frame-scene-inspector
[t-webxr-api]: /content/overview/debug#webxr-api-emulator
[t-videosphere]: /content/overview/panoramic
[t-localization]: /content/overview/localization
[t-box]: /content/overview/dev-guide#create-a-box-and-observe
[t-callbacks]: /content/overview/dev-guide#clients-and-scene-callbacks
[t-animation-mix]: /content/overview/dev-guide#animate-a-gltf-model
[t-perist]: /content/overview/dev-guide#use-persistence-reload-browser
[t-scene]: /content/overview/build#add-a-scene
[t-attribute]: /content/overview/build#editing-object-properties
[t-object]: /content/overview/build#add-new-objects
[t-meeting]: /content/overview/clone#sharing-a-link-to-a-meeting-space
[t-scene]: /content/overview/user-guide#opening-a-scene
[t-signin]: /content/overview/user-guide#signing-in
[t-username]: /content/overview/user-guide#arena-username
[t-permission]: /content/overview/user-guide#permissions
[t-navigation]: /content/overview/user-guide#moving-around
[t-user-crtl]: /content/overview/user-guide#buttons
[t-audio]: /content/overview/user-guide#audiovideo-capabilities
[t-video]: /content/overview/user-guide#audiovideo-capabilities
[t-chat]: /content/overview/user-guide#chat-find-people-and-places
[t-userlist]: /content/overview/user-guide#chat-find-people-and-places
[t-landmark]: /content/overview/user-guide#chat-find-people-and-places
[t-settings]: /content/overview/user-guide#additional-settings

<!-- unity links-->

[u-gltf]: /content/unity/editor#exporting-unity-objects-as-gltf

<!-- video links: TODO! -->

<!-- wire type links-->

[user]: #user-option
[grph]: #graph-property
[obj3]: #object-3d
[obja]: #attribute-3d-object
[prog]: #program
[sopt]: #scene-option
[senv]: #environment-setting
[srnd]: #renderer-setting
[spps]: #post-processing-setting
