###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectIntersectionFloat

Calculate the intersection of two rectangles with float precision.

## Syntax

```c
SDL_bool SDL_GetRectIntersectionFloat(const SDL_FRect * A,
                            const SDL_FRect * B,
                            SDL_FRect * result);

```

## Function Parameters

|                |                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------- |
| **A**          | an [SDL_FRect](SDL_FRect) structure representing the first rectangle                          |
| **B**          | an [SDL_FRect](SDL_FRect) structure representing the second rectangle                         |
| **result**     | an [SDL_FRect](SDL_FRect) structure filled in with the intersection of rectangles `A` and `B` |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there is an intersection,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If `result` is NULL then this function will return [SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasRectIntersectionFloat](SDL_HasRectIntersectionFloat)

----
[CategoryAPI](CategoryAPI)

