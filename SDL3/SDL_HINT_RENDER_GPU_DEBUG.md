# SDL_HINT_RENDER_GPU_DEBUG

A variable controlling whether to create the GPU device in debug mode.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_GPU_DEBUG "SDL_RENDER_GPU_DEBUG"
```

## Remarks

This variable can be set to the following values:

- "0": Disable debug mode use (default)
- "1": Enable debug mode use

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

