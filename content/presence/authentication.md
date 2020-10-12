---
title: Authentication
nav_order: 5
layout: default
parent: Presence
---

# Authentication

{% include alert type="warning" title="Warning" content="Writing in progress...." %}

## User IDs
ARENA visitors are uniquely identified by their camera name, which is also their user name. As all 3D objects in the ARENA are identified by names, camera IDs have 3 underscore separated components, e.g: `camera_1234_er1k`. The last part is what appears above your head (representation in the 3D view), the middle part is a unique ID. If you want to override the random unique ID, you can specify on the URL parameter e.g. `&fixedCamera=er1k` which will ignore the `&name=` and so `er1k` will appear above your head and the camera ID will be `camera_er1k_er1k`.
