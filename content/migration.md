---
title: Migration
layout: default
nav_order: 85
---

# ARENA Migration Guide

As we update our software there are changes you may need to implement to keep your Python, Unity, and Web interfaces running smoothly.

## Web 1.29.0 → 2.0.0

- **MQTT Topics**: We have refactored the MQTT topic structure which is now incompatible with older **Unity** and **Python** clients. The old authorization endpoints preceded with `arenaxr.org/user/...` are now required to connect to our `arena-web-core` v2 APIs at `arenaxr.org/user/v2/...`. You may see HTTP requests from **Unity** and **Python** fail with the HTTP status code **426: Upgrade Required**. To resolve, upgrade the [Python upgrade](troubleshooting#python-http-error-426-upgrade-required) or [Unity upgrade](troubleshooting#unity-http-error-426-upgrade-required) instructions.
- **Client Events**: You'll need to update your **Unity** and **Python** client applications to parse MQTT events massages from users with the new `clientEvent` fields, that are more logical now. Previously we used `source, position, clickPos`, with new fields named as `target, targetPosition, originPosition`, respectively. Use the table below to migrate, where `msg` is the root payload JSON of the MQTT `clientEvent` message payload:

    | `clientEvent` Property | New Web 2.0.0 | Old Web 1.0.0 |
    | ------------ | --------------- | ------------------------- |
    | User Object     | **`msg.object_id`** | `msg.data.source` |
    | Target Object   | **`msg.data.target`** | `msg.object_id` |
    | Origin Position | **`msg.data.originPosition`** | `msg.data.clickPos` |
    | Target Position | **`msg.data.targetPosition`** | `msg.data.position` |
