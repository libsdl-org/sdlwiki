###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_VSYNC

A variable controlling whether updates to the SDL screen surface should be synchronized with the vertical refresh, to avoid tearing.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_VSYNC               "SDL_RENDER_VSYNC"
```

## Remarks

This variable can be set to the following values:

- "0": Disable vsync
- "1": Enable vsync

By default SDL does not sync screen surface updates with vertical refresh.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

