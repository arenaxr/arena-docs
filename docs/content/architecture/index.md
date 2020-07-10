---
title: Architecture
nav_order: 2
layout: default
has_children: true
---

# Architecture Overview

Content viewed by users is composed of 3D scenes (ARENA Scenes) along with the code and other scene information, such as the local message bus server. The scenes are loaded akin to regular web applications within a web browser with the capability to render the content and interact with location services. All objects in the ARENA scene are implicitly networked via a message bus, which allows the scenes, code, and other sensors and services to interact.

![img](../../assets/img/arena-design-overview.png)

**Figure 2**. ARENA Design. Realms represent a geographically distinct set of resources. Each realm has its own set of ARENA services (web server, message bus, runtime manager).

A directory service run by the ATLAS allows users to find the content at their location and supports linking this content with the physical world (by holding information about location beacons, such as light anchors). Execution of code in the scene is managed by a [resource manager (ARTS)](../arts/) and can be dispatched for execution in an available WebAssembly runtime, according to available network and compute resources, quality of service, and security policies. We provide a WebAssembly runtime hosted in any [ARENA browser device](platforms.html) that can support safely running arbitrary code launched from any other connected target. Currently, we are also working on WebAssembly runtime support outside the browser in both Linux-capable devices and even less capable devices with microcontrollers. 
