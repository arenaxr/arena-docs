---
title: Matterport Large Scans
layout: default
parent: 3D Content
---

{% include alert type="warning" title="Coming Soon" content="Stay tuned for more details..." %}

# Scanning a Large Space with Matterport
For higher fidelity models, we use the Leica BLK360, a terrestrial laser scanner (TLS) with registered 360 color images.
Using the BLK360, along with 3D reconstruction software (e.g. Leica’s [Cyclone FIELD 360](https://leica-geosystems.com/en-us/products/laser-scanners/software/leica-cyclone/leica-cyclone-field-360), or [Matterport](https://matterport.com)), we create 3D models of physical spaces that can easily be imported into ARENA.

1. We place the laser scanner at different spots around the venue that are merged to create the final model.
1. Each scan can take 30 seconds, or up to 2 minutes, depending on the resolution of the scan (we often use the fastest setting).
1. The scan density might vary significantly from space to space, where large open spaces can be captured with few scans, and more complex areas require more scans due to occlusion.
1. Before loading the model into ARENA, manual adjustments to simplify the model can be made using, e.g., [Blender](https://www.blender.org).

{% include alert type="tip" title="Example" content="A model with over 400 square meters took less than 30 minutes to capture for us. A typical venue model (two floors, over 400 square meters) is less than 100MB, larger models can be split and loaded dynamically using a Level-of-Detail (LOD) mechanism that allows to load increasingly more detailed models as a users approaches." %}
