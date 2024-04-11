###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRelativeMouseState

Retrieve the relative state of the mouse.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Uint32 SDL_GetRelativeMouseState(int *x, int *y);

```

## Function Parameters

|           |                                                                   |
| --------- | ----------------------------------------------------------------- |
| **x**     | a pointer filled with the last recorded x coordinate of the mouse |
| **y**     | a pointer filled with the last recorded y coordinate of the mouse |

## Return Value

Returns a 32-bit button bitmask of the relative button state.

## Remarks

The current button state is returned as a button bitmask, which can be
tested using the `SDL_BUTTON(X)` macros (where `X` is generally 1 for the
left, 2 for middle, 3 for the right button), and `x` and `y` are set to the
mouse deltas since the last call to
[SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)() or since event
initialization. You can pass NULL for either `x` or `y`.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetMouseState](SDL_GetMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

