---
title: User Account
nav_order: 2
layout: default
parent: Users & Security
---

# ARENA User Account Options

Authenticated users of the ARENA have a user account with which they can alter public access to any scenes they may create.

## User Profile

Each authenticated user has a profile page to manage their user account options. Your profile page will show you a list of scenes that you have rights to edit.

<!-- image profile link nav bar -->
<!-- image profile link scene -->
<!-- image profile list -->

## User Roles

The first time a user is authenticated in the ARENA they have the **User** role by default. The **Staff** role may be applied by another **Admin** user.

- **Admin**: Admin user, local username/password authenticated
- **Staff**: Elevated/Admin Oauth authenticated user
- **User**: Regular Oauth authenticated user
- **Anonymous**: Unauthenticated user

## Scene Permissions

Each scene has some options to manage permissions and access to the scene. Each scene you create will be published under your user namespace with the following rights by default.

- Public Read: **enabled**
- Public Write: **disabled**
- Allow Anonymous: **enabled**
- Editors: **none**

<!-- image permissions edit -->

### Public Read

Disabling public read will prevent all other users from viewing your scene: except those who have the **Admin** or **Staff** roles.

### Public Write

This is disabled by default, preventing all other users from altering your scene: except those who have the **Admin** or **Staff** roles, and those users you whitelist as **Editor** in the scene.

{% include alert type="warning" title="Warning" content="Enabling this denotes that all users may write to the scene and create, change, or delete content." %}

### Allow Anonymous

Disabling this will cause any **Anonymous** visitor to your scene to be denied access to view the scene or share the video conferencing features, allowing only authenticated users access to those resources.

### Editors

You can use this setting to add or remove other users you may whitelist who can create or alter elements of your scene.

## Public Scenes

By default, scenes published under the `public` namespace are always considered Public Read in the ARENA.

## ACL Default For New Users

We want all users to have the ability to view and move in scenes easily. For this, we use a default Viewer-Closed model:

- A user gets read access to all.
- A user gets write access to personal objects (camera, hand controllers, avatar) only.
- A user must apply for write access for other scene objects through the ACL website, awaiting scene owner's permission.

## Administrator Functions

**Admin** users have an additional function on their profile page. There is a **Staff Users** list which will be empty when the ARENA is first deployed. Here an **Admin** can set which authenticated users have the **Staff** user role.
