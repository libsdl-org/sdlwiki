###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasIntersection

Determine whether two rectangles intersect.

## Syntax

```c
SDL_bool SDL_HasIntersection(const SDL_Rect * A,
                             const SDL_Rect * B);

```

## Function Parameters

|           |                                                                     |
| --------- | ------------------------------------------------------------------- |
| **A**     | an [SDL_Rect](SDL_Rect.md) structure representing the first rectangle  |
| **B**     | an [SDL_Rect](SDL_Rect.md) structure representing the second rectangle |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if there is an intersection,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

If either pointer is NULL the function will return [SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_IntersectRect](SDL_IntersectRect.md)

----
[CategoryAPI](CategoryAPI.md)
