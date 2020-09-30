---
title: Examples
nav_order: 5
layout: default
parent: Messaging Format
---

# Messaging Format Examples

- [**ARENA-core**](https://github.com/conix-center/ARENA-core) webserver repository

## Camera
(from [A-Frame documentation](https://aframe.io/docs/1.0.0/components/camera.html))

| The camera component defines from which perspective the user views the scene. The camera is commonly paired with controls components that allow input devices to move and rotate the camera.

| A camera should usually be positioned at the average height of human eye level (1.6 meters). When used with controls that receive rotation or position (e.g. from a VR device) this position will be overridden.

```html
  <a-entity camera look-controls position="0 1.6 0"></a-entity>
```

The above example puts the camera at a position in the scene, but sure enough, when we use a tablet + WebXRViewer or a VR or AR headset, these values are overwritten. IN FACT it turns out that from a desktop browser, at the start of our A-Frame session, regardless of the values set in the HTML above, the start position is set to (0, 1.6, 0). It was misleading that the HTML definition just happened to match. Our code sets it to (0,0,0) in the declaration. It gets more interesting: on a tablet or phone, the start position again gets overridden - by (0,0,0) this time!

| When moving or rotating the camera relative to the scene, use a camera rig. By doing so, the camera’s height offset can be updated by room-scale devices, while still allowing the tracked area to be moved independently around the scene.

```html
  <a-entity id="rig" position="25 10 0">
    <a-entity id="camera" camera look-controls></a-entity>
  </a-entity>
```

## Sample scene: Earth and Moon with Markers
MQTT messages that define the scene:

### Create models
```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/gltf-model_Earth -m '{"object_id": "gltf-model_Earth", "action": "create", "data": {"object_type": "gltf-model", "position": {"x":0, "y": 0.1, "z": 0}, "url": "models/Earth.glb", "scale": {"x": 5, "y": 5, "z": 5}}}'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/gltf-model_Moon -m '{"object_id": "gltf-model_Moon", "action": "create", "data": {"parent": "gltf-model_Earth", "object_type": "gltf-model", "position": {"x":0, "y": 0.05, "z": 0.6}, "scale": {"x":0.05, "y": 0.05, "z": 0.05}, "url": "models/Moon.glb" }}'
```
### Define animation and movement
 ```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/gltf-model_Earth -m '{"object_id" : "gltf-model_Earth", "action": "update", "type": "object", "data": {"animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 20000, "easing": "linear"}} }'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/gltf-model_Earth -m '{"object_id" : "gltf-model_Earth", "action": "update", "type": "object", "data": {"startEvents": "click", "property": "scale", "dur": 1000, "from": "10 10 10", "to": "5 5 5", "easing": "easeInOutCirc", "loop": 5, "dir": "alternate"} }'
```
### Add a click-listener
```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/gltf-model_Earth -m '{"object_id" : "gltf-model_Earth", "action": "update", "type": "object", "data": {"click-listener": ""}}'
```
### Create marker objects
```json
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/box0 -m '{"object_id" : "box0", "action": "create", "data": {"color": "blue", "object_type": "cube", "scale":  {"x": 0.2, "y": 0.2, "z": 0.2}, "position": {"x": 0, "y": 0, "z": 0} }}'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/box1 -m '{"object_id" : "box1", "action": "create", "data": {"color": "red", "object_type": "cube", "scale":  {"x": 0.2, "y": 0.2, "z": 0.2}, "position": {"x": -0.7, "y": 1.67, "z": 2.11} }}'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/box2 -m '{"object_id" : "box2", "action": "create", "data": {"color": "red", "object_type": "cube", "scale":  {"x": 0.2, "y": 0.2, "z": 0.2}, "position": {"x": -2.88, "y": 2.80, "z": -2.12} }}'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/box3 -m '{"object_id" : "box3", "action": "create", "data": {"color": "red", "object_type": "cube", "scale":  {"x": 0.2, "y": 0.2, "z": 0.2}, "position": {"x": -0.09, "y": 1.30, "z": -3.66} }}'
mosquitto_pub -h arena.andrew.cmu.edu -t realm/s/example/box4 -m '{"object_id" : "box4", "action": "create", "data": {"color": "red", "object_type": "cube", "scale":  {"x": 0.2, "y": 0.2, "z": 0.2}, "position": {"x": 3.31, "y": 2.00, "z": -0.97} }}'
```
### Results
{% include alert type="warning" title="TODO" content="Include awesome demo result from design doc." %}
