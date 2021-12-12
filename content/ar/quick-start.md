---
title: Quick Start
nav_order: 1
layout: tutorial
parent: AR Experiences
---

# First AR Scene Example

Try the following for a quick sample of AR using ARENA.

## Requirements

We will use an [Apriltag](https://april.eecs.umich.edu/software/apriltag) optical marker to anchor an ARENA scene in the real world. 

Detection of optical markers requires that the browser supports ARENA's computer vision while in AR mode. Currently, there are a few options to do so. We will quickly describe how to startup this using an Android and an iOS devide. 

{% include alert type="note" content="
Checkout [the AR Experiences Requirements Section](/content/ar/requirements) for details on the requirements of different types of anchors that can be used in ARENA and the browsers that support these.
"%}

**Android**: [Chrome Beta](https://www.google.com/chrome/beta/).
**iOS**: [XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989).

## Open an ARENA Scene in AR

Print out an [AprilTag with ID 0](https://github.com/conix-center/apriltag-gen/blob/master/output/tag36_11_00000.pdf) and open the scene at this URL: [https://arenaxr.org/public/artest?armode=true](https://arenaxr.org/public/artest?armode=true)

{% include alert type="note" content="
The above URL includes an `armode=true` flag which tells ARENA to automatically enter AR by skiping some sound/camera configation steps.

For a quick test, you can also use an Apriltag on a screen. Note however that the ARENA location solver needs to know the size of the tag to accuratelly compute its location (the scene is configured for an Apriltag of size 150x150 mm, and you will have better results if it is this size).
"%}

This should display the following sequence of screens. Click “Allow” for motion and camera access and “Enter” for AR mode.  The “armode=true” URL parameter skips the normal AV setup box.  In that case, the user must select the “AR” button in the lower right to switch into AR mode.

| ![img](/assets/img/ar/enter-ar-1.png){: style="float: left"} | ![img](/assets/img/ar/enter-ar-2.png){: style="float: left"} |
| Provide access to Sensors (1) | Provide access to Sensors (2) |
| ![img](/assets/img/ar/enter-ar-3.png){: style="float: left"} | |
| Scene with origin (x, y, x: 0, 0, 0) anchored by the Apriltag | |
