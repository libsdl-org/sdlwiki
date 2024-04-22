###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_fmod

Return the floating-point remainder of `x / y`

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_fmod(double x, double y);

```

## Function Parameters

|           |                                 |
| --------- | ------------------------------- |
| **x**     | the numerator                   |
| **y**     | the denominator. Must not be 0. |

## Return Value

Returns the remainder of `x / y`

## Remarks

Divides `x` by `y`, and returns the remainder.

Domain: `-INF <= x <= INF`, `-INF <= y <= INF`, `y != 0`

Range: `-y <= z <= y`

This function operates on double-precision floating point values, use
[SDL_fmodf](SDL_fmodf) for single-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_fmodf](SDL_fmodf)
* [SDL_modf](SDL_modf)
* [SDL_trunc](SDL_trunc)
* [SDL_ceil](SDL_ceil)
* [SDL_floor](SDL_floor)
* [SDL_round](SDL_round)
* [SDL_lround](SDL_lround)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

