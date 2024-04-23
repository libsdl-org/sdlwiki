###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_EXTERNAL_CONTEXT

A variable controlling whether the graphics context is externally managed.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_EXTERNAL_CONTEXT    "SDL_VIDEO_EXTERNAL_CONTEXT"
```

## Remarks

This variable can be set to the following values:

- "0": SDL will manage graphics contexts that are attached to windows.
- "1": Disable graphics context management on windows.

By default SDL will manage OpenGL contexts in certain situations. For
example, on Android the context will be automatically saved and restored
when pausing the application. Additionally, some platforms will assume
usage of OpenGL if Vulkan isn't used. Setting this to "1" will prevent this
behavior, which is desireable when the application manages the graphics
context, such as an externally managed OpenGL context or attaching a Vulkan
surface to the window.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

