# SDL_sinf

Compute the sine of `x`.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_sinf(float x);
```

## Function Parameters

|       |       |                                   |
| ----- | ----- | --------------------------------- |
| float | **x** | floating point value, in radians. |

## Return Value

(float) Returns sine of `x`.

## Remarks

Domain: `-INF <= x <= INF`

Range: `-1 <= y <= 1`

This function operates on single-precision floating point values, use
[SDL_sin](SDL_sin) for double-precision floats.

This function may use a different approximation across different versions,
platforms and configurations. i.e, it can return a different value given
the same input on different machines or operating systems, or if SDL is
updated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_sin](SDL_sin)
- [SDL_asinf](SDL_asinf)
- [SDL_cosf](SDL_cosf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

