---
title: ARENA Objects
nav_order: 7
layout: default
has_children: true
---

# ARENA Object Schemas and Over-the-Wire Messages

ARENA Scenes are a collection of Entities to which Components can be attached, following [A-Frame's Entity-Component-System (ECS) architecture](https://aframe.io/docs/1.2.0/introduction/entity-component-system.html). All objects have a set of common properties: object id, a type, and an action (create, update, delete). The `persist` flag indicates if [ARENA persist service](/contents/architecture/persistence) should persist this object. Properties in the data sections (`Box Data` in the example figure) are the object-specific properties and components. The example below shows a Box Geometry with depth, height, width properties, and position components. As shown, other properties, such as the segments dimentions, and components (e.g., a click listner, or material properties) can be added to a Box geometry.

<img src="/assets/img/schemas/build-box-object-simple.png" width="100%"/>

All ARENA objects have similar well-defined schemas, and these are the basis for the over-the-wire message format shown below. This is the message format transmitted over the PubSub to create/update/delete objects.
```json
{
  "object_id": "abox",
  "persist": true,
  "type": "object",
  "action": "create",
  "data": {
    "object_type": "box",
    "depth": 1,
    "height": 1,
    "width": 1,
    "position": {
      "x": 0,
      "y": 0,
      "z": 0
    }
  }
}
```

## ARENA Objects and A-Frame

ARENA's 3D environment is built on top of [A-Frame](https://aframe.io/), and it supports the majority of A-Frame's primitives (e.g., geometries like boxes, circles, spheres) and components (that can be attached to objects, such as position, rotation, material, sound). 

To clarify this relation, observe the Box geometry object shown below. The **3D object type** shown, `box`, is the A-Frame primitive used. Any of the properties in the **Box Data** section are properties of [A-Frame's Box primitive](https://aframe.io/docs/1.2.0/primitives/a-box.html). You can see that the properties shown, such as `depth`, `height`, `width`, and other additional properties such as `segments depth`, `segments height` that can be added, all belong to [A-Frame's Box primitive](https://aframe.io/docs/1.2.0/primitives/a-box.html). In fact, any property supported by A-Frame can be added (for example, if A-Frame adds a new property not on ARENA schemas, it can be manually added).

<img src="/assets/img/schemas/build-box-material.png" width="100%"/>

Notice also that the Box geometry has **Material** properties. This represents an [A-Frame's Material Component](https://aframe.io/docs/1.2.0/components/material.html) attached to this geometry. All properties defined here are passed to this A-Frame component.

{% include alert type="tip" content="
Looking up [A-Frame's documentation](https://aframe.io/docs/1.2.0/introduction/) for supported primitives and components is often an excellent way to complement ARENA's documentation and obtain further clarification of the meaning of object's properties.
"%}

**See our [reference of ARENA supported objects and their properties](/content/schemas/definitions).**

## ARENA-Specific components

We also extended A-Frame by building ARENA-specific components and systems for, e.g. AR markers, programs, networked events, and options. 

**The documentation of ARENA-specific components and systems is [here](/content/schemas/arena-aframe-components).**

