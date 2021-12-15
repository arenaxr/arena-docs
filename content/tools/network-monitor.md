---
title: Connectivity Graph
nav_order: 3
layout: default
parent: Tools
---

## ARENA Connectivity Graph

ARENA's PubSub is supported by a [MQTT Mosquitto broker](https://github.com/eclipse/mosquitto), modified to keep track of connected clients and data flows. This is organized into a graph that is available to users and, more importantly, to the runtime supervisor, ARTS (see the following paragraph). Take a minute to view the ARENA network's connections as you move around in the ARENA on our [Network graph](https://arenaxr.org/network). Clients connected <span style="background-color: black; color: orange;">(orange square)</span>, client subnets <span style="background-color: black; color: gray;">(gray box)</span>, MQTT topics <span style="background-color: black; color: DeepSkyBlue;">(blue circle)</span>, and their current relationships and throughput <span style="background-color: black; color: white;">(white arrow)</span> can be visualized.

Controls:

- **Pause/Play**: Stop or resume fetching graphs.
- **Forward/Back**: Step forward one or step back one previously fetched graph.
- **Scroll**: Zoom in and out of detail.
