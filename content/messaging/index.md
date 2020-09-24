---
title: Messaging Format
nav_order: 3
layout: default
has_children: true
---

# Messaging Format Overview
Render 3d content in AFrame from MQTT messages

## General Purpose AFrame using Subtopics
Most of ARENA's MQTT messages take JSON data where x,y,z (location in meters), x,y,z,w (rotation in quaternions), x,y,z (scale factor where 1=100%).
If you leave out any of these, defaults will be used: location(0,0,0), rotation(0,0,0,1), scale(1,1,1), color(white). Another general setting is whether or not to persist an object to the ARENA scene database, determined by `"persist": true`.

## User IDs
ARENA visitors are uniquely identified by their camera name, which is also their user name. As all 3D objects in the ARENA are identified by names, camera IDs have 3 underscore separated components, e.g: `camera_1234_er1k`. The last part is what appears above your head (representation in the 3D view), the middle part is a unique ID. If you want to override the random unique ID, you can specify on the URL parameter e.g. `&fixedCamera=er1k` which will ignore the `&name=` and so `er1k` will appear above your head and the camera ID will be `camera_er1k_er1k`.

## Installation
Step one is to clone [ARENA-core](https://github.com:conix-center/ARENA-core) repo into the default web content folder on a linux machine runing Apache, e.g. in `/var/www/html`.
**AFrame is added as a submodule, use the following command to clone:**

`git clone --recurse-submodules git@github.com:conix-center/ARENA-core.git`

Step two, you'll also probably want to be running the Mosquitto MQTT server. In addition, it should be a version that supports websockets. To get one with this feature, and without a known crash bug, we recommend using version 1.6.3 and building with websockets enabled, e.g. in `config.mk` set `WITH_WEBSOCKETS:=yes`.

### Local Instance Installation with docker
See [arena-services-docker](https://github.com/conix-center/arena-services-docker) repository.
