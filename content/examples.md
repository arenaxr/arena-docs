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

| Example                   |                Thumbnail                | Description                                                                      | Type: Links                |
| :------------------------ | :-------------------------------------: | :------------------------------------------------------------------------------- | :------------------------- | --------------------------- | ---------------------------- | --------------------------- | ----------------------------- |
| Action (Message)          |                                         | The scene graph action: create, update (merge), delete.                          | [Graph:][grph]                                                                                            [Tutorial][t-action]        |
| Animation                 |     [![][i-animation]][i-animation]     | Animate and tween values.                                                        | [Attribute:][obja]         [Schema][s-animation]     [Message][m-animation]     [Python][p-animation]     [Tutorial][t-animation]     |
| Animation Mixer           | [![][i-animation-mix]][i-animation-mix] | Control playing animations stored in a GLTF model.                               | [Attribute:][obja]         [Schema][s-animation-mix] [Message][m-animation-mix] [Python][p-animation-mix] [Tutorial][t-animation-mix] |
| AR Hide/Show              |   [![][i-ar-hideshow]][i-ar-hideshow]   | Hide/Show object when entering AR.                                               | [Attribute:][obja]         [Schema][s-ar-hideshow]                                                                                    |
| AR Marker                 |      [![][i-armarker]][i-armarker]      | A location marker used to anchor scenes/objects, in the real world               | [Attribute:][obja]         [Schema][s-armarker]                                                           [Tutorial][t-armarker]      |
| ARTS                      |          [![][i-arts]][i-arts]          | ARTS, a runtime supervisor for programs                                          | [Application][a-arts]                                                                                                                 |
| ATLAS                     |         [![][i-atlas]][i-atlas]         | ATLAS, a geolocation index of AR scenes.                                         | Application                                                                                               Tutorial forthcoming        |
| Attribution               |   [![][i-attribution]][i-attribution]   | Attribution Component. Saves attribution data in any entity                      | [Attribute:][obja]         [Schema][s-attribution]                                                        [Tutorial][t-attribution]   |
| Audio                     |      [![][i-audio-on]][i-audio-on]      | User's Microphone On/Off state (requires permission)                             | [User:][user]                                                                                             [Tutorial][t-audio]         |
| Blip                      |          [![][i-blip]][i-blip]          | When the object is created or deleted, it will animate in/out                    | [Attribute:][obja]         [Schema][s-blip]                                                                                           |
| Box                       |           [![][i-box]][i-box]           | Box Geometry (Unity Cube)                                                        | [Object:][obj3]            [Schema][s-box]           [Message][m-box]           [Python][p-box]           [Tutorial][t-box]           |
| Box Collision             | [![][i-box-collision]][i-box-collision] | Listen for bounding-box collisions with user camera and hands                    | [Attribute:][obja]         [Schema][s-box-collision]                                                                                  |
| Buffer Geometry           |        [![][i-buffer]][i-buffer]        | Reduce geometry memory usage while being harder to manipulate                    | [Attribute:][obja]         [Schema][s-buffer]                                                                                         |
| Build                     |         [![][i-build]][i-build]         | Build is a JSON editor for the persisted scene graph.                            | [Application][a-build]                                                                                    [Tutorial][t-build]         |
| Build 3D                  |       [![][i-build3d]][i-build3d]       | Build3D is a visual 3D editor for the persisted scene graph (based on Inspector) | Application                                                                                               Tutorial forthcoming        |
| Callbacks                 |                                         | A handler in a program to receive an ARENA Event.                                | Concept                                                                                                   [Tutorial][t-callbacks]     |
| Camera                    |        [![][i-camera]][i-camera]        | Camera is the pose and component data representing a user avatar                 | [Object:][obj3]            [Schema][s-camera]        [Message][m-camera]        [Python][p-camera]                                    |
| Capsule                   |       [![][i-capsule]][i-capsule]       | Capsule Geometry                                                                 | [Object:][obj3]            [Schema][s-capsule]                                                                                        |
| Chat                      |       [![][i-message]][i-message]       | A messaging tool for other users in the ARENA                                    | [User:][user]                                                                                             [Tutorial][t-chat]          |
| Child                     |                                         | See Parent.                                                                      | Concept                                                                                                                               |
| Circle                    |        [![][i-circle]][i-circle]        | Circle Geometry                                                                  | [Object:][obj3]            [Schema][s-circle]                                   [Python][p-circle]                                    |
| Click                     |         [![][i-click]][i-click]         | Object will listen for clicks                                                    | [Attribute:][obja]         [Schema][s-click]         [Message][m-click]         [Python][p-clickable]                                 |
| Collision                 |     [![][i-collision]][i-collision]     | Collisions trigger click events                                                  | [Attribute:][obja]         [Schema][s-collision]                                                                                      |
| Cone                      |          [![][i-cone]][i-cone]          | Cone Geometry                                                                    | [Object:][obj3]            [Schema][s-cone]                                     [Python][p-cone]                                      |
| Conference                |                                         | Using the ARENA scene as a 3D zoom room, video conference, meeting.              | Concept                                                                                                   [Tutorial][t-meeting]       |
| Cube                      |          [![][i-cube]][i-cube]          | Cube Geometry (**deprecated**, see Box)                                          | [Object:][obj3]            [Schema][s-cube]                                                                                           |
| Cylinder                  |      [![][i-cylinder]][i-cylinder]      | Cylinder Geometry                                                                | [Object:][obj3]            [Schema][s-cylinder]                                 [Python][p-cylinder]                                  |
| Data Block                |                                         | The scene graph data Attributes, storing component details.                      | [Graph:][grph]                                                                                                                        |
| Display Name              |   [![][i-displayname]][i-displayname]   | The user-editable display name, derived from the Google account byu default      | [User:][user]                                                                                             [Tutorial][t-displayname]   |
| Dodecahedron              |  [![][i-dodecahedron]][i-dodecahedron]  | Dodecahedron Geometry                                                            | [Object:][obj3]            [Schema][s-dodecahedron]                             [Python][p-dodecahedron]                              |
| Entity                    |        [![][i-entity]][i-entity]        | Entities are containers into which components can be attached                    | [Object:][obj3]            [Schema][s-entity]                                   [Python][p-entity]                                    |
| Event                     |         [![][i-event]][i-event]         | Events are ephemeral messages used for events like controller actions            | [Object:][obj3]            [Schema][s-event]         [Message][m-event]         [Python][p-event]                                     |
| Facial Recognition Avatar |     [![][i-avatar-on]][i-avatar-on]     | Recognizes your facial feature points from your camera and animates a 3d head    | [User:][user]                                                                                             [Tutorial][t-face]          |
| File Store                |     [![][i-filestore]][i-filestore]     | The filestore interface for user file editing and uploading.                     | [Application][a-filestore]                                                                                [Tutorial][t-filestore]     |
| Flight/Fly                |     [![][i-flying-on]][i-flying-on]     | The user state to navigate on a 2D ground plane or 3D flight.                    | [User:][user]                                                                                             [Tutorial][t-usercrtl]      |
| Gaussian Splat            |         [![][i-splat]][i-splat]         | Load 3D Gaussian Splat                                                           | [Object:][obj3]            [Schema][s-splat]                                                                                          |
| Geometry                  |                                         | Geometry (Mesh) is the ordered collection of vertices to make a 3D primitive.    | Concept                                                                                                                               |
| GLTF LOD                  |      [![][i-GLTF-lod]][i-GLTF-lod]      | Switch between default and detailed GLTF models                                  | [Attribute:][obja]         [Schema][s-GLTF-lod]                                                           [Tutorial][t-GLTF-lod]      |
| GLTF Model                |          [![][i-GLTF]][i-GLTF]          | GLTF Models afford consistent cross-platform rendering of 3D assets              | [Object:][obj3]            [Schema][s-GLTF]          [Message][m-GLTF]          [Python][p-GLTF]          [Tutorial][t-GLTF]          |
| GLTF Model Update         |   [![][i-modelUpdate]][i-modelUpdate]   | Allows translation of named GLTF model sub-components.                           | [Attribute:][obja]         [Schema][s-modelUpdate]   [Message][m-modelUpdate]                                                         |
| GLTF Morph                |    [![][i-GLTF-morph]][i-GLTF-morph]    | Target and control a GLTF model morphTargets created in Blender                  | [Attribute:][obja]         [Schema][s-GLTF-morph]                               [Python][p-GLTF-morph]                                |
| Go to Landmark            | [![][i-goto-landmark]][i-goto-landmark] | Teleports user to the landmark with the given name                               | [Attribute:][obja]         [Schema][s-goto-landmark]                                                                                  |
| Go to URL                 |      [![][i-goto-url]][i-goto-url]      | Goto given URL                                                                   | [Attribute:][obja]         [Schema][s-goto-url]      [Message][m-goto-url]      [Python][p-goto-url]                                  |
| Hand Left                 |          [![][i-hand]][i-hand]          | Hand Left is the metadata pose and controller type of the user avatar            | [Object:][obj3]            [Schema][s-hand]                                     [Python][p-hands]                                     |
| Hand Right                |          [![][i-hand]][i-hand]          | Hand Right is the metadata pose and controller type of the user avatar           | [Object:][obj3]            [Schema][s-hand]                                     [Python][p-hands]                                     |
| Icosahedron               |   [![][i-icosahedron]][i-icosahedron]   | Icosahedron Geometry                                                             | [Object:][obj3]            [Schema][s-icosahedron]                              [Python][p-icosahedron]                               |
| Image                     |         [![][i-image]][i-image]         | Display an image on a plane                                                      | [Object:][obj3]            [Schema][s-image]         [Message][m-image]         [Python][p-image]                                     |
| Impulse                   |       [![][i-impulse]][i-impulse]       | The force applied using physics.                                                 | [Attribute:][obja]         [Schema][s-impulse]       [Message][m-dynamic-body]  [Python][p-impulse]                                   |
| Inspector                 |     [![][i-inspector]][i-inspector]     | The A-Frame Inspector, a visual 3D scene graph debugger                          | Application                                                                                               [Tutorial][t-inspector]     |
| Jitsi Video               |   [![][i-jitsi-video]][i-jitsi-video]   | Apply Jitsi video source to the geometry                                         | [Attribute:][obja]         [Schema][s-jitsi-video]                                                                                    |
| Landmark                  |      [![][i-landmark]][i-landmark]      | Landmarks allow you to jump to certain places of interest in a scene             | [Attribute:][obja]         [Schema][s-landmark]      [Message][m-landmark]                                [Tutorial][t-landmark]      |
| Light                     |         [![][i-light]][i-light]         | A light                                                                          | [Object:][obj3]            [Schema][s-light]         [Message][m-light]         [Python][p-light]                                     |
| Line                      |          [![][i-line]][i-line]          | Draw a line                                                                      | [Object:][obj3]            [Schema][s-line]          [Message][m-line]          [Python][p-line]                                      |
| Look At                   |       [![][i-look-at]][i-look-at]       | Dynamically rotate or face towards another entity or position                    | [Attribute:][obja]         [Schema][s-look-at]       [Message][m-look-at]                                                             |
| Material                  |      [![][i-material]][i-material]      | The material properties of the object’s surface.                                 | [Attribute:][obja]         [Schema][s-material]      [Message][m-color]                                                               |
| Material Extras           |  [![][i-material-ext]][i-material-ext]  | Define extra material properties: texture encoding, render order                 | [Attribute:][obja]         [Schema][s-material-ext]                                                                                   |
| Multi-Src                 |      [![][i-multisrc]][i-multisrc]      | Define multiple visual sources applied to an object.                             | [Attribute:][obja]         [Schema][s-multisrc]      [Message][m-multisrc]                                                            |
| Namespace                 |                                         | Your ARENA account namespace (same as User Name)                                 | Concept                                                                                                   [Tutorial][t-username]      |
| Nav Mesh                  |      [![][i-nav-mesh]][i-nav-mesh]      | Invisible 3D model surface for users to move upon.                               | [Scene:][sopt]                                                                                            [Tutorial][t-navmesh]       |
| Navigation Controller     |   [![][i-nav-control]][i-nav-control]   | Using the VR Helmet Controller to hop around a scene.                            | [User:][user]                                                                                             [Tutorial][t-usercrtl]      |
| Navigation Keys           |      [![][i-nav-keys]][i-nav-keys]      | Using the VR Desktop keyboard keys to move around a scene.                       | [User:][user]                                                                                             [Tutorial][t-navigation]    |
| Network Graph             |       [![][i-network]][i-network]       | A web interface of MQTT message traffic                                          | [Application][a-network]                                                                                  [Tutorial][t-network]       |
| Null                      |                                         | Any JSON attribute may be removed by setting it equal to `null`                  | [Graph:][grph]                                                                  [Python][p-null]          [Tutorial][t-null]          |
| Object ID                 |                                         | The scene graph name ID for the entity, must be unique in the scene.             | [Graph:][grph]                                                                                                                        |
| Ocean                     |         [![][i-ocean]][i-ocean]         | Ocean                                                                            | [Object:][obj3]            [Schema][s-ocean]                                                                                          |
| Octahedron                |    [![][i-octahedron]][i-octahedron]    | Octahedron Geometry                                                              | [Object:][obj3]            [Schema][s-octahedron]                               [Python][p-octahedron]                                |
| Origin Marker             |                                         | Origin Tag                                                                       | Concept                                                                                                   [Tutorial][t-origin]        |
| Overwrite                 |                                         | The scene graph directive to erase and overwrite this entity's data, not merge   | [Graph:][grph]                                                                                                                        |
| Parent                    |        [![][i-parent]][i-parent]        | Parent's object_id. Child objects inherit scale and translation                  | [Attribute:][obja]         [Schema][s-parent]        [Message][m-parent]        [Python][p-parent]                                    |
| Particle System           |  [![][i-particle-sys]][i-particle-sys]  | Particle system component for A-Frame.                                           | [Attribute:][obja]         [Schema][s-particle-sys]                                                                                   |
| Particles (SPE)           | [![][i-spe-particles]][i-spe-particles] | GPU based particle systems in A-Frame.                                           | [Attribute:][obja]         [Schema][s-spe-particles] [Message][m-spe-particles]                                                       |
| PCD Model                 |           [![][i-pcd]][i-pcd]           | Load a Point-Cloud data (PCD) model                                              | [Object:][obj3]            [Schema][s-pcd]                                                                                            |
| Persist                   |                                         | The scene graph directive to store the entity in the persistence database.       | [Graph:][grph]                                                                                            [Tutorial][t-persist]       |
| Physics                   |  [![][i-dynamic-body]][i-dynamic-body]  | Physics type attached to the object.                                             | [Attribute:][obja]         [Schema][s-dynamic-body]  [Message][m-dynamic-body]  [Python][p-physics]                                   |
| Plane                     |         [![][i-plane]][i-plane]         | Plane Geometry (Unity Quad/Plane)                                                | [Object:][obj3]            [Schema][s-plane]                                    [Python][p-plane]                                     |
| Position                  |      [![][i-position]][i-position]      | 3D object position                                                               | [Attribute:][obja]         [Schema][s-position]      [Message][m-position]      [Python][p-position]                                  |
| Program                   |       [![][i-program]][i-program]       | ARENA program data                                                               | [Program:][prog]                                     [Message][m-program]                                 [Tutorial][t-program]       |
| Remote Render             | [![][i-remote-render]][i-remote-render] | Whether or not an object should be remote rendered [Experimental]                | [Attribute:][obja]         [Schema][s-remote-render]                                                                                  |
| Ring                      |          [![][i-ring]][i-ring]          | Ring Geometry                                                                    | [Object:][obj3]            [Schema][s-ring]                                     [Python][p-ring]                                      |
| Rotation                  |      [![][i-rotation]][i-rotation]      | 3D object rotation in quaternions; Right-handed coordinates                      | [Attribute:][obja]         [Schema][s-rotation]      [Message][m-rotation]      [Python][p-rotation]                                  |
| Rounded Box               |    [![][i-roundedbox]][i-roundedbox]    | Rounded Box Geometry                                                             | [Object:][obj3]            [Schema][s-roundedbox]                                                                                     |
| Scale                     |         [![][i-scale]][i-scale]         | 3D object scale                                                                  | [Attribute:][obja]         [Schema][s-scale]         [Message][m-scale]         [Python][p-scale]                                     |
| Scene                     |         [![][i-scene]][i-scene]         | The main 3D rendered scene web interface                                         | [Application][a-scene]                                                                                    [Tutorial][t-scene]         |
| Scenes List               |     [![][i-scenelist]][i-scenelist]     | A list of scenes to browse and scene entry URL options.                          | [Application][a-scenelist]                                                                                [Tutorial][t-scenelist]     |
| Screenshareable           |   [![][i-screenshare]][i-screenshare]   | Whether or not a user can screen share on an object                              | [Attribute:][obja]         [Schema][s-screenshare]                                                        [Tutorial][t-screenshare]   |
| Segment                   |                                         | Segments are the rows of triangles used to render a Mesh Geometry Primitive      | Concept                                                                                                                               |
| Shadow                    |        [![][i-shadow]][i-shadow]        | Defines how objects cast and receive shadow                                      | [Attribute:][obja]         [Schema][s-shadow]                                                                                         |
| Sign In                   |                                         | Signin, login                                                                    | [User:][user]                                                                                             [Tutorial][t-signin]        |
| Sign Out                  |                                         | Signout, logout                                                                  | [User:][user]                                                                                             [Tutorial][t-usercrtl]      |
| Skip Cache                |     [![][i-skipCache]][i-skipCache]     | Disable retrieving the shared geometry object from the cache                     | [Attribute:][obja]         [Schema][s-skipCache]                                                                                      |
| Sound                     |         [![][i-sound]][i-sound]         | Positional sound is thus affected by the component's position                    | [Attribute:][obja]         [Schema][s-sound]         [Message][m-sound]         [Python][p-sound]                                     |
| Speed                     |    [![][i-speed-fast]][i-speed-fast]    | The user setting defining how fast to move when using Navigation Keys            | [User:][user]                                                                                             [Tutorial][t-usercrtl]      |
| Sphere                    |        [![][i-sphere]][i-sphere]        | Sphere Geometry                                                                  | [Object:][obj3]            [Schema][s-sphere]                                   [Python][p-sphere]                                    |
| Start/Spawn Position      |                                         | The scene options to control the variance of position to enter the scene         | [Scene:][sopt]                                                                                            [Tutorial][t-spawn]         |
| Tetrahedron               |   [![][i-tetrahedron]][i-tetrahedron]   | Tetrahedron Geometry                                                             | [Object:][obj3]            [Schema][s-tetrahedron]                              [Python][p-tetrahedron]                               |
| Text                      |          [![][i-text]][i-text]          | Display text                                                                     | [Object:][obj3]            [Schema][s-text]          [Message][m-text]          [Python][p-text]                                      |
| Text Input                |     [![][i-textinput]][i-textinput]     | Opens an HTML prompt when clicked. Sends text xas an event on MQTT               | [Attribute:][obja]         [Schema][s-textinput]                                [Python][p-textinput]                                 |
| Thickline                 |     [![][i-thickline]][i-thickline]     | Draw a thick line that can have a custom width                                   | [Object:][obj3]            [Schema][s-thickline]     [Message][m-thickline]     [Python][p-thickline]                                 |
| Three.js Scene            |       [![][i-threejs]][i-threejs]       | Load a Three.js Scene                                                            | [Object:][obj3]            [Schema][s-threejs]                                                                                        |
| Torus                     |         [![][i-torus]][i-torus]         | Torus Geometry                                                                   | [Object:][obj3]            [Schema][s-torus]                                    [Python][p-torus]                                     |
| Torus Knot                |     [![][i-torusKnot]][i-torusKnot]     | Torus Knot Geometry                                                              | [Object:][obj3]            [Schema][s-torusKnot]     [Message][m-torusKnot]     [Python][p-torusKnot]                                 |
| Triangle                  |      [![][i-triangle]][i-triangle]      | Triangle Geometry                                                                | [Object:][obj3]            [Schema][s-triangle]                                 [Python][p-triangle]                                  |
| TTL                       |                                         | The scene graph directive Time-To-Live specifying auto-delete time               | [Graph:][grph]                                       [Message][m-ttl]                                                                 |
| UI Button Panel           |    [![][i-ui-buttons]][i-ui-buttons]    | ARENAUI Button Panel                                                             | [Object:][obj3]            [Schema][s-ui-buttons]                               [Python][p-ui-buttons]    [Tutorial][t-ui-buttons]    |
| UI Card                   |       [![][i-ui-card]][i-ui-card]       | ARENAUI Card                                                                     | [Object:][obj3]            [Schema][s-ui-card]                                  [Python][p-ui-card]       [Tutorial][t-ui-card]       |
| UI Prompt                 |     [![][i-ui-prompt]][i-ui-prompt]     | ARENAUI Prompt                                                                   | [Object:][obj3]            [Schema][s-ui-prompt]                                [Python][p-ui-prompt]     [Tutorial][t-ui-prompt]     |
| User Account              |       [![][i-profile]][i-profile]       | The User's account profile and scene permissions.                                | [Application][a-profile]                                                                                  [Tutorial][t-profile]       |
| User List                 |         [![][i-users]][i-users]         | A scene tool to list connect users and their Jitsi (video conference) state      | [User:][user]                                                                                             [Tutorial][t-userlist]      |
| User Name                 |                                         | Your ARENA account username (same as Namespace)                                  | Concept                                                                                                   [Tutorial][t-username]      |
| Video                     |      [![][i-video-on]][i-video-on]      | User's Camera On/Off state (requires permission)                                 | [User:][user]                                                                                             [Tutorial][t-video]         |
| Video Control             | [![][i-video-control]][i-video-control] | Video Control                                                                    | [Attribute:][obja]         [Schema][s-video-control]                            [Python][p-video-control]                             |
| Videosphere               |   [![][i-videosphere]][i-videosphere]   | Video sphere 360 video bubble                                                    | [Object:][obj3]            [Schema][s-videosphere]   [Message][m-videosphere]                             [Tutorial][t-videosphere]   |
| VR Hide/Show              |   [![][i-vr-hideshow]][i-vr-hideshow]   | Hide/Show object when entering VR.                                               | [Attribute:][obja]         [Schema][s-vr-hideshow]                                                                                    |
| WebXR                     |     [![][i-webxr-api]][i-webxr-api]     | WebXR is an API for building web-accessible XR scenes.                           | Application                                                                                               [Tutorial][t-webxr-api]     |

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
[i-armarker]: /assets/img/xr/enter-ar-3.png
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
[i-nav-control]: /assets/img/xr/quest-2.png
{:width="100px"}
[i-displayname]: /assets/img/overview/userguide/name.png
{:width="100px"}
[i-arts]: /
{:width="100px"}
[i-atlas]: /
{:width="100px"}
[i-build]: /assets/img/overview/build/media/image13.png
{:width="100px"}
[i-build3d]: /
{:width="100px"}
[i-filestore]: /assets/img/overview/filestore/fs2.jpg
{:width="100px"}
[i-inspector]: /assets/img/overview/inspector.png
{:width="100px"}
[i-network]: /
{:width="100px"}
[i-profile]: /
{:width="100px"}
[i-scene]: /
{:width="100px"}
[i-scenelist]: /assets/img/overview/clone/ARENA-scene-clone0.png
{:width="100px"}
[i-webxr-api]: /assets/img/overview/webxr-vr-emulator.png
{:width="100px"}
[i-down-arrow]: /assets/img/icons/down-arrow.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-up-arrow]: /assets/img/icons/up-arrow.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-audio-on]: /assets/img/icons/audio-on.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-audio-off]: /assets/img/icons/audio-off.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-video-on]: /assets/img/icons/video-on.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-video-off]: /assets/img/icons/video-off.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-options]: /assets/img/icons/options.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-avatar-on]: /assets/img/icons/avatar-on.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-avatar-off]: /assets/img/icons/avatar-off.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-flying-on]: /assets/img/icons/flying-on.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-flying-off]: /assets/img/icons/flying-off.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-speed-slow]: /assets/img/icons/speed-slow.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-speed-medium]: /assets/img/icons/speed-medium.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-speed-fast]: /assets/img/icons/speed-fast.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-screen-on]: /assets/img/icons/screen-on.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-logout]: /assets/img/icons/logout.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-message]: /assets/img/icons/message.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-users]: /assets/img/icons/users.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-landmarks]: /assets/img/icons/landmarks.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-health-error]: /assets/img/icons/exclamation-error.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-health-warn]: /assets/img/icons/exclamation-warn.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-sigbad]: /assets/img/icons/signal-bad.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-sigweak]: /assets/img/icons/signal-weak.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-sigpoor]: /assets/img/icons/signal-poor.png
{:height="32px" width="32px" style="background-color:#262626"}
[i-siggood]: /assets/img/icons/signal-good.png
{:height="32px" width="32px" style="background-color:#262626"}

