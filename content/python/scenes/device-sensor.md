---
title: DeviceSensor
layout: default
parent: Scenes
grand_parent: Python Library
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pexample, changes here may be overwritten. -->

# Device Sensor

The following source code was mirrored from the `arena-py` [device-sensor.py](https://github.com/arenaxr/arena-py/blob/master/examples/scenes/device-sensor.py) example.

```python
import json
from datetime import datetime

from arena.device import Device

device = Device(host="arenaxr.org", device="robot1")
CUSTOM_TOPIC = f"{device.realm}/d/{device.namespace}/{device.device}/rtc1"

def on_recv_message(client, userdata, msg):
    try:
        payload_str = msg.payload.decode("utf-8", "ignore")
        payload = json.loads(payload_str)
        print(payload)
    except:
        pass

device.message_callback_add(CUSTOM_TOPIC, on_recv_message)

@device.run_forever(interval_ms=1000)
def on_second_publ_message():
    payload = {}
    d = datetime.now().isoformat()[:-3]+"Z"
    payload["timestamp"] = d
    payload = json.dumps(payload)
    device.publish(CUSTOM_TOPIC, payload)

device.run_tasks()
```
