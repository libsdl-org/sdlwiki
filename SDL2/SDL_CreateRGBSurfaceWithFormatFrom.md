###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateRGBSurfaceWithFormatFrom

Allocate a new RGB surface with with a specific pixel format and existing pixel data.

## Syntax

```c
SDL_Surface* SDL_CreateRGBSurfaceWithFormatFrom
    (void *pixels, int width, int height, int depth, int pitch, Uint32 format);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **pixels**     | a pointer to existing pixel data                                                   |
| **width**      | the width of the surface                                                           |
| **height**     | the height of the surface                                                          |
| **depth**      | the depth of the surface in bits                                                   |
| **pitch**      | the pitch of the surface in bytes                                                  |
| **format**     | the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) for the new surface's pixel format. |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function operates mostly like
[SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom)(), except instead of
providing pixel color masks, you provide it with a predefined format from
[SDL_PixelFormatEnum](SDL_PixelFormatEnum).

No copy is made of the pixel data. Pixel data is not managed automatically;
you must free the surface before you free the pixel data.

## Version

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom)
* [SDL_CreateRGBSurfaceWithFormat](SDL_CreateRGBSurfaceWithFormat)
* [SDL_FreeSurface](SDL_FreeSurface)

----
[CategoryAPI](CategoryAPI)

