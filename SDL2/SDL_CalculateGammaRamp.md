###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CalculateGammaRamp

Calculate a 256 entry gamma ramp for a gamma value.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_CalculateGammaRamp(float gamma, Uint16 * ramp);

```

## Function Parameters

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| **gamma**     | a gamma value where 0.0 is black and 1.0 is identity |
| **ramp**      | an array of 256 values filled in with the gamma ramp |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetWindowGammaRamp](SDL_SetWindowGammaRamp)

----
[CategoryAPI](CategoryAPI)

