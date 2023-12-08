###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_acos

Use this function to compute arc cosine of `x`.

## Syntax

```c
double SDL_acos(double x);

```

## Function Parameters

|           |                                   |
| --------- | --------------------------------- |
| **x**     | floating point value, in radians. |

## Return Value

Returns arc cosine of `x`.

## Remarks

The definition of `y = acos(x)` is `x = cos(y)`.

Domain: `-1 <= x <= 1`

Range: `0 <= y <= Pi`

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
/* acos(x) = Pi/2 - asin(x) */
SDL_Log("acos(0):\t\t%f", SDL_acos(0));
SDL_Log("Pi/2 - asin(0):\t%f", M_PI / 2 - SDL_asin(0));

/* acos(-x) = Pi  - acos(x) */
SDL_Log("acos(-(-1)):\t%f", SDL_acos(-(-1)));
SDL_Log("Pi - acos(-1):\t%f", M_PI - SDL_acos(-1));
```

----
[CategoryAPI](CategoryAPI.md), [CategoryStandard](CategoryStandard.md), [CategoryDraft](CategoryDraft.md)
