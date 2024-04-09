###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_modff

Split `x` into integer and fractional parts

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
float SDL_modff(float x, float *y);

```

## Function Parameters

|           |                                                 |
| --------- | ----------------------------------------------- |
| **x**     | floating point value                            |
| **y**     | output pointer to store the integer part of `x` |

## Return Value

Returns the fractional part of `x`

## Remarks

This function operates on single-precision floating point values, use
[SDL_modf](SDL_modf) for double-precision floats.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_modf](SDL_modf)
* [SDL_truncf](SDL_truncf)
* [SDL_fmodf](SDL_fmodf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

