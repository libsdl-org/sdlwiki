###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_floorf

Compute the floor of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
float SDL_floorf(float x);

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

This function operates on single-precision floating point values, use
[SDL_floorf](SDL_floorf) for double-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_floor](SDL_floor)
* [SDL_ceilf](SDL_ceilf)
* [SDL_truncf](SDL_truncf)
* [SDL_roundf](SDL_roundf)
* [SDL_lroundf](SDL_lroundf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

