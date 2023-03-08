---
layout: default
parent: Objects Schema
grand_parent: ARENA Objects
---


Box Collision Listener
========

Listen for bounding-box collisions with user camera and hands. Must be applied to an object or model with geometric mesh.


Box Collision Listener Attributes
--------------------

| Attribute | Type    | Default     | Description                                                                                       | Required |
|:----------|:--------|:------------|:--------------------------------------------------------------------------------------------------|:---------|
| enabled   | boolean | ```True```  | Publish detections, set `false` to disable                                                        | No       |
| dynamic   | boolean | ```False``` | **Important:** set `true` for moving objects, so that its bounding box is constantly recalculated | Yes      |
 
