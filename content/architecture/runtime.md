---
title: ARENA Runtime
nav_order: 6
layout: default
parent: Architecture
---

## ARENA Runtime

ARENA applications are compiled into WebAssembly (WASM),an open standard that defines a portable binary code format for executable programs, currently supported by all major web browsers. WASM programs are run in a secure sandbox and have been gaining traction outside of the browser as a lightweight and secure option for serverless-style computing. There are compilers for many languages that target WASM. ARENA includes a WASM runtime environment for browser-capable devices that leverages the already available browser infrastructure, whereas other headless compute elements run a standalone WASM runtime. We are currently developing [WASM runtimes](https://github.com/SilverLineFramework/orchestrator) in both Linux-capable devices and even dispatch Ahead-of-Time (AOT) compiled WASM to microcontrollers. Our WASM runtime accepts requests to execute programs, provides sandboxed execution with access to (also sandboxed) networked resources, and manages the WASM programs’ lifetime, including live migration capabilities (i.e.context swap across devices). The WASM runtime provides a basis for agile programs that operate in the dynamic, distributed computing contexts we imagine for future XR applications. It is an enabler for ARENA applications that can span cloud, edge and device plat-forms in a network transparent manner.  We are also developing a program manager for scenes, we call `init3D`, to provide facilities to manage programs interactively from within scenes.

# ARENA Runtime Orchestrator

By leveraging a common runtime and carefully integrated resource monitoring, the ARENA Orchestrator can handle very heterogenous compute resources, across compute classes, from small embedded devices to edge servers. It is distinct from several previous frameworks for managing distributed computing in that it focus on adaptation to changing resources and support for highly heterogenous distributed systems found at the edge.

The ARENA Orchestrator is responsible for managing computational resources available in an ARENA realm (realms represent a geographically distinct set of resources; see [Architecture](/content/architecture/)). It uses [WASM modules](https://webassembly.github.io/spec/core/syntax/modules.html) as a basic compute unit that can run in isolation in a distributed set of available [runtimes](runtime), which run in, e.g., headsets, phones, laptops, embedded routers or edge servers. Runtimes register in ARTS their availability, resources. and system access APIs implemented.

As applications are started in the ARENA (Figure 1), the orchestrator decides the best available compute resource(s) to run the application and monitors its execution do adapt to changing resource availability and consumption. This execution-time adaptation is a unique aspect of ARTS that leverages an important feature: **live migration of WASM modules** (see [runtime](runtime)).

![img](/assets/img/arena-arts-app-start.png)

 **Figure 1**. Starting a new Application in the ARENA

See the [Orchestrator github](https://github.com/SilverLineFramework/orchestrator).


The [ARENA Programs](/content/programs) Section details how to start programs within a scene using the ARENA runtime.
