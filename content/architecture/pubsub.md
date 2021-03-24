---
title: MQTT
nav_order: 3
layout: default
parent: Architecture
---

# MQTT PubSub Topic Tree

{% include alert type="warning" title="warning" content="Writing in progress..." %}

## Example topics

## Topic Elements

`a`
: Storage area for (a)priltag detection data

`c`
: Storage area for user text (c)hat messages

`g`
: Storage area for (g)eneral use

`o`
: Storage area for public or (o)pen user to user payload topics

`s`
: Storage area for (s)cene graphical objects

`p`
: Storage area for (p)rivate user to user payload topics

`proc`
: Storage area for runtime (proc)ess and module data

`{namespace}`
: namespace for a particular user within the scene

`{object-id}`
: a-frame object name; object topic should receive mostly a-frame content

`{realm}`
: future use; a namespace we expect to be useful for peer mqtt brokers; probably geographic-based

`{process-id}`
: namespace for a particular application within the scene

`{session-id}`
: A server generated id to establish a unique user connection

`{scene-id}`
: name of particular scene, could be captured from the atlas

`{userhandle}`
: appended to control origin of the chat messages: `b64encode('{session-id}_{username}')`

`{username}`
: the ARENA account username for the user

- \*Names in `{}` are dynamic

## Scene Allowed

`{realm}/s/#`

- All scenes: staff/admin have rights to all scene objects.
- **Subscribe**: staff
- **Publish**: staff

`{realm}/s/{username}/#`

- Scene namespaces: scene owners have rights to their scene objects only.
- **Subscribe**: specific user: username
- **Publish**: specific user: username

`{realm}/s/{namespace}/{scene-id}/#`

- Individual scenes: did the user set specific public read or public write?
- **Subscribe**: public_read=True, or namespace user added editor
- **Publish**: public_write=True, or namespace user added editor

`{realm}/s/{namespace}/{scene-id}/camera_{session-id}_{username}/#`
`{realm}/s/{namespace}/{scene-id}/viveRight_{session-id}_{username}/#`
`{realm}/s/{namespace}/{scene-id}/viveLeft_{session-id}_{username}/#`

- User-presence objects: scene owners have rights to their scene objects only.
- **Subscribe**: public_read=True
- **Publish**: specific anon/user, issued id and username from authentication service.

{% include alert type="note" title="Note" content="Since anon usernames are not authenticated, there is a risk of spoofing their user-presence." %}

## Sensor Allowed

`{realm}/g/a/#`

- All apriltag sensors
- **Subscribe**: staff, user, anon
- **Publish**: staff, user, anon

`{realm}/vio/{namespace}/{scene-id}/#`

- VIO or test cameras to student experiments
- **Publish**: staff

## Chat Allowed

A user handle is appended to control origin of the chat messages in the topic and payload to prevent spoofing. Where `userhandle = b64encode({session-id}\_{username})`.

`{realm}/c/{namespace}/p/{session-id}_{username}/#`

- Receive private messages: Read
- **Subscribe**: staff, user, anon

`{realm}/c/{namespace}/o/#`

- Receive open messages to everyone and/or scene: Read
- **Subscribe**: staff, user, anon

`{realm}/c/{namespace}/o/{userhandle}`

- Send open messages (chat keepalive, messages to all/scene: Write
- **Publish**: staff, user, anon

`{realm}/c/{namespace}/p/+/{userhandle}`

- Private messages to user: Write
- **Publish**: staff, user, anon

## Runtime Manager Allowed

`{realm}/proc/#`

- Open topic for controlling runtime processes
- **Subscribe**: staff, user, anon
- **Publish**: staff, user, anon

## Network Metrics Allowed

`$NETWORK`

- Monitor topic for logging or visualizing metrics
- **Subscribe**: staff, user, anon

`$NETWORK/latency`

- Topic for writing network metrics
- **Publish**: staff, user, anon
