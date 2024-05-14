###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MAC_OPENGL_ASYNC_DISPATCH

A variable controlling whether dispatching OpenGL context updates should block the dispatching thread until the main thread finishes processing

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_OPENGL_ASYNC_DISPATCH "SDL_MAC_OPENGL_ASYNC_DISPATCH"
```

## Remarks

This variable can be set to the following values:

- "0": Dispatching OpenGL context updates will block the dispatching thread
  until the main thread finishes processing (default).
- "1": Dispatching OpenGL context updates will allow the dispatching thread
  to continue execution.

Generally you want the default, but if you have OpenGL code in a background
thread on a Mac, and the main thread hangs because it's waiting for that
background thread, but that background thread is also hanging because it's
waiting for the main thread to do an update, this might fix your issue.

This hint only applies to macOS.

This hint is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

