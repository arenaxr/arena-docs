---
title: User Account
nav_order: 2
layout: default
parent: Users & Security
---

# ARENA User Account Options

{% include alert type="warning" title="warning" content="Writing in progress..." %}

## User Profile
Each authenticated user has a profile page to manage their user account options.
Your profile page will show you a list of scenes that you have rights to edit.

## Scene Permissions, defaults
Each scene has a number of default options to manage security and access to the scene.
Each scene you create will be published under your user namespace with the following rights.
- public Read: enabled
- public write: disabled
- allow anonymous: enabled

## Public scenes
By default, scenes published under the public namespace are always considered Public Read in the ARENA.

## User scenes

## Allow Anonymous
Default: enabled. Disabling allow anonymous for your scene will cause any anonymous visitor to your scene to denied access to view the scene or share the video conferencing features, allowing only authenticated users access to those resources.

## Public Read
Default: enabled. Disabling public read will prevent all normal users from accessing your scene: except those who have the admin or staff roles, and those users you white list as editors to view and conference in the scene.

## Public Write
Default: disabled. This denotes that all users may write to the scene and create change or delete content. This is disabled by default.

## ACL Default New Users

Approaches: We want all users to have the ability to view and move in scenes easily.
Default Viewer Closed (current):

- User gets read access to all.
- User gets write access to personal objects (camera, controllers, avatar) only.
- User must apply for writing other scene objects through the ACL website, awaiting scene owners permission.
