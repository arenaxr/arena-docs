---
title: 
nav_order: 2
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Program
=======


Program

All wire objects have a set of basic attributes ```{object_id, action, type, persist, data}```. The ```data``` attribute defines the object-specific attributes

Program Attributes
-------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|object_id|string||Object identifier; Must be a valid UUID.|Yes|
|action|string; One of: ```['create', 'delete', 'update', 'clientEvent']```|```'create'```|One of 3 basic Create/Update/Delete actions or a special client event action (e.g. a click)|Yes|
|persist|boolean|```true```|Persist this object in the database|Yes|
|type|string; Must be: ```program```|```'program'```|ARENA program data|Yes|
|data|[program](program)||Object data payload; Program config data|Yes|

### Program Data Attributes

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|name|string||Name of the program in the format namespace/program-name|Yes|
|affinity|string; One of: ```['client', 'none']```|```'client'```|Indicates the module affinity (client=client's runtime; none or empty=any suitable/available runtime)|No|
|instantiate|string; One of: ```['single', 'client']```|```'client'```|Single instance of the program (=single), or let every client create a program instance (=client). Per client instance will create new uuid for each program.|Yes|
|filename|string||Filename of the entry binary|Yes|
|filetype|string; One of: ```['WA', 'PY']```|```'['WA']'```|Type of the program (WA=WASM or PY=Python)|Yes|
|args|array||Command-line arguments (passed in argv). Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key}|No|
|env|array|```['MID=${moduleid}', 'SCENE=${scene}', 'NAMESPACE=${namespace}', 'MQTTH=${mqtth}', 'REALM=realm']```|Environment variables. Supports variables: ${scene}, ${namespace}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key}|Yes|
|channels|array|```[{'path': '/ch/${scene}', 'type': 'pubsub', 'mode': 'rw', 'params': {'topic': 'realm/s/${scene}'}}]```|Channels describe files representing access to IO from pubsub and client sockets (possibly more in the future; currently only supported for WASM programs).|No|