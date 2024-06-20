###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_RELATIVE_CURSOR_VISIBLE

A variable controlling whether the hardware cursor stays visible when relative mode is active.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

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

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

