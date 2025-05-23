# SDL_lround

Round `x` to the nearest integer representable as a long

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
long SDL_lround(double x);
```

## Function Parameters

|        |       |                       |
| ------ | ----- | --------------------- |
| double | **x** | floating point value. |

## Return Value

(long) Returns the nearest integer to `x`.

## Remarks

Rounds `x` to the nearest integer. Values halfway between integers will be
rounded away from zero.

Domain: `-INF <= x <= INF`

Range: `MIN_LONG <= y <= MAX_LONG`

This function operates on double-precision floating point values, use
[SDL_lroundf](SDL_lroundf) for single-precision floats. To get the result
as a floating-point type, use [SDL_round](SDL_round).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_lroundf](SDL_lroundf)
- [SDL_round](SDL_round)
- [SDL_floor](SDL_floor)
- [SDL_ceil](SDL_ceil)
- [SDL_trunc](SDL_trunc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

