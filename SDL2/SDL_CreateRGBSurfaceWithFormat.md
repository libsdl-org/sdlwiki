###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateRGBSurfaceWithFormat

Allocate a new RGB surface with a specific pixel format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Surface* SDL_CreateRGBSurfaceWithFormat
    (Uint32 flags, int width, int height, int depth, Uint32 format);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **flags**      | the flags are unused and should be set to 0                                        |
| **width**      | the width of the surface                                                           |
| **height**     | the height of the surface                                                          |
| **depth**      | the depth of the surface in bits                                                   |
| **format**     | the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) for the new surface's pixel format. |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function operates mostly like
[SDL_CreateRGBSurface](SDL_CreateRGBSurface)(), except instead of providing
pixel color masks, you provide it with a predefined format from
[SDL_PixelFormatEnum](SDL_PixelFormatEnum).

## Version

This function is available since SDL 2.0.5.

## See Also

* [SDL_CreateRGBSurface](SDL_CreateRGBSurface)
* [SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom)
* [SDL_FreeSurface](SDL_FreeSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