<!-- json schema links-->

[s-animation-mix]: /content/schemas/message/animation-mixer
[s-animation]: /content/schemas/message/animation
[s-ar-hideshow]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-armarker]: /content/schemas/message/armarker
[s-attribution]: /content/schemas/message/attribution
[s-blip]: /content/schemas/message/blip
[s-box-collision]: /content/schemas/message/box-collision-listener
[s-box]: /content/schemas/message/box
[s-buffer]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-camera]: /content/schemas/message/camera
[s-capsule]: /content/schemas/message/capsule
[s-circle]: /content/schemas/message/circle
[s-click]: /content/schemas/message/click-listener
[s-collision]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-cone]: /content/schemas/message/cone
[s-cube]: /content/schemas/message/cube
[s-cylinder]: /content/schemas/message/cylinder
[s-dodecahedron]: /content/schemas/message/dodecahedron
[s-dynamic-body]: /content/schemas/message/dynamic-body
[s-entity]: /content/schemas/message/entity
[s-event]: /content/schemas/message/event
[s-gltf-lod]: /content/schemas/message/gltf-model-lod
[s-gltf-morph]: /content/schemas/message/gltf-morph
[s-gltf]: /content/schemas/message/gltf-model
[s-goto-landmark]: /content/schemas/message/goto-landmark
[s-goto-url]: /content/schemas/message/goto-url
[s-hand]: /content/schemas/message/hand
[s-hand]: /content/schemas/message/hand
[s-icosahedron]: /content/schemas/message/icosahedron
[s-image]: /content/schemas/message/image
[s-impulse]: /content/schemas/message/impulse
[s-jitsi-video]: /content/schemas/message/jitsi-video
[s-landmark]: /content/schemas/message/landmark
[s-light]: /content/schemas/message/light
[s-line]: /content/schemas/message/line
[s-look-at]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-material-ext]: /content/schemas/message/material-extras
[s-material]: /content/schemas/message/material
[s-modelUpdate]: /content/schemas/message/modelUpdate
[s-multisrc]: /content/schemas/message/multisrc
[s-ocean]: /content/schemas/message/ocean
[s-octahedron]: /content/schemas/message/octahedron
[s-parent]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-particle-sys]: /content/schemas/message/particle-system
[s-pcd]: /content/schemas/message/pcd-model
[s-plane]: /content/schemas/message/plane
[s-position]: /content/schemas/message/position
[s-remote-render]: /content/schemas/message/remote-render
[s-ring]: /content/schemas/message/ring
[s-rotation]: /content/schemas/message/rotation
[s-roundedbox]: /content/schemas/message/roundedbox
[s-scale]: /content/schemas/message/scale
[s-screenshare]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-shadow]: /content/schemas/message/shadow
[s-skipCache]: /content/schemas/message/entity#entity-generic-object-data-attributes
[s-sound]: /content/schemas/message/sound
[s-spe-particles]: /content/schemas/message/spe-particles
[s-sphere]: /content/schemas/message/sphere
[s-splat]: /content/schemas/message/gaussian-splat
[s-tetrahedron]: /content/schemas/message/tetrahedron
[s-text]: /content/schemas/message/text
[s-textinput]: /content/schemas/message/textinput
[s-thickline]: /content/schemas/message/thickline
[s-threejs]: /content/schemas/message/threejs-scene
[s-torus]: /content/schemas/message/torus
[s-torusKnot]: /content/schemas/message/torusKnot
[s-triangle]: /content/schemas/message/triangle
[s-ui-buttons]: /content/schemas/message/arenaui-button-panel
[s-ui-card]: /content/schemas/message/arenaui-card
[s-ui-prompt]: /content/schemas/message/arenaui-prompt
[s-video-control]: /content/schemas/message/video-control
[s-videosphere]: /content/schemas/message/videosphere
[s-vr-hideshow]: /content/schemas/message/entity#entity-generic-object-data-attributes

