---
title: Access Control
nav_order: 4
layout: tutorial
parent: Architecture
---

# ARENA PubSub Message Bus
The ARENA message bus is currently supported by a MQTT Mosquitto broker, modified to keep track of connected clients and data flows. This information is organized into a graph that is available to users and, more importantly, to the [runtime supervisor - ARTS](../arts/). The broker is also configured with a [JWT](https://jwt.io/) plugin that implements the PubSub ACL on the topic structure (more details below), and we use Mosquitto’s bridging to create clusters of brokers.

## PubSub Access Control

The root of trust for an ARENA Realm derives from the Access Control List (ACL) permissions managed by the Authentication and Access Control service. Users are authenticated using OAuth and the service emits JSON Web Tokens (JWT) based on permissions for which scenes users control or grant control as an ACL. PubSub brokers and other services (e.g.  the persistence datastore) use JWT to enforce access control. PubSub brokers accept and validate these tokens and use them to allow/disallow publish or subscribe access. We use the PubSub topic structure to sculpt and whitelist which 3D objects, chat, runtime, and other communications bind this ACL to the user’s JWT. To prevent clients from elevating their privileges by publishing malicious messages on the topics they are allowed to publish, we perform client-side checks on message reception and discard invalid messages. See more [security details](../architecture/security.html).

A few example topics are included below for context, as well as a list of topic elements used, and which topics are added to the ARENA JWT based upon user and system defined access control list (ACL) settings.

## Example Topics

General 3D Object
: `realm/s/er1k/test-scene/box_1`

User 3D Object
: `realm/s/er1k/test-scene/camera_1234567890_er1k`

Chat Message
: `realm/c/er1k/p/1234567890_er1k/MTIzNDU2Nzg5MF9lcjFr`

AprilTag Detection
: `realm/g/a/camera_1234567890_er1k`

VIO Update
: `realm/vio/er1k/test-scene/vio-12`

Runtime Stdout
: `realm/proc/debug/stdout/e5f4439e-5a02-4e5d-9d72-704d171d8949`

## Topic Elements

`a`
: Storage area for **AprilTag detection** data

`c`
: Storage area for user text **chat messages**

`g`
: Storage area for **general use**

`o`
: Storage area for public or **open user** payload topics

`s`
: Storage area for **scene graphic objects**

`p`
: Storage area for **private user to user** payload topics

`proc`
: Storage area for runtime **process** and module data

`vio`
: Storage area for **VIO camera** pose updates

`$NETWORK`
: Storage area for **network performance** metrics

`{namespace}`
: Namespace for a particular user within the scene

`{object-id}`
: A-Frame object name; object topic should receive mostly A-Frame content

`{realm}`
: Future use; a namespace we expect to be useful for peer MQTT brokers; probably geographic-based

`{process-id}`
: Namespace for a particular application within the scene

`{session-id}`
: A server-generated ID to establish a unique user connection

`{scene-id}`
: Name of particular scene, could be captured from the ATLAS

`{userhandle}`
: Appended to control origin of the chat messages: `b64encode('{session-id}_{username}')`

`{username}`
: The ARENA account username for the user

\*Names in `{}` are dynamic

## Scene Allowed

### `{realm}/s/#`

- All scenes: Staff/Admin have rights to all scene objects.
- **Subscribe**: Staff
- **Publish**: Staff

### `{realm}/s/{username}/#`

- Scene namespaces: scene owners have rights to their scene objects only.
- **Subscribe**: specific user: `username`
- **Publish**: specific user: `username`

### `{realm}/s/{namespace}/{scene-id}/#`

- Individual scenes: did the user set specific public read or public write?
- **Subscribe**: `public_read`=True, or `namespace` user added `editor`
- **Publish**: `public_write`=True, or `namespace` user added `editor`

### `{realm}/s/{namespace}/{scene-id}/camera_{session-id}_{username}/#`

### `{realm}/s/{namespace}/{scene-id}/handRight_{session-id}_{username}/#`

### `{realm}/s/{namespace}/{scene-id}/handLeft_{session-id}_{username}/#`

- User-presence objects: scene owners have rights to their scene objects only.
- **Subscribe**: `public_read`=True
- **Publish**: specific Anonymous/User, issued ID and username from authentication service.

{% include alert type="note" title="Note" content="Since anonymous usernames are not authenticated, there is a risk of spoofing their user-presence, and as such, all users are issued a `session-id` for their camera objects to prevent this." %}

## Sensor Allowed

### `{realm}/g/a/#`

- All AprilTag sensors
- **Subscribe**: Staff, User, Anonymous
- **Publish**: Staff, User, Anonymous

### `{realm}/vio/{namespace}/{scene-id}/#`

- VIO or test cameras for student experiments
- **Publish**: Staff

## Chat Allowed

A user handle is appended to control the origin of the chat messages in the topic and payload to prevent spoofing. Where `userhandle = b64encode({session-id}\_{username})`.

### `{realm}/c/{namespace}/p/{session-id}_{username}/#`

- Receive private messages: Read
- **Subscribe**: Staff, User, Anonymous

### `{realm}/c/{namespace}/o/#`

- Receive open messages to everyone and/or scene: Read
- **Subscribe**: Staff, User, Anonymous

### `{realm}/c/{namespace}/o/{userhandle}`

- Send open messages (chat keep-alive, messages to all/scene: Write
- **Publish**: Staff, User, Anonymous

### `{realm}/c/{namespace}/p/+/{userhandle}`

- Private messages to User: Write
- **Publish**: Staff, User, Anonymous

## Runtime Manager Allowed

### `{realm}/proc/#`

- Open topic for controlling runtime processes
- **Subscribe**: Staff, User, Anonymous
- **Publish**: Staff, User, Anonymous

## Network Metrics Allowed

### `$NETWORK`

- Monitor topic for logging or visualizing metrics
- **Subscribe**: Staff, User, Anonymous

### `$NETWORK/latency`

- Topic for writing network metrics
- **Publish**: Staff, User, Anonymous
