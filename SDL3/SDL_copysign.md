###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_copysign

Copy the sign of one floating-point value to another.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_copysign(double x, double y);

```

## Function Parameters

|           |                                              |
| --------- | -------------------------------------------- |
| **x**     | floating point value to use as the magnitude |
| **y**     | floating point value to use as the sign      |

## Return Value

Returns the floating point value with the sign of y and the magnitude of x

## Remarks

The definition of copysign is that ``copysign(x, y) = abs(x) * sign(y)``.

Domain: `-INF <= x <= INF`, ``-INF <= y <= f``

Range: `-INF <= z <= INF`

This function operates on double-precision floating point values, use
[SDL_copysignf](SDL_copysignf) for single-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_copysignf](SDL_copysignf)
* [SDL_fabs](SDL_fabs)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

