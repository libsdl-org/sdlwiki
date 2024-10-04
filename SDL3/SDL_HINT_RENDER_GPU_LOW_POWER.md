###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_RENDER_GPU_LOW_POWER

A variable controlling whether to prefer a low-power GPU on multi-GPU systems.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_GPU_LOW_POWER "SDL_RENDER_GPU_LOW_POWER"
```

## Remarks

This variable can be set to the following values:

- "0": Prefer high-performance GPU (default)
- "1": Prefer low-power GPU

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

