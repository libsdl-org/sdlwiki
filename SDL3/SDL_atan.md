###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_atan

Compute the arc tangent of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_atan(double x);
```

## Function Parameters

|        |       |                       |
| ------ | ----- | --------------------- |
| double | **x** | floating point value. |

## Return Value

(double) Returns arc tangent of of `x` in radians, or 0 if `x = 0`.

## Remarks

The definition of `y = atan(x)` is `x = tan(y)`.

Domain: `-INF <= x <= INF`

Range: `-Pi/2 <= y <= Pi/2`

This function operates on double-precision floating point values, use
[SDL_atanf](SDL_atanf) for single-precision floats.

To calculate the arc tangent of y / x, use [SDL_atan2](SDL_atan2).

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_atanf](SDL_atanf)
- [SDL_atan2](SDL_atan2)
- [SDL_tan](SDL_tan)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

