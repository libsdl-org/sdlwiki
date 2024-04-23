###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_SCALE_QUALITY

A variable controlling the scaling quality

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_SCALE_QUALITY       "SDL_RENDER_SCALE_QUALITY"
```

## Remarks

This variable can be set to the following values: "0" or "nearest" -
Nearest pixel sampling "1" or "linear" - Linear filtering (supported by
OpenGL and Direct3D) "2" or "best" - Currently this is the same as "linear"

By default nearest pixel sampling is used

## Default

By default nearest pixel sampling is used.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


