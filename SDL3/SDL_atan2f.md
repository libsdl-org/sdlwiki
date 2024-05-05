###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_atan2f

Compute the arc tangent of `y / x`, using the signs of x and y to adjust the result's quadrant.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_atan2f(float y, float x);

```

## Function Parameters

|           |                                                         |
| --------- | ------------------------------------------------------- |
| **x**     | floating point value of the denominator (x coordinate). |
| **y**     | floating point value of the numerator (y coordinate)    |

## Return Value

Returns arc tangent of of `y / x` in radians, or, if `x = 0`, either
`-Pi/2`, `0`, or `Pi/2`, depending on the value of `y`.

## Remarks

The definition of `z = atan2(x, y)` is `y = x tan(z)`, where the quadrant
of z is determined based on the signs of x and y.

Domain: `-INF <= x <= INF`, `-INF <= y <= INF`

Range: `-Pi/2 <= y <= Pi/2`

This function operates on single-precision floating point values, use
[SDL_atan2](SDL_atan2) for double-precision floats.

To calculate the arc tangent of a single value, use [SDL_atanf](SDL_atanf).

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_atan2f](SDL_atan2f)
- [SDL_atan](SDL_atan)
- [SDL_tan](SDL_tan)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

