# SDL_ISCOLORSPACE_MATRIX_BT2020_NCL

A macro to determine if an [SDL_Colorspace](SDL_Colorspace) uses BT2020_NCL matrix coefficients.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_ISCOLORSPACE_MATRIX_BT2020_NCL(cspace)   (SDL_COLORSPACEMATRIX(cspace) == SDL_MATRIX_COEFFICIENTS_BT2020_NCL)
```

## Macro Parameters

|            |                                               |
| ---------- | --------------------------------------------- |
| **cspace** | an [SDL_Colorspace](SDL_Colorspace) to check. |

## Return Value

Returns true if BT2020_NCL, false otherwise.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

