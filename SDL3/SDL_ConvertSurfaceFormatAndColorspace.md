###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertSurfaceFormatAndColorspace

Copy an existing surface to a new surface of the specified format and colorspace.

## Syntax

```c
SDL_Surface* SDL_ConvertSurfaceFormatAndColorspace(SDL_Surface *surface, Uint32 pixel_format, SDL_Colorspace colorspace);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **surface**          | the existing [SDL_Surface](SDL_Surface) structure to convert |
| **pixel_format**     | the new pixel format                                         |
| **colorspace**       | the new colorspace                                           |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function converts an existing surface to a new format and colorspace
and returns the new surface. This will perform any pixel format and
colorspace conversion needed.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePixelFormat](SDL_CreatePixelFormat)
* [SDL_ConvertSurface](SDL_ConvertSurface)
* [SDL_CreateSurface](SDL_CreateSurface)

----
[CategoryAPI](CategoryAPI)

