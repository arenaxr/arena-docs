---
title: Architecture
nav_order: 9
layout: default
has_children: true
---

# Architecture Overview

Figure 1 presents an overview of the ARENA Architecture.

![img](/assets/img/architecture/arch.png)

**Figure 1**. ARENA Architecture. Realms represent a geographically distinct set of resources. Each realm has its own set of ARENA services (web server, message bus, runtime manager).

A directory service, called <b>Atlas</b>, allows users to find nearby content based on coarse location and then supports managing the data needed to link <b>Scene</b> content with the physical world. As users find local content, they  are  handed  off  to  a <b>Realm</b>,  which  is  a  server  (or  group  of servers) that hosts ARENA 3D content and services. Channeling interactions through local/nearby Realms helps to improve latency-sensitive interactions. Realms connect hardware components like <i>viewing devices</i>, such as headsets, mobile phones or tablet and other <i>headless devices</i> embedded in the environment (e.g., cameras and other  sensors  used  for  localization  and  environment  awareness).Realms also include a set of <i>ARENA services</i> (message bus, content server, persistence, runtime manager) to support devices in that geographical area. Most services expose REST APIs to, e.g., query current state, permissions, or create access tokens.User devices connected to the ARENA can not only show 3D content, but also host hot-pluggable applications. We created a common runtime to support sandboxed code launched from any connected target. We leverage modern WebXR-capable browsers to support diverse platforms and rendering capabilities, and several existing frameworks used to create the ARENA browser client: [A-Frame](https://aframe.io/), [three.js](https://threejs.org/) and [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) (also shown inf Figure 1).

Follow the table of contents below to see more about the ARENA Architecture.
