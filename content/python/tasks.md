---
title: Tasks
nav_order: 5
layout: default
parent: Python Library
---

# Tasks in arena-py

Tasks are ways you can run programs in the ARENA.

You can think of tasks like threads. In fact, they behave a bit like Python threads, but unlike threads,
arena-py tasks are all run in a single event loop.

## Run Tasks/Start Event Loop
```python
scene.run_tasks()
```

## Stop Running Tasks/Stop Event Loop
```python
scene.stop_tasks()
```

## Tasks

You can run a task once at startup:
```python
@scene.run_once
def f():
    print("here on startup")

# or do this:
scene.run_once(f)
```

You can run a task after a specified period of time (after [interval_ms] milliseconds):
```python
@scene.run_after_interval(interval_ms=1000)
def f():
    print("here, but after 1 second")

# or do this:
scene.run_after_interval(f, 1000)
```

You can run a task every [interval_ms] milliseconds:
```python
@scene.run_forever(interval_ms=10000)
def f():
    print("here, but after 10 seconds")

# or do this:
scene.run_forever(f, 10000)
```

You can run an async task (for advanced users who want to use asyncio to have more control over what their tasks are doing):
```python
@scene.run_async
def f():
    print("here")
    await scene.sleep(5000) # must use scene.sleep or asyncio.sleep. DO NOT use time.sleep!
    print("here, but after 5 seconds")

# or do this:
scene.run_async(f, 1000)
```

## Sharing global variables
Like with threads, global variables in arena-py must be used with the "global" keyword.
Note: If global variables are pointing to something allocated in memory (like a class or list), "global" may not be needed, but it's always best to use "global" just to be safe.

```python
x = 0

@scene.run_once
def main():
    global x # note the use of "global"
    x += 1
    print(x)

@scene.run_after_interval(interval_ms=1000)
def hello():
    global x # note the use of "global"
    x += 1
    print(x)

# below might not work as intended
@scene.run_after_interval(interval_ms=2000)
def hello1():
    # note the lack of "global"
    x += 1
    print(x)
```

## Arguments
You can add arguments to tasks like so:
```python
@scene.run_once(text="arena-py 2.0!", parent="sphere")
def make_text(text, parent):
    text_obj = Text(value=text, position=(0,1.5,0), parent=parent)
    scene.add_object(text_obj)

# scene.run_once(make_text, text="arena-py 2.0!", parent="sphere") # also works
```

```python
objs = []

@scene.run_forever(interval_ms=1234, objs=objs)
def forever(objs):
    for o in objs:
        print(o)

# scene.run_forever(forever, 1234, objs=objs) # also works
```
