---
title: Migration
layout: default
---

# ARENA Migration Guide

As we update our software there are changes you may need to implement for

## arena-py and arena-unity
- **user/user_state and user/mqtt_auth**: These authorization endpoints are now reuired to connect to our `arena-web-core` v2 APIs. You may see HTTP requests from **Unity** and **Python** clients fail with the HTTP status code **428: Upgrade Required**
- **clientEvent**: You'll need to update your **Unity** and **Python** client applications to parse MQTT events massages from users with the new `clientEvent` fields, that are more logical now. Previously we used `source, position, clickPos`, with new fields named as `target, targetPosition, originPosition`, respectively.
