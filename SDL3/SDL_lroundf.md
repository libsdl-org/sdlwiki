# SDL_lroundf

Round `x` to the nearest integer representable as a long

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
long SDL_lroundf(float x);
```

## Function Parameters

|       |       |                       |
| ----- | ----- | --------------------- |
| float | **x** | floating point value. |

## Return Value

(long) Returns the nearest integer to `x`.

## Remarks

Rounds `x` to the nearest integer. Values halfway between integers will be
rounded away from zero.

Domain: `-INF <= x <= INF`

Range: `MIN_LONG <= y <= MAX_LONG`

This function operates on single-precision floating point values, use
[SDL_lround](SDL_lround) for double-precision floats. To get the result as
a floating-point type, use [SDL_roundf](SDL_roundf).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_lround](SDL_lround)
- [SDL_roundf](SDL_roundf)
- [SDL_floorf](SDL_floorf)
- [SDL_ceilf](SDL_ceilf)
- [SDL_truncf](SDL_truncf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

