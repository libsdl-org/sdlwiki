###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertSurfaceFormat

Copy an existing surface to a new surface of the specified format enum.

## Syntax

```c
SDL_Surface* SDL_ConvertSurfaceFormat(SDL_Surface *surface,
                                      Uint32 pixel_format);

```

## Function Parameters

|                      |                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------ |
| **surface**          | the existing [SDL_Surface](SDL_Surface) structure to convert                         |
| **pixel_format**     | the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) that the new surface is optimized for |

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

## Related Functions

* [SDL_CreatePixelFormat](SDL_CreatePixelFormat)
* [SDL_ConvertSurface](SDL_ConvertSurface)
* [SDL_CreateSurface](SDL_CreateSurface)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


