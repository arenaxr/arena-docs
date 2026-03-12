---
title: Permissions Guide
nav_order: 3
layout: tutorial
parent: Architecture
---

# Permissions Guide

> **Versioning Note:** This document describes the **V2** `arena-services-docker` MQTT topic permissions, requiring compatible V2+ server environments and ARENA `py`/`unity` clients V1+.

This guide outlines the MQTT publish and subscribe permissions granted to users connecting to the ARENA message broker. Permissions are embedded in the JSON Web Token (JWT) provided by the `arena-account` service, which acts as the Access Control List (ACL) enforced by the Mosquitto broker.

## Overview

Permissions depend on a user's role (Staff, Authenticated User, Anonymous), the token type requested (Scene vs. Device), and the specific scene's settings.

---

## 1. Global Public Scope

**All Users** (regardless of authentication, unless it is a specific device token limit) are granted read access to the global public scenes namespace.
* **Subscribe:** `{realm}/s/public/+/+/+`

---

## 2. Authenticated Users

Authenticated users possess specific rights depending on their role.

### Administrators / Staff
Staff users have full access to view and modify any object within any scene or device namespace.
* **Subscribe:** `{realm}/s/+/+/+/+/+` (Read all scene data)
* **Publish:** `{realm}/s/+/+/o/{userclient}/#` (Write objects to all scenes)
* **Subscribe / Publish:** `{realm}/d/#` (All device objects)

### Standard Authenticated Users
Regular users have full access over their own personal namespaces.
* **Subscribe:** `{realm}/s/{username}/+/+/+/+` (Read user's scene data)
* **Publish:** `{realm}/s/{username}/+/o/{userclient}/#` (Write objects to user's scenes)
* **Subscribe / Publish:** `{realm}/d/{username}/#` (User's device objects)

Users can also be granted **Editor** or **Viewer** rights to specific namespaces and scenes.
* **Subscribe:** `{realm}/s/{namespace}/{scene-id}/+/+/+` (For each scene the user has rights to)
* **Publish:** `{realm}/s/{namespace}/{scene-id}/o/{userclient}/#` (For each scene the user is an editor of)

### Device Tokens
If an authenticated user requests a specific device token (e.g., for headless devices under their account).
* **Subscribe / Publish:** `{realm}/d/{namespace}/{device_id}/#` (Device payload objects)

---

## 3. Scene-Level Permissions

When a user joins a specific scene, they are granted permissions based on the scene's settings (e.g., Public Read, Public Write, Anonymous Allowed).

**Anonymous Access Restrictions:**
If the user is not authenticated and the scene has `anonymous_users=False`, no permissions are granted (token generation is rejected).

**Scene Read/Write Options:**
Depending on whether the scene allows public read or write access:
* **Read Scene Objects:** `{realm}/s/{namespace}/{scene-id}/+/+/+` (Subscribe)
* **Modify Scene Objects:** `{realm}/s/{namespace}/{scene-id}/o/{userclient}/#` (Publish)

**User Presence (Camera and Hands):**
If the token request provides camera and controller IDs and the user is permitted in the scene, they are granted rights to update their own avatar's pose/object (`u/` msgType):
* **Publish (Head/Camera):** `{realm}/s/{namespace}/{scene-id}/u/{userclient}/{camid}` and `.../{camid}/+`
* **Publish (Left Hand):** `{realm}/s/{namespace}/{scene-id}/u/{userclient}/{handleftid}` and `.../{handleftid}/+`
* **Publish (Right Hand):** `{realm}/s/{namespace}/{scene-id}/u/{userclient}/{handrightid}` and `.../{handrightid}/+`

---

## 4. Chat and Messaging

If a user is inside a scene and provides a `userid`, they can participate in the chat system or send presence updates. (`c` and `x` msgTypes).

* **Receive All Chat:** `{realm}/s/{namespace}/{scene-id}/+/+/+` (Handled by general scene read)
* **Receive Private Messages:** `{realm}/s/{namespace}/{scene-id}/+/+/+/{userid}/#` (Subscribe)
* **Send Open Messages:** `{realm}/s/{namespace}/{scene-id}/c/{userclient}/{userid}` (Publish)
* **Send Private Messages:** `{realm}/s/{namespace}/{scene-id}/c/{userclient}/{userid}/{to_userid}` (Publish)

---

## 5. Sub-Systems and Components

User tokens additionally grant read and write scopes for subsystems running on the server:

### Render, Environment, and Debug
These topics end with an exact dash `-` to block unauthorized users from subscribing to and sniffing pseudo-group render payloads:
* **Publish (Render):** `{realm}/s/{namespace}/{scene-id}/r/{userclient}/{userid}/-`
* **Publish (Environment):** `{realm}/s/{namespace}/{scene-id}/e/{userclient}/{userid}/-`
* **Publish (Debug):** `{realm}/s/{namespace}/{scene-id}/d/{userclient}/{userid}/-`

### AprilTags
Users within a scene can publish and subscribe to AprilTag topics:
* **Subscribe / Publish:** `{realm}/g/a/#`

### Runtime Manager (Silverline)
Global namespace-level topic for controlling runtime processes:
* **Subscribe / Publish:** `{realm}/g/{namespace}/p/+`

Scene-level program topic:
* **Publish:** `{realm}/s/{namespace}/{scene-id}/p/{userclient}/{userid}`
* **Subscribe / Publish:** `{realm}/s/{namespace}/{scene-id}/p/+/#` (Editors)

### Network Graph
Topics used for visualizing and measuring network latencies and topologies:
* **Subscribe:** `$NETWORK`
* **Publish:** `$NETWORK/latency`
