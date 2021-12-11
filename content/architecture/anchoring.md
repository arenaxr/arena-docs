---
title: Anchoring to Reality
nav_order: 3
layout: tutorial
parent: Architecture
---

ARENA provides several mechanisms to help streamline the management and sharing of anchor data as well as simplifying the process of combining multiple tracking technologies into a uniform coordinate system. ARENA scenes can be registered and discovered by the Atlas service. Atlas operates in a hierarchical manner much like the Internet’s Domain Name Service (DNS), but using a mixture of GPS coordinates, UUIDs and Scenes instead of domain names. UUID markers can be embedded into QR codes,BLE beacons or other digital markers (WiFi, LTE tower, etc). Atlas can also provide absolute and/or local coordinates for markers that are associated with scenes. For example, a user could scan a QR code or read a BLE beacon which provides a UUID that maps to a GPS coordinate along with any Scenes that contain that GPS coordinate. Atlas stores a GPS location for each Scene along with a 3D bounding polygon. The GPS location is typically assigned to the origin of the Scene’s local coordinate system.  A user can perform follow-up queries to Atlas for assets that fall within each Scene. For example, a Scene might contain a number of AprilTags(low bit-density tracking markers) that have GPS coordinates as well as local coordinates referenced from the Scene’s origin. It is worth noting that a Scene’s address can be used to form a URL for virtual environments that have no physical location.Since Atlas is a public facing entity that needs administrative management, ARENA also supports the ability to store location data within a Scene by attaching real-world properties to objects.

```json
{
   "object_id":"abox",
   "persist":true,
   "type":"object",
   "action":"create",
   "data":{
      "object_type":"box",
      "depth":1,
      "height":1,
      "width":1,
      "position":{
         "x":1,
         "y":1,
         "z":1
      },
      "rotation":{
         "x":0,
         "y":0,
         "z":0
      },
      "armarker":{
         "lat":40.4432,
         "lon":79.9428,
         "markerid":"1",
         "markertype":"apriltag_36h11",
         "size":150,
         "ele":200
      }
   }
}
```
**Figure 1**. Example Box Object with an ARMarker.

Figure 1 shows an example of how a box object in a scene can have an AR marker property attached to it. This simplifies the common case where a developer builds a local scene and wants a quick way to manage beacon data annotations for localization systems. ARmarkers can be set as static or dynamic to determine if clients should use them for relocalization or if clients should provide locationin formation for the tag. Our current client can decode AprilTags in browsers that allow camera access (e.g. Mozilla WebXR Viewer and Chrome). If the client decodes a static tag, it uses the location data to compute the pose of the device’s camera. If the tag is dynamic (and the client has a confident fix on its location), it publishes its estimate of the tag location to that object. In this way, multiple users in a space can update and share the location of dynamic tags. Since these tags are attached to objects, this naturally updates the object positions and is reflected across all users and programs. User cameras and rigs can also be updated by external tracking systems.

For example, a Python agent can convert OptiTrack motion capture objects into ARENA position updates. If you target those outputs to specific user cameras or objects, they are automatically localized within the scene. This seamlessly works side-by-side with devices that use optical tags or even UWB localization. We have a number of helper applications that leverage different localization systems to help build tag maps (e.g. OptiTrack can be used to calibrate AprilTags within a shared space). This is another example where the implicitly networked nature of all objects dramatically simplifies merging data from multiple sensing modalities

# Coordinate Frame

{% include alert type="warning" title="Coming Soon" content="Stay tuned for more details..." %}
