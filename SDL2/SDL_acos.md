###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_acos

Use this function to compute arc cosine of `x`.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
double SDL_acos(double x);
```

## Function Parameters

|        |       |                                   |
| ------ | ----- | --------------------------------- |
| double | **x** | floating point value, in radians. |

## Return Value

(double) Returns arc cosine of `x`.

## Remarks

The definition of `y = acos(x)` is `x = cos(y)`.

Domain: `-1 <= x <= 1`

Range: `0 <= y <= Pi`

## Version

This function is available since SDL 2.0.2.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

