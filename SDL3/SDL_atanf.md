###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_atanf

Compute the arc tangent of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_atanf(float x);

```

## Function Parameters

|           |                       |
| --------- | --------------------- |
| **x**     | floating point value. |

## Return Value

Returns arc tangent of of `x` in radians, or 0 if `x = 0`

## Remarks

The definition of `y = atan(x)` is `x = tan(y)`.

Domain: `-INF <= x <= INF`

Range: `-Pi/2 <= y <= Pi/2`

This function operates on single-precision floating point values, use
[SDL_atan](SDL_atan) for dboule-precision floats.

To calculate the arc tangent of y / x, use [SDL_atan2f](SDL_atan2f).

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_atan](SDL_atan)
- [SDL_atan2f](SDL_atan2f)
- [SDL_tanf](SDL_tanf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

