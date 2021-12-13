---
title: Optical Markers
nav_order: 4
layout: tutorial
parent: MR Experiences
---

# Optical Markers

{% include alert type="note" content="
Check out [the AR Experiences Requirements Section](/content/mr/requirements) for requirements of different types of anchors that can be used in ARENA and the browsers that support these.
"%}

ARENA can support different optical markers: [Apriltags](https://april.eecs.umich.edu/software/apriltag), has experimental (outside the mainline code) support for [lightanchors/flash](https://youtu.be/_P01roIG93U), and more are expected to be added.

Optical markers are added to ARENA scenes by attaching **ARMarker** components to scene objects. To perform relocalization, the ARENA location solver must know the pose of the detected marker. It will first try to find objects in the Scene with ARMarkers attached to use the pose of these objects, and if no data about a marker is found in the Scene, it will query ATLAS. Markers with ID 0, however, are assumed to mark the origin: 0, 0, 0 (x, y, z). You can override the ID 0 parameters in the Scene if desired.

This section will describe how this can be achieved and provide a couple of examples.

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/rU6E3LHg0aQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

## Attaching an ARMarker Component to Scene Objects

An ARENA scene might contain several markers with GPS coordinates and local coordinates referenced from the Scene's origin. The following image exemplifies how to attach an **ARMarker** component to a geometry object in a scene (in this case, a box), using the [scene builder](/content/overview/build):

<img src="/assets/img/mr/build-add-armarker.png" width="500"/>

The ARMarker component that will appear at the end of the form will allow defining properties of the marker:

<img src="/assets/img/mr/build-armarker.png" width="500"/>

The image above shows the default ARMarker component attributes. A few more attributes, such as GPS coordinates and a URL attached to the marker can also be added. The examples below will show how to use these properties in more detail using Apriltags, the most common ARMarkers used in ARENA.

## Coordinate System

In ARENA's world coordinate system (shown as i. in the figure below), positive in the x-axis is to the right, positive y-axis is up, and positive z-axis is out of the screen. The origin at 0, 0, 0 (x, y, z) is the center of the world.

<img src="/assets/img/mr/coordinate-sys.png" width="500"/>

The figure shows examples of markers and how their orientation aligns with ARENA's coordinate system. For example, a vertical marker along the world's z-axis (shown as ii. in the figure) does not need a rotation as this aligns with the marker's local coordinate system. However, a marker laid horizontal on the ground (iii. in the figure) is rotated by -90° in the x-axis.

The ARENA pose solver knows the pose of the marker by looking at the object to which a corresponding ARMarker component is attached. To indicate the pose of markers, we enter it as the pose of an object placed in the Scene to which we link an ARMarker component that has the identifier of the marker. See the 'fixed origin maker' example below for a concrete example.


## Examples

[Apriltags](https://april.eecs.umich.edu/software/apriltag) are a common type of low-bit density optical markers that can be used in ARENA. ARENA can decode AprilTags (36h11 family) in browsers that allow camera access (see [the Requirements Section](/content/mr/requirements) for details). The following examples show how to use Apriltags to anchor content in the real world.

### Fixed Origin Marker
To add a marker and reference the Scene's origin in the real world, we add an object (named 'origin-marker' in the example) that will visually represent the marker at coordinates 0,0,0 (x, y, z). Then, we attach an ARMarker component to it. Because the marker is laid horizontally on the ground, we have to rotate the object (that visually represents the marker) by -90° in the x-axis.

Check the example [Scene in ARENA](https://arenaxr.org/public/artags1). The AprilTag references the origin of the Scene in the real world. Here, we placed it near the corner of the carpet:

<img src="/assets/img/mr/scene-origin-tag.png" width="500"/>

In the example, we add a .gltf to the Scene that visually represents the AprilTag and the reference axis. This object is placed at 0, 0, 0 (x, y, z), and we attached an ARMarker with id 0 and size 150 mm (the id and size of the AprilTag placed on the floor), and set it as static (dynamic=false) and not buildable (buildable=false). The object (the .gltf) is rotated by -90° in the x-axis. The entire object definition that you can enter in the scene [scene builder](/content/overview/build) is [here](https://gist.github.com/nampereira/3e4cbf6748b42719ac3bd5d2f8354aad).


### Dynamic Marker

To use a dynamic marker, we need to reference the Scene in the real world first. As shown in the previous example, we can do this by adding an AprilTag at the origin.

Let us say we want to move a geometry, say a box, in the Scene. We add the box to the Scene and attach an ARMarker that we set as **dynamic** (this must be a different id than the AprilTag used to reference the Scene's origin). The second object will move in the Scene every time an observer with **permission to change the Scene** sees the corresponding AprilTag. This last part is essential; observers who cannot change the Scene will not update the box's position.

Check the example here. We have an AprilTag that references the origin **and** a dynamic tag that moves the box. Notably, the dynamic ARMarker component should define the id of the dynamic marker (1) and the size (50 mm).

<img src="/assets/img/mr/scene-dynamic-marker.gif" width="500"/>

The viewer device was an IPad with XRViewer, and the user was logged in ARENA so it could change the box's position once it detected the dynamic AprilTag. In the Scene [scene builder](/content/overview/build), you can edit the Scene permissions to make sure the user logged in to the viewer device can edit the Scene:

<img src="/assets/img/mr/build-scene-permissions.png" width="300"/>

<img src="/assets/img/mr/scene-permissions.png" width="500"/>

For reference, [these are the attributes](https://gist.github.com/nampereira/de5b6286bfb9c4ad79960e767f165315) of the box object (named 'dynamic-box') we attached a dynamic ARMArker (note that the position is just the initial static position; it will be updated once the marker gets in the view of a device with permissions to update it).
