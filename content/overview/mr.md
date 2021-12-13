---
title: Mixed Reality
nav_order: 4
layout: tutorial
parent: Overview
---

# Quick MR Experience Example

ARENA has seamless support for a spectrum of experiences, from completely immersing the user in a digital world (Virtual Reality; **VR**) to enhancing the real world with interactive digital content (Augmented Reality; **AR**). A spectrum often identified as **miXed Reality (XR)**. Try the following for a quick sample of AR using ARENA by opening a pre-made scene and anchoring it in the real world with an optical marker. 

For simplicity, here we suggest a pass-through AR experience using the back-facing camera of a phone or tablet to capture the world and display the mix of virtual and real contents on the screen (options using Android and iOS below). In the [MR Section](/content/mr/) you can find more information about using ARENA for MR, including different types of anchors, and supported devices.

## Requirements

We will use an [AprilTag](https://april.eecs.umich.edu/software/apriltag) optical marker to anchor an ARENA scene in the real world.

Detection of optical markers requires that the browser supports ARENA's computer vision while in AR mode. For this quick test, we suggest [Chrome Beta](https://www.google.com/chrome/beta/) on Android or [XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) on iOS.

{% include alert type="note" content="
Check out [this](/content/mr/requirements) Requirements Section for details on the requirements of different types of anchors that can be used in ARENA and the browsers that support these.
"%}

## Open an ARENA Scene in AR

Print out (or display on a screen[^1]) an [AprilTag with ID 0](https://github.com/conix-center/apriltag-gen/blob/master/output/tag36_11_00000.pdf) and open the scene at the following URL[^2]:

[https://arenaxr.org/public/artest?armode=true](https://arenaxr.org/public/artest?armode=true)<br/>
<img src="/assets/img/mr/artest-url-qr-code.svg" width="200"/>

{% include alert type="note" content="
Use the QR Code to quickly open the URL. See some instructions about doing this using **XRBrowser** [further down](#open-scene-from-qr-code-xrbrowser).
"%}

[^1]: For a quick test, you can also use an AprilTag on a screen. Note, however, that the ARENA location solver needs to know the size of the tag to accurately compute its location (this information comes from the ARMarker object in the scene, which, in this scene, is configured for an AprilTag of size 150x150 mm).

[^2]: The URL includes an `armode=true` flag which tells ARENA to automatically enter AR by skipping some AV setup steps. If this flag is not present, the user must select the <button type="button" name="button" class="btn fs-3 ">AR</button> button in the lower right to switch into AR mode.

Opening the URL should display the following sequence of screens. Click “Allow” for motion and camera access and “Enter” for AR mode.

| ![img](/assets/img/mr/enter-ar-1.png){: style="float: left"} | ![img](/assets/img/mr/enter-ar-2.png){: style="float: left"} |
| Provide access to sensors (1) | Enter AR mode confirmation |

Finally, point the device to the AprilTag, and scene's origin should be anchored to it:
<img src="/assets/img/mr/enter-ar-3.png" width="100%"/>

### Open Scene From QR Code (XRBrowser)

[XRBrowser](https://apps.apple.com/us/app/xr-browser/id1588029989) supports loading a URL from a QR code:

**i)** Tap the address bar. The QR code scanner button will show up on the right.
<img src="/assets/img/mr/xrbrowser-qr-code.png" width="400"/>

**ii).** XRBrowser will open your phone camera for scanning QR codes after you grant it permission.

**iii)** Position the QR code to align it within the frame outlined by the four blue corners. XRBrowser will automatically scan the QR code once it detects proper alignment.

**iv)** After scanning (because the QR code is a web address), the page will open.

#### Footnotes
