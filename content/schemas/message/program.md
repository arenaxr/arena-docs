---
title: 
nav_order: 30
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Program Data
============


Object data payload; Program config data

Program Data Attributes
------------------------

|Attribute|Description|Type|Default|Required|
| :--- | :--- | :--- | :--- | :--- |
|name|Name of the program in the format namespace/program-name|string||Yes|
|affinity|Indicates the module affinity (client=client's runtime; none or empty=any suitable/available runtime)|string; One of: ```['client', 'none']```|```'client'```|No|
|instantiate|Single instance of the program (=single), or let every client create a program instance (=client). Per client instance will create new uuid for each program.|string; One of: ```['single', 'client']```|```'client'```|Yes|
|filename|Filename of the entry binary|string||Yes|
|filetype|Type of the program (WA=WASM or PY=Python)|string; One of: ```['WA', 'PY']```|```'['WA']'```|Yes|
|args|Command-line arguments (passed in argv). Supports variables: ${scene}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key}|array||No|
|env|Environment variables. Supports variables: ${scene}, ${namespace}, ${mqtth}, ${cameraid}, ${username}, ${runtimeid}, ${moduleid}, ${query-string-key}|array|```['MID=${moduleid}', 'SCENE=${scene}', 'NAMESPACE=${namespace}', 'MQTTH=${mqtth}', 'REALM=realm']```|Yes|
|channels|Channels describe files representing access to IO from pubsub and client sockets (possibly more in the future; currently only supported for WASM programs).|array|```[{'path': '/ch/${scene}', 'type': 'pubsub', 'mode': 'rw', 'params': {'topic': 'realm/s/${scene}'}}]```|No|
