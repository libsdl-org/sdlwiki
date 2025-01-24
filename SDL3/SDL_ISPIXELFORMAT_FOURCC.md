# SDL_ISPIXELFORMAT_FOURCC

A macro to determine if an [SDL_PixelFormat](SDL_PixelFormat) is a "FourCC" format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_ISPIXELFORMAT_FOURCC(format)  /* The flag is set to 1 because 0x1? is not in the printable ASCII range */ \
    ((format) && (SDL_PIXELFLAG(format) != 1))
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns true if the format has alpha, false otherwise.

## Remarks

This covers custom and other unusual formats.

Note that this macro double-evaluates its parameter, so do not use
expressions with side-effects here.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

