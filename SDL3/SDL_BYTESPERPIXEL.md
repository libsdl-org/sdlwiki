###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BYTESPERPIXEL

A macro to determine an [SDL_PixelFormat](SDL_PixelFormat)'s bytes per pixel.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_BYTESPERPIXEL(format) \
    (SDL_ISPIXELFORMAT_FOURCC(format) ? \
        ((((format) == SDL_PIXELFORMAT_YUY2) || \
          ((format) == SDL_PIXELFORMAT_UYVY) || \
          ((format) == SDL_PIXELFORMAT_YVYU) || \
          ((format) == SDL_PIXELFORMAT_P010)) ? 2 : 1) : (((format) >> 0) & 0xFF))
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns the bytes-per-pixel of `format`.

## Remarks

Note that this macro double-evaluates its parameter, so do not use
expressions with side-effects here.

FourCC formats do their best here, but many of them don't have a meaningful
measurement of bytes per pixel.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

## See Also

- [SDL_BITSPERPIXEL](SDL_BITSPERPIXEL)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

