###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IntersectRect

Calculate the intersection of two rectangles.

## Syntax

```c
SDL_bool SDL_IntersectRect(const SDL_Rect * A,
                           const SDL_Rect * B,
                           SDL_Rect * result);

```

## Function Parameters

|                |                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------- |
| **A**          | an [SDL_Rect](SDL_Rect.md) structure representing the first rectangle                          |
| **B**          | an [SDL_Rect](SDL_Rect.md) structure representing the second rectangle                         |
| **result**     | an [SDL_Rect](SDL_Rect.md) structure filled in with the intersection of rectangles `A` and `B` |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if there is an intersection,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

If `result` is NULL then this function will return [SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HasIntersection](SDL_HasIntersection.md)

----
[CategoryAPI](CategoryAPI.md)
