# SDL_COLORSPACEPRIMARIES

A macro to retrieve the primaries of an [SDL_Colorspace](SDL_Colorspace).

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_COLORSPACEPRIMARIES(cspace)  (SDL_ColorPrimaries)(((cspace) >> 10) & 0x1F)
```

## Macro Parameters

|            |                                               |
| ---------- | --------------------------------------------- |
| **cspace** | an [SDL_Colorspace](SDL_Colorspace) to check. |

## Return Value

Returns the [SDL_ColorPrimaries](SDL_ColorPrimaries) of `cspace`.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

