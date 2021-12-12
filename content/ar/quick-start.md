---
title: Quick AR Taste
nav_order: 1
layout: tutorial
parent: AR Experiences
---

# Quick AR Experience Example

Try the following for a quick sample of AR using ARENA by opening a pre-made scene and achoring it in the real world with an optical marker.

## Requirements

We will use an [Apriltag](https://april.eecs.umich.edu/software/apriltag) optical marker to anchor an ARENA scene in the real world. 

Detection of optical markers requires that the browser supports ARENA's computer vision while in AR mode. For this quick test, we suggest [Chrome Beta](https://www.google.com/chrome/beta/) on Android or [XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989) on iOS. 

{% include alert type="note" content="
Check out [this](/content/ar/requirements) Requirements Section for details on the requirements of different types of anchors that can be used in ARENA and the browsers that support these.
"%}

## Open an ARENA Scene in AR

Print out (or display on a screen[^1]) an [AprilTag with ID 0](https://github.com/conix-center/apriltag-gen/blob/master/output/tag36_11_00000.pdf) and open the scene at the following URL[^2]: 

[https://arenaxr.org/public/artest?armode=true](https://arenaxr.org/public/artest?armode=true)<br/>
<img src="/assets/img/ar/artest-url-qr-code.svg" width="200"/>

{% include alert type="note" content="
Use the QR Code to quickly open the URL. See some instructions about doing this using **XR Browser** [further down](#open-scene-from-qr-code-xr-viewer-only).
"%}

[^1]: For a quick test, you can also use an Apriltag on a screen. Note, however, that the ARENA location solver needs to know the size of the tag to accurately compute its location (this information comes from the ARMarker object in the scene, which, in this scene, is configured for an Apriltag of size 150x150 mm).

[^2]: The URL includes an `armode=true` flag which tells ARENA to automatically enter AR by skipping some AV setup steps. If this flag is not present, the user must select the <button type="button" name="button" class="btn fs-3 ">AR</button> button in the lower right to switch into AR mode.

Opening the URL should display the following sequence of screens. Click “Allow” for motion and camera access and “Enter” for AR mode.  

| ![img](/assets/img/ar/enter-ar-1.png){: style="float: left"} | ![img](/assets/img/ar/enter-ar-2.png){: style="float: left"} |
| Provide access to sensors (1) | Enter AR mode confirmation |

Finally, point the device to the Apriltag, and scene's origin should be anchored to it:
<img src="/assets/img/ar/enter-ar-3.png" width="100%"/>

### Open Scene From QR Code (XR Browser)

[XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989) supports loading a URL from a QR code: 

**i)** Tap the address bar. The QR code scanner button will show up on the right.
<img src="/assets/img/ar/xrbrowser-qr-code.png" width="400"/>

**ii).** XR Browser will open your phone camera for scanning QR codes after you grant it permission.

**iii)** Position the QR code to align it within the frame outlined by the four blue corners. XR Browser will automatically scan the QR code once it detects proper alignment.

**iv)** After scanning (because the QR code is a web address), the page will open.

#### Footnotes
