---
title: Web Interface
nav_order: 2
layout: default
has_children: true
---

# Web Frontend User Interface

The web client interface for our main ARENA instance is at [https://arenaxr.org/](https://arenaxr.org/):

<img src="/assets/img/interface/main-website.jpg"/>

From this main entry point, there are a few relevant areas:
- **Login**: [/user](https://arenaxr.org/user)
- **Scene List**: [/user/scenes](https://arenaxr.org/user/scenes)
- **Scene Builder**: [/build](https://arenaxr.org/build)
- **User Files**: [/files](https://arenaxr.org/files/)

In addition, we can access ARENA scenes as described below.

## Accessing ARENA Scenes

**Scenes** are accessed from `<namespace>/<scene>`, where `namespace` is the ARENA user name, and `scene` is the name of the scene. If a namespace is not given, it will default to the `public` namespace. For example, the **lobby** scene (the `scenename`) of the **public** namespace in our main ARENA instance: can be access through both [https://arenaxr.org/public/lobby](https://arenaxr.org/public/lobby) or, ommitting the namespace: [https://arenaxr.org/lobby](https://arenaxr.org/public/lobby). See some example public scenes [here](https://arenaxr.org/showcase.html).

{% include alert type="note" content="
We recommend the [ARENA Overview](/content/overview) as a quick introduction to ARENA and some of these areas, including on how to [access scenes](/content/overview/user-guide) and [edit/create them](/content/overview/build).
"%}

## ARENA Users and Security

There are 2 basic methods of accessing the ARENA: **Authenticated** and **Anonymous**. Anonymous users are only allowed to participate in video conferencing as observers of the ARENA. Authenticated users however, also have the opportunity to create and edit ARENA 3D scenes and run programs in the ARENA.
- **Collaborate**: [Join other users](user-presence) in a video conference.
- **Create**: Use your [authenticated account](user-account) to build something amazing!
- **Control**: Review our current [security model](/content/architecture/security).

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/sDR-I1XVN1A?autoplay=1&controls=0&showinfo=0&modestbranding=1&wmode=transparent&disablekb=1&rel=0&enablejsapi=1&widgetid=1&loop=1&mute=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

**Follow the table of contents below to see more about the ARENA Web Frontend**.
