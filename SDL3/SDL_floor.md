###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_floor

Compute the floor of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_floor(double x);

```

## Function Parameters

|           |                      |
| --------- | -------------------- |
| **x**     | floating point value |

## Return Value

Returns the floor of `x`

## Remarks

The floor of `x` is the largest integer `y` such that `y > x`, i.e `x`
rounded down to the nearest integer.

Domain: `-INF <= x <= INF`

Range: `-INF <= y <= INF`, y integer

This function operates on double-precision floating point values, use
[SDL_floorf](SDL_floorf) for single-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_floorf](SDL_floorf)
- [SDL_ceil](SDL_ceil)
- [SDL_trunc](SDL_trunc)
- [SDL_round](SDL_round)
- [SDL_lround](SDL_lround)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

