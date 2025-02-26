---
title: Sound
layout: default
parent: Attributes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Sound

Play toy piano sound from a URL when you click a box. Sets click-listener Component, waveform URL, and sound attribute.

The sound component defines the entity as a source of sound or audio. The sound component can be positional and is thus affected by the component's position.

More properties at <a href='https://aframe.io/docs/1.5.0/components/sound.html'>A-Frame Sound</a>.

Additional Python properties are available in the [Sound API Reference](/content/python-api/attributes/sound).

The following source code was mirrored from the `arena-py` [sound.py](https://github.com/arenaxr/arena-py/blob/master/examples/attributes/sound.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

sound = Sound(
    src="store/audio/toypiano/Asharp1.wav",
    on="mousedown",
)

@scene.run_once
def make_music_box():
    my_box = Box(
        object_id="box_asharp",
        position=(2.5, 0.25, -5),
        scale=(0.8, 1, 1),
        material=Material(color="#000000"),
        clickable=True,
        sound=sound,
    )
    scene.add_object(my_box)

scene.run_tasks()
```
