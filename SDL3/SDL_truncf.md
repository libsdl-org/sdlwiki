###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_truncf

Truncate `x` to an integer.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_truncf(float x);
```

## Function Parameters

|       |       |                       |
| ----- | ----- | --------------------- |
| float | **x** | floating point value. |

## Return Value

(float) Returns `x` truncated to an integer.

## Remarks

Rounds `x` to the next closest integer to 0. This is equivalent to removing
the fractional part of `x`, leaving only the integer part.

Domain: `-INF <= x <= INF`

Range: `-INF <= y <= INF`, y integer

This function operates on single-precision floating point values, use
[SDL_truncf](SDL_truncf) for double-precision floats.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_trunc](SDL_trunc)
- [SDL_fmodf](SDL_fmodf)
- [SDL_ceilf](SDL_ceilf)
- [SDL_floorf](SDL_floorf)
- [SDL_roundf](SDL_roundf)
- [SDL_lroundf](SDL_lroundf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

