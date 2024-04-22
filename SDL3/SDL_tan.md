###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_tan

Compute the tangent of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_tan(double x);

```

## Function Parameters

|           |                                  |
| --------- | -------------------------------- |
| **x**     | floating point value, in radians |

## Return Value

Returns tangent of `x`

## Remarks

Domain: `-INF <= x <= INF`

Range: `-INF <= y <= INF`

This function operates on double-precision floating point values, use
[SDL_tanf](SDL_tanf) for single-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_tanf](SDL_tanf)
* [SDL_sin](SDL_sin)
* [SDL_cos](SDL_cos)
* [SDL_atan](SDL_atan)
* [SDL_atan2](SDL_atan2)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

