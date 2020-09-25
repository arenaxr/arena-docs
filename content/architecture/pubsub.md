---
title: MQTT
nav_order: 3
layout: default
parent: Architecture
---

# MQTT PubSub Topic Tree

{% include alert type="danger" title="OUT OF DATE" content="These topics have been expanded, and could use an update" %}

## Graphic elements

- `<realm>/s/<scene-id>/<object>`
- Ex. `pittsburgh/s/ascene/aobject/`

`<realm>`  
: future use; a namespace we expect to be useful for peer mqtt brokers; probably geographic-based

`s`  
: indicates that we have a scene id next

`<scene-id>`  
: name of particular scene, could be captured from the atlas

`<process-id/session-id>`
: namespace for a particular user or application within the scene

`<object>`
: a-frame object name; object topic should receive mostly a-frame content

## Runtime resources

- `<realm>/r/<runtime UUID>`
- `<realm>/n/topology/`…
- `<realm>/n/flows/`…

`r`
: denotes the storage area for runtime related information

`n`
: denotes the storage area for network related information

`topology`
: blob of json that describes the current physical topology managed by this server

`flows`
: blob of json that describes the current network flows

- \*Names in < > are dynamic
- [] indicates optional parameters
