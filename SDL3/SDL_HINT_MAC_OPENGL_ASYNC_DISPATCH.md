###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MAC_OPENGL_ASYNC_DISPATCH

A variable controlling whether dispatching OpenGL context updates should block the dispatching thread until the main thread finishes processing on macOS.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_OPENGL_ASYNC_DISPATCH "SDL_MAC_OPENGL_ASYNC_DISPATCH"
```

## Remarks

The variable can be set to the following values:

- "0": Dispatching OpenGL context updates will block the dispatching thread
  until the main thread finishes processing. (default)
- "1": Dispatching OpenGL context updates will allow the dispatching thread
  to continue execution.

Generally you want the default, but if you have OpenGL code in a background
thread on a Mac, and the main thread hangs because it's waiting for that
background thread, but that background thread is also hanging because it's
waiting for the main thread to do an update, this might fix your issue.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

