###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_powf

Raise `x` to the power `y`

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_powf(float x, float y);
```

## Function Parameters

|       |       |              |
| ----- | ----- | ------------ |
| float | **x** | the base     |
| float | **y** | the exponent |

## Return Value

(float) Returns `x` raised to the power `y`

## Remarks

Domain: `-INF <= x <= INF`, `-INF <= y <= INF`

Range: `-INF <= z <= INF`

If `y` is the base of the natural logarithm (e), consider using
[SDL_exp](SDL_exp) instead.

This function operates on single-precision floating point values, use
[SDL_powf](SDL_powf) for double-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_pow](SDL_pow)
- [SDL_expf](SDL_expf)
- [SDL_logf](SDL_logf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

