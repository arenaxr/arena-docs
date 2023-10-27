---
title: miXed Reality
nav_order: 1.3
layout: tutorial
parent: Tutorial
---

# Quick XR Experience Example

ARENA has seamless support for a spectrum of experiences, from completely immersing the user in a digital world (Virtual Reality; **VR**) to enhancing the real world with interactive digital content (Augmented Reality; **AR**). A spectrum often identified as **miXed Reality (XR)**. Try the following for a quick sample of AR using ARENA by opening a pre-made scene and anchoring it in the real world with an optical marker.

For simplicity, here we suggest a pass-through AR experience using the back-facing camera of a phone or tablet to capture the world and display the mix of virtual and real contents on the screen (options using Android and iOS below). In the [XR Section](/content/xr/) you can find more information about using ARENA for XR, including different types of anchors, and supported devices.

## Requirements

We will use an [AprilTag](https://april.eecs.umich.edu/software/apriltag) optical marker to anchor an ARENA scene in the real world.

Detection of optical markers requires that the browser supports ARENA's computer vision while in AR mode. For this quick test, we suggest [Chrome Beta](https://www.google.com/chrome/beta/) on Android or [XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989) on iOS.

{% include alert type="note" content="
Check out the [XR Requirements Section](/content/xr/requirements) for details on the requirements of different types of anchors that can be used in ARENA and the browsers that support these.
"%}

## Open an ARENA Scene in AR

1. Print out (or display on a screen[^1]) an [AprilTag with ID 0](https://raw.githubusercontent.com/arenaxr/apriltag-gen/master/output/tag36_11_00000.pdf). It should look like the image above.
2. Then, open the scene by entering the following URL[^2] in the address bar of **either [Chrome Beta](https://www.google.com/chrome/beta/) on Android or [XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989) on iOS**:

    **[https://arenaxr.org/public/artest?armode=true](https://arenaxr.org/public/artest?armode=true)**<br/>

{% include alert type="note" content="
See instructions on using a **QR Code to quickly open the URL on XR Browser** [further down](#open-scene-from-qr-code-xr-browser).
"%}

[^1]: For a quick test, you can also use an AprilTag on a screen. Note, however, that the ARENA location solver needs to know the size of the tag to accurately compute its location (this information comes from the ARMarker object in the scene, which, in this scene, is configured for an AprilTag of size 150x150 mm).

[^2]: The URL includes an `armode=true` flag which tells ARENA to automatically enter AR by skipping some AV setup steps. If this flag is not present, the user must select the **\[ AR \]** button in the lower right to switch into AR mode.

Opening the URL should display the following sequence of screens. Click “Allow” for motion and camera access and “Enter” for AR mode.

| ![img](/assets/img/xr/enter-ar-1.png){: style="float: left"} | ![img](/assets/img/xr/enter-ar-2.png){: style="float: left"} |
| Provide access to sensors (1) | Enter AR mode confirmation |

Finally, point the device to the AprilTag, and scene's origin should be anchored to it:
<img src="/assets/img/xr/enter-ar-3.png" width="100%"/>

### Open Scene From QR Code (XR Browser)

[XR Browser](https://apps.apple.com/us/app/xr-browser/id1588029989) supports loading a URL from a QR code:
> **i)** Tap the address bar. The QR code scanner button will show up on the right.
> <img src="/assets/img/xr/xrbrowser-qr-code.png" width="400"/>
>
> **ii).** XR Browser will open your phone camera for scanning QR codes after you grant it permission.
>
> **iii)** Position the following QR code to align it within the frame outlined by the four blue corners. XR Browser will automatically scan the QR code once it detects proper alignment.
> <img src="/assets/img/xr/artest-url-qr-code.svg" width="200"/><br/>
>
> **iv)** After scanning (because the QR code is a web address), the page will open.

{% include alert type="goal" content="
Experiment with viewing 3D content in XR, Mixed Reality.
"%}

#### Footnotes
