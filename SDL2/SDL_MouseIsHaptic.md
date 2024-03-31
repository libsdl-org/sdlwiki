###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MouseIsHaptic

Query whether or not the current mouse has haptic capabilities.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_MouseIsHaptic(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the mouse is haptic or
[SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpenFromMouse](SDL_HapticOpenFromMouse)

----
[CategoryAPI](CategoryAPI)

