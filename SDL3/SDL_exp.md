# SDL_exp

Compute the exponential of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_exp(double x);
```

## Function Parameters

|        |       |                       |
| ------ | ----- | --------------------- |
| double | **x** | floating point value. |

## Return Value

(double) Returns value of `e^x`.

## Remarks

The definition of `y = exp(x)` is `y = e^x`, where `e` is the base of the
natural logarithm. The inverse is the natural logarithm,
[SDL_log](SDL_log).

Domain: `-INF <= x <= INF`

Range: `0 <= y <= INF`

The output will overflow if `exp(x)` is too large to be represented.

This function operates on double-precision floating point values, use
[SDL_expf](SDL_expf) for single-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_expf](SDL_expf)
- [SDL_log](SDL_log)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

