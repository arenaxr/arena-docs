---
title: Objects
nav_order: 3
layout: default
parent: Unity Library
---

# ARENA Unity Objects
This library provides you some options to manage CRUD operations on ARENA Persist objects during Runtime(**Play**). Each operation will publish the appropriate ARENA message for the persistence database and other client subscribers to the scene.

## Create
- Create any Unity GameObject and drag it as a parent of the `ARENA CLient Runtime` in the `Hierarchy`.
- Create any ARENA GameObject using the menu `GameObject > ARENA > [object_type]`.
- Name conflicts or non-ARENA-safe characters will be altered automatically.

## Update
- `Scene` view: Change the `Transform` using the TRS graphic manipulation tools.
- `Inspector` Transform: Change the `Transform` by editing it's values manually.
- `Inspector` ArenaObject: Use `Publish Unity Data` to publish non-Transform changes like Color or Transparency.
- `Inspector` ArenaObject: Edit `Json Data` and use `Publish json Data` to manually publish.

## Rename
- Change the name of any ARENA object to publish the appropriate `create` and `delete` messages:
    - `Hierarchy` list item for an ArenaObject.
    - `Inspector` view for an ArenaObject.
    - App menu `Edit > Rename`.
    - Context menu `Rename`.

## Delete
- Select one or many ARENA objects:
    - Keystroke delete.
    - App menu `Edit > Delete`.
    - Context menu `Delete`.
- `Edit > Undo Create` just after creating an object also works to delete.
- Every delete command on ARENA objects that you initiate will ask you to confirm first.
