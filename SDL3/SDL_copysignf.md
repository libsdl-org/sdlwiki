###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_copysignf

Copy the sign of one floating-point value to another.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_copysignf(float x, float y);
```

## Function Parameters

|       |       |                                              |
| ----- | ----- | -------------------------------------------- |
| float | **x** | floating point value to use as the magnitude |
| float | **y** | floating point value to use as the sign      |

## Return Value

(float) Returns the floating point value with the sign of y and the
magnitude of x

## Remarks

The definition of copysign is that ``copysign(x, y) = abs(x) * sign(y)``.

Domain: `-INF <= x <= INF`, ``-INF <= y <= f``

Range: `-INF <= z <= INF`

This function operates on single-precision floating point values, use
[SDL_copysign](SDL_copysign) for double-precision floats.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_copysignf](SDL_copysignf)
- [SDL_fabsf](SDL_fabsf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

