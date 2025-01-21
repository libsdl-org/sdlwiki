###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PIXELORDER

A macro to retrieve the order of an [SDL_PixelFormat](SDL_PixelFormat).

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_PIXELORDER(format)   (((format) >> 20) & 0x0F)
```

## Macro Parameters

|            |                                                 |
| ---------- | ----------------------------------------------- |
| **format** | an [SDL_PixelFormat](SDL_PixelFormat) to check. |

## Return Value

Returns the order of `format`.

## Remarks

This is usually a value from the [SDL_BitmapOrder](SDL_BitmapOrder),
[SDL_PackedOrder](SDL_PackedOrder), or [SDL_ArrayOrder](SDL_ArrayOrder)
enumerations, depending on the format type.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

