---
title: Migration
layout: default
nav_order: 85
---

# ARENA Migration Guide

As we update our software there are changes you may need to implement to keep your Python, Unity, and Web interfaces running smoothly.

## Web 2.2.4 → 2.2.5 (Physics Update)

ARENA has migrated its physics engine from Ammo.js to PhysX. The older physics components (`static-body`, `dynamic-body`, and `impulse`) are deprecated and should be updated to their PhysX equivalents. *Note: All new PhysX components require the scene to have physics enabled via `scene-options: physics`.*

### `static-body` and `dynamic-body` → `physx-body`
The older components have been unified into a single **`physx-body`** component.

| Old Property (`static-body` / `dynamic-body`) | New Property (`physx-body`) | Notes / Considerations |
| --- | --- | --- |
| `type` ("static", "dynamic") | `type` ("static", "dynamic", "kinematic") | `dynamic-body` becomes `physx-body` with `type: dynamic` (default). `static-body` becomes `type: static`. |
| `mass` | `mass` | **Default value changed**: Old default was `5`, new default is `1`. |
| `linearDamping` | `linearDamping` | **Default value changed**: Old default `0.01`, new default `0`. |
| `angularDamping` | `angularDamping` | **Default value changed**: Old default `0.01`, new default `0`. |
| `shape` | (Removed) | PhysX automatically calculates collision shapes from the underlying geometry. This override is no longer supported on the body. |
| `cylinderAxis` | (Removed) | No longer supported. |
| `sphereRadius` | (Removed) | No longer supported. |

### `impulse` → `physx-force-pushable`
The old impulse component forced you to calculate the force vectors manually. The new `physx-force-pushable` simplifies this for click interactions.

| Old Property (`impulse`) | New Property (`physx-force-pushable`) | Notes / Considerations |
| --- | --- | --- |
| `on` | `on` | Behavior is identical (e.g. `mousedown`). |
| `force` ({x,y,z}) | `force` (Number) | Simplified to a scalar multiplier. The push direction is automatically calculated from the user's camera ray and click intersection point. |
| `position` ({x,y,z}) | (Removed) | The position of the impulse is now automatically determined by the 3D cursor's intersection point on the object. |

### `collision-listener` (PhysX and Payload Update)
The `collision-listener` component has been successfully migrated to use the new PhysX engine. To ensure it continues to work:
- **Event Dependency**: It now listens for PhysX `contactbegin` instead of Ammo.js `collide`.
- **Requirements**: Ensure the colliding bodies have `emitCollisionEvents: true` set on their `physx-body` component for the events to fire.
- **Payload Changes**: It still publishes `collision` events to MQTT (to differentiate from `box-collision-listener`), but aligns its positional metadata output with the newer payload format. The MQTT payload now correctly registers the user as the `object_id` and the collided object as the `target`.

## Web 1.29.0 → 2.0.0 (MQTT Topics, Client Events)

- **MQTT Topics**: We have refactored the MQTT topic structure which is now incompatible with older **Unity** and **Python** clients. The old authorization endpoints preceded with `arenaxr.org/user/...` are now required to connect to our `arena-web-core` v2 APIs at `arenaxr.org/user/v2/...`. You may see HTTP requests from **Unity** and **Python** fail with the HTTP status code **426: Upgrade Required**. To resolve, use the  [Python upgrade](troubleshooting#python-http-error-426-upgrade-required) or [Unity upgrade](troubleshooting#unity-http-error-426-upgrade-required) instructions.
- **Client Events**: You'll need to update your **Unity** and **Python** client applications to parse MQTT events messages from users with the new `clientEvent` fields, that are more logical now. Previously we used `source, position, clickPos`, with new fields named as `target, targetPosition, originPosition`, respectively. Use the table below to migrate, where `msg` is the root payload JSON of the MQTT `clientEvent` message payload:

    | **`clientEvent`** Property | New Web 2.0.0 | Old Web 1.0.0 |
    | ------------ | --------------- | ------------------------- |
    | User Object     | **`msg.object_id`** | `msg.data.source` |
    | Target Object   | **`msg.data.target`** | `msg.object_id` |
    | Origin Position | **`msg.data.originPosition`** | `msg.data.clickPos` |
    | Target Position | **`msg.data.targetPosition`** | `msg.data.position` |
