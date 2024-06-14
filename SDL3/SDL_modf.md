###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_modf

Split `x` into integer and fractional parts

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_modf(double x, double *y);
```

## Function Parameters

|          |       |                                                  |
| -------- | ----- | ------------------------------------------------ |
| double   | **x** | floating point value.                            |
| double * | **y** | output pointer to store the integer part of `x`. |

## Return Value

(double) Returns the fractional part of `x`.

## Remarks

This function operates on double-precision floating point values, use
[SDL_modff](SDL_modff) for single-precision floats.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_modff](SDL_modff)
- [SDL_trunc](SDL_trunc)
- [SDL_fmod](SDL_fmod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

