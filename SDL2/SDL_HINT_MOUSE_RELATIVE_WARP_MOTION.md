###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_RELATIVE_WARP_MOTION

A variable controlling whether a motion event should be generated for mouse warping in relative mode.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_WARP_MOTION  "SDL_MOUSE_RELATIVE_WARP_MOTION"
```

## Remarks

This variable can be set to the following values: "0" - Warping the mouse
will not generate a motion event in relative mode "1" - Warping the mouse
will generate a motion event in relative mode

By default warping the mouse will not generate motion events in relative
mode. This avoids the application having to filter out large relative
motion due to warping.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

