###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SoftStretchLinear

Perform bilinear scaling between two surfaces of the same format, 32BPP.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SoftStretchLinear(SDL_Surface * src,
                    const SDL_Rect * srcrect,
                    SDL_Surface * dst,
                    const SDL_Rect * dstrect);

```

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