<!-- tutorial? links-->

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

<!-- full message example links-->

[m-animation-mix]: /content/schemas/message-examples#animating-gltf-models
[m-animation]: /content/schemas/message-examples#animate
[m-box]: /content/schemas/message-examples#draw-a-cube
[m-camera]: /content/schemas/message-examples#relocalize-camera-rig
[m-click]: /content/schemas/message-examples#events
[m-color]: /content/schemas/message-examples#color
[m-delete]: /content/schemas/message-examples#remove
[m-dynamic-body]: /content/schemas/message-examples#physics
[m-environemnt]: /content/schemas/message-examples#background-themes
[m-event]: /content/schemas/definitions#event-message
[m-event]: /content/schemas/message-examples#events-1
[m-gltf]: /content/schemas/message-examples#models
[m-goto-url]: /content/schemas/message-examples#goto-url
[m-image]: /content/schemas/message-examples#images
[m-landmark]: /content/schemas/message-examples#landmark
[m-light]: /content/schemas/message-examples#lights
[m-line]: /content/schemas/message-examples#lines
[m-Look-at]: /content/schemas/message-examples#camera-look-at
[m-modelUpdate]: /content/schemas/message/modelUpdate#gltf-model-update-example
[m-multisrc]: /content/schemas/message-examples#images-on-objects
[m-object]: /content/schemas/definitions#object-message
[m-occlusion]: /content/schemas/message-examples#transparent-occlusion
[m-parent]: /content/schemas/message-examples#parentchild-linking
[m-persist]: /content/schemas/message-examples#persisted-objects
[m-position]: /content/schemas/message-examples#move
[m-program]: /content/schemas/definitions#program-message
[m-rotation]: /content/schemas/message-examples#rotate
[m-scale]: /content/schemas/message-examples#images
[m-scene]: /content/schemas/definitions#scene-options-message
[m-sound]: /content/schemas/message-examples#sound
[m-spe-particles]: /content/schemas/message-examples#particles
[m-stats]: /content/schemas/message-examples#scene-settings
[m-text]: /content/schemas/message-examples#text
[m-thickline]: /content/schemas/message-examples#thicklines
[m-torusKnot]: /content/schemas/message-examples#other-primitives-torusknot
[m-transparency]: /content/schemas/message-examples#transparency
[m-ttl]: /content/schemas/message-examples#temporary-objects-ttl
[m-user]: /content/schemas/message-examples#move-camera
[m-videosphere]: /content/schemas/message-examples#360-video

