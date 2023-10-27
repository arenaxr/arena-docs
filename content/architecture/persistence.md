---
title: Persistence DB
nav_order: 5
layout: tutorial
parent: Architecture
---

# Persistence

When a Scene in ARENA is loaded, its current state is fetched from a data store service that tracks the persisted state of the Scene. In this section, we detail some features of this essential ARENA service.

![img](/assets/img/overview/scene-load.png)
**Figure 3**. Scene objects are first loaded from a data store service and then updated over PubSub.

## Object Persistence
Simply adding `persist: true` to the top level MQTT message for any `create` action and the object will be saved.
A client then can make a HTTP request to the URL the server this service is running on to retrieve a list of
initially loaded objects upon entering any scene.

If an `update` message contains an explicit `persist: false`, then the `data` therein will not be saved in persistence.

## TTL
Adding a `ttl` (int seconds) to the top level MQTT message for any `create` action with `persist:true` signals that the object
will be automatically deleted from persistence after set duration, as well as a corresponding `delete` action message
sent over pubsub.

## Templates

Templates are special scenes that can be instantiated in entirety in other scenes.

Templates are crafted in a scene name prefixed with the `@` symbol, e.g. `@myTemplate`. The creation process is
exactly the same as any other scene with C(R)UD actions on pubsub, with the exception that `ttl` values are not
enforced. That is to say, the objects do not expire inside @template scenes, but rather activated upon instantiation.

When a template is loaded, a parent container is first created in the target scene. This parent container follows the
object ID naming scheme: ``templateId::instanceId``, e.g. `myTemplate::instance_0`.

Then every object inside the designated @template scene is replicated as descendants of the parent container. In this
way, the parent can be repositioned, rotated, or scaled to adjust the template all at once.  The objects within
the template follow the naming scheme ``templateId::instanceId::objectId``, e.g. `myTemplate::instance_0::cube1`.

To load an instance of a template, send message to your desired target scene:

``{"action":"loadTemplate","data":{"templateId":"myTemplate","instanceId":"instance_0"},"object_id":"myClient"}``

The `data` object should also contain `position`, `rotation`, or `scale` directives if intended not to all default
to 0 (or 1 for scale) values. You may also set a `parent` to attach the entire parent container to another existing
object in the target scene.

After the template load, all objects behave as typical in any scene.

{% include alert type="info" title="NOTES" content="
If a template scene is empty with no objects, or an instance ID already exists within a target scene, the template load will fail silently.
" %}

## Implementation and Source

The persistence service listens on the pubsub message bus for ARENA objects to save to a mongodb store.

- [ARENA-persist](https://github.com/arenaxr/arena-persist) repository
