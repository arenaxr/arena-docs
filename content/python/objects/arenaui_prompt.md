---
title: ArenauiPrompt
layout: default
parent: Objects
grand_parent: Python Library
---

# ARENAUI Prompt

Similar to a button panel, this prompt is intended to be used a quick confirmation popup.
Its buttons may be customized and an additional text description can be included, similar
to what one may see in traditional 2D web interfaces.

Additional Python properties are available in the [ArenauiPrompt API Reference](/content/python-api/objects/arenaui_prompt).

The following source code was mirrored from the `arena-py` [arenaui_prompt.py](https://github.com/arenaxr/arena-py/blob/master/examples/objects/arenaui_prompt.py) example.

```python
from arena import *

scene = Scene(host="arenaxr.org", scene="example")

@scene.run_once
def make_ui_prompt():
    # Add a popup prompt with single button
    def prompt_handler(_scene, evt, _msg):
        if evt.type == "buttonClick":
            if evt.data.buttonName == "OK":
                print("OK clicked!")
                scene.delete_object(prompt)

    prompt = ArenauiPrompt(
        object_id="promptA",
        title="Prompt A",
        description="This is a prompt with a description.",
        buttons=["OK"],
        position=Position(2, 2, -2),
        evt_handler=prompt_handler,
    )
    scene.add_object(prompt)

scene.run_tasks()
```
