###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ceilf

Compute the ceiling of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_ceilf(float x);

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

This function operates on single-precision floating point values, use
[SDL_ceil](SDL_ceil) for double-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ceil](SDL_ceil)
- [SDL_floorf](SDL_floorf)
- [SDL_truncf](SDL_truncf)
- [SDL_roundf](SDL_roundf)
- [SDL_lroundf](SDL_lroundf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

