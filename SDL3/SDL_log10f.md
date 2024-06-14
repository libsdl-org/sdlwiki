###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_log10f

Compute the base-10 logarithm of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_log10f(float x);
```

## Function Parameters

|       |       |                                               |
| ----- | ----- | --------------------------------------------- |
| float | **x** | floating point value. Must be greater than 0. |

## Return Value

(float) Returns the logarithm of `x`.

## Remarks

Domain: `0 < x <= INF`

Range: `-INF <= y <= INF`

It is an error for `x` to be less than or equal to 0.

This function operates on single-precision floating point values, use
[SDL_log10](SDL_log10) for double-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_log10](SDL_log10)
- [SDL_logf](SDL_logf)
- [SDL_powf](SDL_powf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

