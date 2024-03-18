---
title: Spot AR
nav_order: 4.5
layout: tutorial
parent: XR Experiences
---

# Spot AR

ARENA uses the [WebXR Device API](https://immersiveweb.dev) to drive it's Augmented Reality interface, but not all web browsers support it well yet (Safari/Firefox) on mobile devices. To accommodate Safari and Firefox until they [fully support the WebXR Device API](/content/xr/requirements), we implemented a simple form of computer vision (CV) for AprilTags that uses the fixed position of the user's camera called **Spot AR**.

<img src="/assets/img/xr/spotar-diag.png" width="300"/>

In Spot AR, the device does not yet have access to the accelerometer data usually supplied to the WebXR Device API to account for device drift, so we ask users to stay within the standing position they scan from.

To test **Spot AR**:
1. Scan the QR Code below with your smartphone camera.
1. Visit the scene link from the QR code scan in your phone web browser.
1. Keep your phone camera pointed toward the AprilTag.

<img src="/assets/img/xr/spotar-qrcode.png" width="250"/>
<img src="/assets/img/xr/spotar-apriltag.png" width="250"/>

The QR Code should link to this ARENA scene URL using several of our [URL parameters](/content/interface/params):
- https://arenaxr.org/poster?armode=1&auth=anonymous&camUpdateIntervalMs=16&skipav=1

You can also print and scan our [ARENA poster](/assets/img/xr/ARENA-poster-print.pdf) for your wall, which visits the same link.
