###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ceil

Compute the ceiling of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_ceil(double x);

```

## Function Parameters

|           |                      |
| --------- | -------------------- |
| **x**     | floating point value |

## Return Value

Returns the ceiling of `x`

## Remarks

The ceiling of `x` is the smallest integer `y` such that `y > x`, i.e `x`
rounded up to the nearest integer.

Domain: `-INF <= x <= INF`

Range: `-INF <= y <= INF`, y integer

This function operates on double-precision floating point values, use
[SDL_ceilf](SDL_ceilf) for single-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ceilf](SDL_ceilf)
- [SDL_floor](SDL_floor)
- [SDL_trunc](SDL_trunc)
- [SDL_round](SDL_round)
- [SDL_lround](SDL_lround)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

