# SDL_fmodf

Return the floating-point remainder of `x / y`

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_fmodf(float x, float y);
```

## Function Parameters

|       |       |                                 |
| ----- | ----- | ------------------------------- |
| float | **x** | the numerator.                  |
| float | **y** | the denominator. Must not be 0. |

## Return Value

(float) Returns the remainder of `x / y`.

## Remarks

Divides `x` by `y`, and returns the remainder.

Domain: `-INF <= x <= INF`, `-INF <= y <= INF`, `y != 0`

Range: `-y <= z <= y`

This function operates on single-precision floating point values, use
[SDL_fmod](SDL_fmod) for double-precision floats.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_fmod](SDL_fmod)
- [SDL_truncf](SDL_truncf)
- [SDL_modff](SDL_modff)
- [SDL_ceilf](SDL_ceilf)
- [SDL_floorf](SDL_floorf)
- [SDL_roundf](SDL_roundf)
- [SDL_lroundf](SDL_lroundf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

