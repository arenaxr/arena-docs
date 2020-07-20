---
title: Persistence DB
nav_order: 5
layout: default
parent: Tools
---

# Persistence DB

# Arena Persistence service

Listens on MQTT for ARENA objects to save to mongodb store

## Install

- Install nodejs
- `npm install`

## Usage

### Persistence
Simply adding `persist: true` to the top level MQTT message for any `create` action and the object will be saved.
A client then can make a HTTP request to the URL the server this service is running on the retrieve a list of 
initially loaded objects upon entering any scene. 

If an `update` message contains an explicit `persist: false`, then the `data` therein will not be saved in persistence.

### TTL
Adding a `ttl` (int seconds) to the top level MQTT message for any `create` action signals that the object
will be automatically deleted from peristence after set duration, as well as a correspdoning `delete` action message
sent over pubsub. `ttl` implies that `persist` is `true`.

### Templates

Templates are special scenes that can be instantiated in entirety in another scenes.

Templates are crafted in a scene name prefixed with the `@` symbol, e.g. `@myTemplate`. The creation process is
exactly same as any other scene with C(R)UD actions on pubsub, with exception that `ttl` values are not
enforced. That is to say, the objects do not expire inside @template scenes, but rather activated upon instantiation.

When a template is loaded, a parent container is first created in the target scene. This parent container follows the
object id naming sceme: ``templateId::instanceId``, e.g. `myTemplate::instance_0`.
 
Then every object inside the designated @template scene is replicated as descendents of the parent container. In this
way, the parent can be repositioned, rotated, or scaled to adjust the template all at once.  The objects within
the template follow the naming scheme ``templateId::instanceId::objectId``, e.g. `myTemplate::instance_0::cube1`.

To load an instance of a template, send message to your desired target scene:

``{"action":"loadTemplate","data":{"templateId":"myTemplate","instanceId":"instance_0"},"object_id":"myClient"}``

The `data` object should also contain `position`, `rotation`, or `scale` directives if intended not to all default
to 0 (or 1 for scale) values. You may also set a `parent` to attach the entire parent container to another existing
object in the target scene. 

After the template load, all objects behave as typical in any scene.

*Notes:*

- If a template scene is empty with no objects, or an instanceid already exists within a target scene, the template
load will fail silently. 

