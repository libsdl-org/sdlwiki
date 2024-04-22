###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_pow

Raise `x` to the power `y`

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_pow(double x, double y);

```

## Function Parameters

|           |              |
| --------- | ------------ |
| **x**     | the base     |
| **y**     | the exponent |

## Return Value

Returns `x` raised to the power `y`

## Remarks

Domain: `-INF <= x <= INF`, `-INF <= y <= INF`

Range: `-INF <= z <= INF`

If `y` is the base of the natural logarithm (e), consider using
[SDL_exp](SDL_exp) instead.

This function operates on double-precision floating point values, use
[SDL_powf](SDL_powf) for single-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_powf](SDL_powf)
* [SDL_exp](SDL_exp)
* [SDL_log](SDL_log)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

