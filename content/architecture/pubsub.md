---
title: MQTT
nav_order: 3
layout: default
parent: Architecture
---

# MQTT PubSub Topic Tree

{% include alert type="danger" title="OUT OF DATE" content="These topics have been expanded, and could use an update" %}

## Elements

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

`r`
: denotes the storage area for runtime related information

`n`
: denotes the storage area for network related information

- \*Names in `{}` are dynamic
- [] indicates optional parameters

## Scene Allowed:

- `{realm}/s/#`

  - All scenes: staff/admin have rights to all scene objects.
  - Subscribe: staff
  - Publish: staff

- `{realm}/s/{username}/#`

  - Scene namespaces: scene owners have rights to their scene objects only.
  - Subscribe: specific user: username
  - Publish: specific user: username

- `{realm}/s/{namespace}/{scene}/#`

  - Individual scenes: did the user set specific public read or public write?
  - Subscribe: public_read=True, or namespace user added editor
  - Publish: public_write=True, or namespace user added editor

- `{realm}/s/{namespace}/{scene}/camera_{id}_{username}/#`
- `{realm}/s/{namespace}/{scene}/viveRight_{id}_{username}/#`
- `{realm}/s/{namespace}/{scene}/viveLeft_{id}_{username}/#`

  - User-presence objects: scene owners have rights to their scene objects only.
  - Subscribe: public_read=True
  - Publish: specific anon/user, issued id and username from authentication service.
  - Note: Since anon usernames are not authenticated, there is a risk of spoofing their user-presence.

## Sensor Allowed:

- `{realm}/g/a/#`

  - All apriltag sensors
  - Subscribe: staff, user, anon
  - Publish: staff, user, anon

- `{realm}/vio/{scene}/#`

  - VIO or test cameras to student experiments
  - Publish: staff

## Chat Allowed:

A user handle is appended to control origin of the chat messages in the topic and payload to prevent spoofing. Where `userhandle = b64encode({id}\_{username})`.

- `{realm}/c/{namespace}/p/{id}_{username}/#`

  - Receive private messages: Read
  - Subscribe: staff, user, anon

- `{realm}/c/{namespace}/o/#`

  - Receive open messages to everyone and/or scene: Read
  - Subscribe: staff, user, anon

- `{realm}/c/{namespace}/o/{userhandle}`

  - Send open messages (chat keepalive, messages to all/scene: Write
  - Publish: staff, user, anon

- `{realm}/c/{namespace}/p/+/{userhandle}`

  - Private messages to user: Write
  - Publish: staff, user, anon

## Runtime Manager Allowed:

- `{realm}/proc/#`

  - Open topic for controlling runtime processes
  - Subscribe: staff, user, anon
  - Publish: staff, user, anon

## Network Metrics Allowed:

- `$NETWORK`

  - Monitor topic for logging or visualizing metrics
  - Subscribe: staff, user, anon

- `$NETWORK/latency`

  - Topic for writing network metrics
  - Publish: staff, user, anon
