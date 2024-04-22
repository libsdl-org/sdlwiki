###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_asinf

Compute the arc sine of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_asinf(float x);

```

## Function Parameters

|           |                       |
| --------- | --------------------- |
| **x**     | floating point value. |

## Return Value

Returns arc sine of `x`, in radians.

## Remarks

The definition of `y = asin(x)` is `x = sin(y)`.

Domain: `-1 <= x <= 1`

Range: `-Pi/2 <= y <= Pi/2`

This function operates on single-precision floating point values, use
[SDL_asin](SDL_asin) for double-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_asin](SDL_asin)
* [SDL_acosf](SDL_acosf)
* [SDL_sinf](SDL_sinf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

