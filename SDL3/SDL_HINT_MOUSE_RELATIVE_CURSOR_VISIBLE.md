###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_CURSOR_VISIBLE

A variable controlling whether the hardware cursor stays visible when relative mode is active.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_CURSOR_VISIBLE  "SDL_MOUSE_RELATIVE_CURSOR_VISIBLE"
```

## Remarks

This variable can be set to the following values: "0" - The cursor will be
hidden while relative mode is active (default) "1" - The cursor will remain
visible while relative mode is active

Note that for systems without raw hardware inputs, relative mode is
implemented using warping, so the hardware cursor will visibly warp between
frames if this is enabled on those systems.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

