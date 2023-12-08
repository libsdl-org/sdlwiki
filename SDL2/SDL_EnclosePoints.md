###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_EnclosePoints

Calculate a minimal rectangle enclosing a set of points.

## Syntax

```c
SDL_bool SDL_EnclosePoints(const SDL_Point * points,
                           int count,
                           const SDL_Rect * clip,
                           SDL_Rect * result);

```

## Function Parameters

|                |                                                                                  |
| -------------- | -------------------------------------------------------------------------------- |
| **points**     | an array of [SDL_Point](SDL_Point.md) structures representing points to be enclosed |
| **count**      | the number of structures in the `points` array                                   |
| **clip**       | an [SDL_Rect](SDL_Rect.md) used for clipping or NULL to enclose all points          |
| **result**     | an [SDL_Rect](SDL_Rect.md) structure filled in with the minimal enclosing rectangle |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if any points were enclosed or
[SDL_FALSE](SDL_FALSE.md) if all the points were outside of the clipping
rectangle.

## Remarks

If `clip` is not NULL then only points inside of the clipping rectangle are
considered.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
