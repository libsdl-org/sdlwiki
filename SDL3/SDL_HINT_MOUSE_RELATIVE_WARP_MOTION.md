###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_WARP_MOTION

A variable controlling whether a motion event should be generated for mouse warping in relative mode.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_WARP_MOTION  "SDL_MOUSE_RELATIVE_WARP_MOTION"
```

## Remarks

The variable can be set to the following values:

- "0": Warping the mouse will not generate a motion event in relative mode
- "1": Warping the mouse will generate a motion event in relative mode

By default warping the mouse will not generate motion events in relative
mode. This avoids the application having to filter out large relative
motion due to warping.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

