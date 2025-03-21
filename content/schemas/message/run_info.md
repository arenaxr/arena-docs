---
title: Execution info
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---

<!--CAUTION: This file is autogenerated from https://github.com/arenaxr/arena-schemas. Changes made here may be overwritten.-->


Execution info
==============


Program execution info, added at runtime.

Execution info Attributes
--------------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|**web_host**|string||ARENA web host.|No|
|**namespace**|string||ARENA namespace.|No|
|**scene**|string||ARENA scene.|No|
|**realm**|string||ARENA realm.|No|
|**filename**|string||Executable filename.|No|
|**args**|string||Command line arguments.|No|
|**env**|string||Value of ARENA-py environment variables.|No|
|**create_time**|string||Program creation time.|No|
|**last_active_time**|string||Program last publish/receive time.|No|
|**last_pub_time**|string||Program last publish time.|No|
|**pub_msgs**|integer||Number of published messages.|No|
|**pub_msgs_per_sec**|number||Published messages per second avg.|No|
|**rcv_msgs**|integer||Number of received messages.|No|
|**rcv_msgs_per_sec**|number||Received messages per second avg.|No|
|**last_rcv_time**|string||Last message receive time.|No|
