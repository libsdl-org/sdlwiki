###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectEnclosingPointsFloat

Calculate a minimal rectangle enclosing a set of points with float precision.

## Syntax

```c
SDL_bool SDL_GetRectEnclosingPointsFloat(const SDL_FPoint * points,
                            int count,
                            const SDL_FRect * clip,
                            SDL_FRect * result);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **points**     | an array of [SDL_FPoint](SDL_FPoint) structures representing points to be enclosed |
| **count**      | the number of structures in the `points` array                                     |
| **clip**       | an [SDL_FRect](SDL_FRect) used for clipping or NULL to enclose all points          |
| **result**     | an [SDL_FRect](SDL_FRect) structure filled in with the minimal enclosing rectangle |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if any points were enclosed or
[SDL_FALSE](SDL_FALSE) if all the points were outside of the clipping
rectangle.

## Remarks

If `clip` is not NULL then only points inside of the clipping rectangle are
considered.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

