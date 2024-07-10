###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPixelFormatForMasks

Convert a bpp value and RGBA masks to an enumerated pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
SDL_PixelFormat SDL_GetPixelFormatForMasks(int bpp, Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask);
```

## Function Parameters

|        |           |                                                |
| ------ | --------- | ---------------------------------------------- |
| int    | **bpp**   | a bits per pixel value; usually 15, 16, or 32. |
| Uint32 | **Rmask** | the red mask for the format.                   |
| Uint32 | **Gmask** | the green mask for the format.                 |
| Uint32 | **Bmask** | the blue mask for the format.                  |
| Uint32 | **Amask** | the alpha mask for the format.                 |

## Return Value

([SDL_PixelFormat](SDL_PixelFormat)) Returns the
[SDL_PixelFormat](SDL_PixelFormat) value corresponding to the format masks,
or [SDL_PIXELFORMAT_UNKNOWN](SDL_PIXELFORMAT_UNKNOWN) if there isn't a
match.

## Remarks

This will return [`SDL_PIXELFORMAT_UNKNOWN`](SDL_PIXELFORMAT_UNKNOWN) if
the conversion wasn't possible.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetMasksForPixelFormat](SDL_GetMasksForPixelFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