<!-- python links-->

[p-animation-mix]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation_mixer.py
[p-animation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation.py
[p-box]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/box.py
[p-camera]: /content/python/objects#camera
[p-circle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/circle.py
[p-clickable]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/clickable.py
[p-color]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/color.py
[p-cone]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cone.py
[p-cylinder]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/cylinder.py
[p-dodecahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/dodecahedron.py
[p-entity]: /content/python/objects#generic-object
[p-event]: /content/python/events#generating-events-with-arena-py-scenes
[p-gltf-morph]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/morph.py
[p-gltf]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/gltf.py
[p-goto-url]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_url.py
[p-hands]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/hands.py
[p-icosahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/icosahedron.py
[p-image]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/image.py
[p-impulse]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[p-landmarks]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/landmarks.py
[p-light]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/light.py
[p-line]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/line.py
[p-material]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/material.py
[p-octahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/octahedron.py
[p-parent]: https://github.com/arenaxr/arena-py/blob/master/examples/earth-moon.py
[p-physics]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/physics_impulse.py
[p-plane]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/plane.py
[p-position]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/position.py
[p-ring]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ring.py
[p-rotation]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/rotation.py
[p-scale]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/scale.py
[p-sound]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/sound.py
[p-sphere]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/sphere.py
[p-tetrahedron]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/tetrahedron.py
[p-text]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/text.py
[p-textinput]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/text_input.py
[p-thickline]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/thickline.py
[p-torus]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus.py
[p-torusKnot]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/torus_knot.py
[p-triangle]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/triangle.py
[p-ui-buttons]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-ui-card]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-ui-prompt]: https://github.com/arenaxr/arena-py/blob/master/examples/objects/ui.py
[p-video-control]: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/video_control.py
[p-null]: /content/python/objects#removing-object-attributes

<!-- tutorial links-->

[t-action]: /content/schemas/definitions#actions
[t-animation-mix]: /content/overview/dev-guide#animate-a-gltf-model
[t-animation]: /content/3d-content/animated-models#animated-models
[t-armarker]: /content/xr/optical-markers#attaching-an-armarker-component-to-scene-objects
[t-armarker]: /content/xr/optical-markers#dynamic-marker
[t-attribute]: /content/overview/build#editing-object-properties
[t-attribution]: /content/3d-content/gltf-files#attribution-metadata
[t-audio]: /content/interface/user-presence#user-audio
[t-box]: /content/overview/dev-guide#create-a-box-and-observe
[t-build]: /content/overview/build
[t-callbacks]: /content/overview/dev-guide#clients-and-scene-callbacks
[t-chat]: /content/overview/user-guide#chat-find-people-and-places
[t-displayname]: /content/interface/user-presence#user-display-name
[t-face]: /content/interface/user-presence#facial-recognition-avatar
[t-filestore]: /content/interface/filestore
[t-gltf-lod]: /content/3d-content/gltf-files#gltf-model-lod-level-of-detail
[t-gltf]: /content/overview/build#add-new-objects
[t-inspector]: /content/overview/debug#debug-your-scene-with-a-frame-scene-inspector
[t-landmark]: /content/overview/build#add-landmarks
[t-landmark]: /content/overview/user-guide#chat-find-people-and-places
[t-localization]: /content/overview/localization
[t-meeting]: /content/overview/clone#sharing-a-link-to-a-meeting-space
[t-navigation]: /content/overview/user-guide#moving-around
[t-navigation]: /content/xr/requirements#moving-around
[t-navmesh]: /content/3d-content/mesh-nav#navigation-meshes
[t-network]: /content/tools/network-monitor
[t-origin]: /content/xr/optical-markers#fixed-origin-marker
[t-perm-device]: /content/overview/user-guide#permissions
[t-persist]: /content/overview/dev-guide#use-persistence-reload-browser
[t-profile]: /content/overview/build#add-a-scene
[t-program]: /content/programs/programs
[t-scene]: /content/overview/user-guide#opening-a-scene
[t-scenelist]: /content/overview/build#add-a-scene
[t-screenshare]: /content/interface/screenshare
[t-settings]: /content/overview/user-guide#additional-settings
[t-signin]: /content/overview/user-guide#signing-in
[t-spawn]: /content/3d-content/mesh-nav#navmesh-snapping-via-landmark-teleports-or-starting-positions
[t-ui-buttons]: /content/3d-content/ui#arenaui-button-panel
[t-ui-card]: /content/3d-content/ui#arenaui-card---a-text-and-image-panel
[t-ui-prompt]: /content/3d-content/ui#arenaui-prompt
[t-usercrtl]: /content/overview/user-guide#buttons
[t-userlist]: /content/overview/user-guide#chat-find-people-and-places
[t-username]: /content/overview/user-guide#arena-username
[t-video]: /content/interface/user-presence#user-video
[t-videosphere]: /content/overview/panoramic
[t-webxr-api]: /content/overview/debug#webxr-api-emulator
[t-profile]: /content/interface/user-account
[t-null]: /content/schemas/definitions#actions

<!-- application links-->
<!-- [a-atlas]: https://atlas.conix.io -->

[a-arts]: https://arenaxr.org/programs
[a-build]: https://arenaxr.org/build
[a-filestore]: https://arenaxr.org/files
[a-network]: https://arenaxr.org/network
[a-profile]: https://arenaxr.org/user/profile
[a-scene]: https://arenaxr.org/public/lobby
[a-scenelist]: https://arenaxr.org/scenes

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
