###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_RENDER_PS2_DYNAMIC_VSYNC

A variable controlling whether vsync is automatically disabled if doesn't reach enough FPS.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_PS2_DYNAMIC_VSYNC    "SDL_RENDER_PS2_DYNAMIC_VSYNC"
```

## Remarks

The variable can be set to the following values:

- "0": It will be using VSYNC as defined in the main flag. (default)
- "1": If VSYNC was previously enabled, then it will disable VSYNC if
  doesn't reach enough speed

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

