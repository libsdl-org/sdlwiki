###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ISPIXELFORMAT_FLOAT

A macro to determine if an [SDL_PixelFormat](SDL_PixelFormat) is a floating point format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_ISPIXELFORMAT_FLOAT(format)    \
      (!SDL_ISPIXELFORMAT_FOURCC(format) && \
       ((SDL_PIXELTYPE(format) == SDL_PIXELTYPE_ARRAYF16) || \
        (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_ARRAYF32)))
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns true if the format is 10-bit, false otherwise.

## Remarks

Note that this macro double-evaluates its parameter, so do not use
expressions with side-effects here.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

