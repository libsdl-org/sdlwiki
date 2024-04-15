###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_fabs

Compute the absolute value of `x`

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
double SDL_fabs(double x);

```

## Function Parameters

|           |                                              |
| --------- | -------------------------------------------- |
| **x**     | floating point value to use as the magnitude |

## Return Value

Returns the absolute value of `x`

## Remarks

Domain: `-INF <= x <= INF`

Range: `0 <= y <= INF`

This function operates on double-precision floating point values, use
[SDL_copysignf](SDL_copysignf) for single-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_fabsf](SDL_fabsf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

