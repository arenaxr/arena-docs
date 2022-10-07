---
title: 
nav_order: 47
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Text Input
==========


Opens an HTML prompt when clicked. Sends text input as an event on MQTT. Requires click-listener.

Text Input Attributes
----------------------

|Attribute|Type|Default|Description|Required|
| :--- | :--- | :--- | :--- | :--- |
|on|string; One of: ```['mousedown', 'mouseup', 'mouseenter', 'mouseleave', 'triggerdown', 'triggerup', 'gripdown', 'gripup', 'menudown', 'menuup', 'systemdown', 'systemup', 'trackpaddown', 'trackpadup']```|```mousedown```|A case-sensitive string representing the event type to listen for, e.g. 'mousedown', 'mouseup'. See https://developer.mozilla.org/en-US/docs/Web/Events|No|
|title|string|```Text Input```|The prompt title|No|
|label|string|```Input text below (max is 140 characters)```|Text prompt label|No|
|placeholder|string|```Type here```|Text input place holder|No|
