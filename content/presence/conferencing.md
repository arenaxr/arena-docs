---
title: Conferencing
nav_order: 5
layout: default
parent: Presence
---

# Conferencing
<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/RorgGVWEIdk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

{% include alert type="warning" title="Coming Soon" content="Stay tuned for more details..."%}

## Audio

## Video

## Screen Sharing
When you click and accept the screenshare icon and popup, it will ask for the object name/id of the object you want to screen share on (defaulted to an object with object_id: `screenshare`, which is dynamically created if it doesn't exist already). 
- If you choose the name/id of an already existing object in a scene, it will set the texture of that existing object to be your screen. 
- If you choose an object that does not exist in a scene, it will spawn a new screen sharing plane with your chosen object_id. This object is not sent through MQTT bus but is still created for all clients.
- Once you have selected your object name, it will open a new tab that allows you to choose which screen you want to share, and ARENA will automatically place that screen onto the object with an object_id you specified.
- You can do whatever you want the object you’re screen sharing on as if it were a normal arena object (change size, shape, attach children, etc). This also applies to the object `screenshare`; its just a standard ARENA object with object_id: `screenshare`!
- When an object is dynamically created with the screen share button, it won't go away after you stop screen sharing. It will only go away if you refresh the page.
