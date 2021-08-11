---
title: Runtime
nav_order: 8
layout: default
parent: ARENA Runtime Supervisor
---

# Runtime

ARENA applications are compiled into WebAssembly (WASM),an open standard that defines a portable binary code format for executable programs, currently supported by all major web browsers. WASM programs are run in a secure sandbox and have been gaining traction outside of the browser as a lightweight and secure option for serverless-style computing. There are compilers for many languages that target WASM. ARENA includes a WASM runtime environment for browser-capable devices that leverages the already available browser infrastructure, whereas other headless compute elements run a standalone WASM runtime. We are currently [developing WASM runtimes in both Linux-capable devices and even dispatch Ahead-of-Time (AOT) compiled WASM to microcontrollers](https://github.com/conix-center/arts). Our WASM runtime accepts requests to execute programs, provides sandboxed execution with access to (also sandboxed) networked resources, and manages the WASM programs’ lifetime, including live migration capabilities (i.e.context swap across devices). The WASM runtime provides a basis for agile programs that operate in the dynamic, distributed computing contexts we imagine for future XR applications. It is an enabler for ARENA applications that can span cloud, edge and device plat-forms in a network transparent manner.  We are also developing a program manager for scenes, we call `init3D`, to provide facilities to manage programs interactively from within scenes.
