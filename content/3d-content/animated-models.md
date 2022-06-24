---
title: Animated Models
layout: default
parent: 3D Content
---

# Animated Models

## Animate (rotation)

Animate rotation of the already drawn cube.

Raw Message

```json
arena-py-pub -mh mqtt.arenaxr.org -s example -m '{"object_id" : "cube_1", "action": "update", "type": "object", "data": { "animation": { "property": "rotation", "to": "0 360 0", "loop": true, "dur": 10000}} }'
```

Python

```python
cube.update(data='{"animation": {"property":"rotation", "to":"0 360 0", "loop":"true", "dur":10000}}')
```

other animations are available that resemble the `"data": {"animation": { "property": ... }}` blob above: see [A-Frame Animation](https://aframe.io/docs/1.3.0/components/animation.html) documentation for more examples
