###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateRGBSurfaceFrom

Allocate a new RGB surface with existing pixel data.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Surface* SDL_CreateRGBSurfaceFrom(void *pixels,
                                      int width,
                                      int height,
                                      int depth,
                                      int pitch,
                                      Uint32 Rmask,
                                      Uint32 Gmask,
                                      Uint32 Bmask,
                                      Uint32 Amask);

```

## Function Parameters

|                |                                   |
| -------------- | --------------------------------- |
| **pixels**     | a pointer to existing pixel data  |
| **width**      | the width of the surface          |
| **height**     | the height of the surface         |
| **depth**      | the depth of the surface in bits  |
| **pitch**      | the pitch of the surface in bytes |
| **Rmask**      | the red mask for the pixels       |
| **Gmask**      | the green mask for the pixels     |
| **Bmask**      | the blue mask for the pixels      |
| **Amask**      | the alpha mask for the pixels     |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function operates mostly like
[SDL_CreateRGBSurface](SDL_CreateRGBSurface)(), except it does not allocate
memory for the pixel data, instead the caller provides an existing buffer
of data for the surface to use.

No copy is made of the pixel data. Pixel data is not managed automatically;
you must free the surface before you free the pixel data.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_CreateRGBSurface](SDL_CreateRGBSurface)
* [SDL_CreateRGBSurfaceWithFormat](SDL_CreateRGBSurfaceWithFormat)
* [SDL_FreeSurface](SDL_FreeSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

