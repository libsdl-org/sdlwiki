###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FLT_EPSILON

Epsilon constant, used for comparing floating-point numbers.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_FLT_EPSILON 1.1920928955078125e-07F /* 0x0.000002p0 */
```

## Remarks

Equals by default to platform-defined `FLT_EPSILON`, or
`1.1920928955078125e-07F` if that's not available.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

