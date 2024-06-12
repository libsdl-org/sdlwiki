###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePixelFormat

Create an [SDL_PixelFormat](SDL_PixelFormat) structure corresponding to a pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
SDL_PixelFormat * SDL_CreatePixelFormat(SDL_PixelFormatEnum pixel_format);
```

## Function Parameters

|                                            |                  |                                                              |
| ------------------------------------------ | ---------------- | ------------------------------------------------------------ |
| [SDL_PixelFormatEnum](SDL_PixelFormatEnum) | **pixel_format** | one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values |

## Return Value

([SDL_PixelFormat](SDL_PixelFormat) *) Returns the new
[SDL_PixelFormat](SDL_PixelFormat) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Returned structure may come from a shared global cache (i.e. not newly
allocated), and hence should not be modified, especially the palette. Weird
errors such as `Blit combination not supported` may occur.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DestroyPixelFormat](SDL_DestroyPixelFormat)
- [SDL_SetPixelFormatPalette](SDL_SetPixelFormatPalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

