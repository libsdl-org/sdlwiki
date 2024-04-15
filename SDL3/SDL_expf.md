###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_expf

Compute the exponential of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
float SDL_expf(float x);

```

## Function Parameters

|           |                      |
| --------- | -------------------- |
| **x**     | floating point value |

## Return Value

Returns value of `e^x`

## Remarks

The definition of `y = exp(x)` is `y = e^x`, where `e` is the base of the
natural logarithm. The inverse is the natural logarithm,
[SDL_logf](SDL_logf).

Domain: `-INF <= x <= INF`

Range: `0 <= y <= INF`

The output will overflow if `exp(x)` is too large to be represented.

This function operates on single-precision floating point values, use
[SDL_exp](SDL_exp) for double-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_exp](SDL_exp)
* [SDL_logf](SDL_logf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

