# SDL_ISCOLORSPACE_LIMITED_RANGE

A macro to determine if an [SDL_Colorspace](SDL_Colorspace) has a limited range.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_ISCOLORSPACE_LIMITED_RANGE(cspace)       (SDL_COLORSPACERANGE(cspace) != SDL_COLOR_RANGE_FULL)
```

## Macro Parameters

|            |                                               |
| ---------- | --------------------------------------------- |
| **cspace** | an [SDL_Colorspace](SDL_Colorspace) to check. |

## Return Value

Returns true if limited range, false otherwise.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

