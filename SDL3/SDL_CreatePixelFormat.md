###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePixelFormat

Create an [SDL_PixelFormat](SDL_PixelFormat) structure corresponding to a pixel format.

## Syntax

```c
SDL_PixelFormat * SDL_CreatePixelFormat(Uint32 pixel_format);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **pixel_format**     | one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values |

## Return Value

Returns the new [SDL_PixelFormat](SDL_PixelFormat) structure or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Returned structure may come from a shared global cache (i.e. not newly
allocated), and hence should not be modified, especially the palette. Weird
errors such as `Blit combination not supported` may occur.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DestroyPixelFormat](SDL_DestroyPixelFormat)

----
[CategoryAPI](CategoryAPI)

