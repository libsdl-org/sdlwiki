###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertSurfaceFormat

Copy an existing surface to a new surface of the specified format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface* SDL_ConvertSurfaceFormat(SDL_Surface *surface, SDL_PixelFormatEnum pixel_format);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **surface**          | the existing [SDL_Surface](SDL_Surface) structure to convert |
| **pixel_format**     | the new pixel format                                         |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function operates just like
[SDL_ConvertSurface](SDL_ConvertSurface)(), but accepts an
[SDL_PixelFormatEnum](SDL_PixelFormatEnum) value instead of an
[SDL_PixelFormat](SDL_PixelFormat) structure. As such, it might be easier
to call but it doesn't have access to palette information for the
destination surface, in case that would be important.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_ConvertSurface](SDL_ConvertSurface)
* [SDL_ConvertSurfaceFormatAndColorspace](SDL_ConvertSurfaceFormatAndColorspace)
* [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)


