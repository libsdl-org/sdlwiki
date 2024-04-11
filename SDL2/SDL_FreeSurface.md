###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeSurface

Free an RGB surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_FreeSurface(SDL_Surface * surface);

```

## Function Parameters

|                 |                                         |
| --------------- | --------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) to free. |

## Remarks

It is safe to pass NULL to this function.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_CreateRGBSurface](SDL_CreateRGBSurface)
* [SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom)
* [SDL_LoadBMP](SDL_LoadBMP)
* [SDL_LoadBMP_RW](SDL_LoadBMP_RW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

