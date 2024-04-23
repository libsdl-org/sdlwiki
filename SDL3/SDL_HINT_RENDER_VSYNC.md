###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_RENDER_VSYNC

A variable controlling whether updates to the SDL screen surface should be synchronized with the vertical refresh, to avoid tearing.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_VSYNC               "SDL_RENDER_VSYNC"
```

## Remarks

This hint overrides the application preference when creating a renderer.

The variable can be set to the following values:

- "0": Disable vsync. (default)
- "1": Enable vsync.

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]]


