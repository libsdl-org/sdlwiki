# SDL_BITSPERPIXEL

A macro to determine an [SDL_PixelFormat](SDL_PixelFormat)'s bits per pixel.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_BITSPERPIXEL(format) \
    (SDL_ISPIXELFORMAT_FOURCC(format) ? 0 : (((format) >> 8) & 0xFF))
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns the bits-per-pixel of `format`.

## Remarks

Note that this macro double-evaluates its parameter, so do not use
expressions with side-effects here.

FourCC formats will report zero here, as it rarely makes sense to measure
them per-pixel.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_BYTESPERPIXEL](SDL_BYTESPERPIXEL)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

