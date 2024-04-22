###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_sin

Compute the sine of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_sin(double x);

```

## Function Parameters

|           |                                  |
| --------- | -------------------------------- |
| **x**     | floating point value, in radians |

## Return Value

Returns sine of `x`

## Remarks

Domain: `-INF <= x <= INF`

Range: `-1 <= y <= 1`

This function operates on double-precision floating point values, use
[SDL_sinf](SDL_sinf) for single-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_sinf](SDL_sinf)
* [SDL_asin](SDL_asin)
* [SDL_cos](SDL_cos)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

