###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PIXELFLAG

A macro to retrieve the flags of an [SDL_PixelFormat](SDL_PixelFormat).

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_PIXELFLAG(format)    (((format) >> 28) & 0x0F)
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns the flags of `format`.

## Remarks

This macro is generally not needed directly by an app, which should use
specific tests, like [SDL_ISPIXELFORMAT_FOURCC](SDL_ISPIXELFORMAT_FOURCC),
instead.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

