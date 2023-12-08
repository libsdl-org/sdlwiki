###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasIntersectionF

Determine whether two rectangles intersect with float precision.

## Syntax

```c
SDL_bool SDL_HasIntersectionF(const SDL_FRect * A,
                              const SDL_FRect * B);

```

## Function Parameters

|           |                                                                       |
| --------- | --------------------------------------------------------------------- |
| **A**     | an [SDL_FRect](SDL_FRect.md) structure representing the first rectangle  |
| **B**     | an [SDL_FRect](SDL_FRect.md) structure representing the second rectangle |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if there is an intersection,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

If either pointer is NULL the function will return [SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 2.0.22.

## Related Functions

* [SDL_IntersectRect](SDL_IntersectRect.md)

----
[CategoryAPI](CategoryAPI.md)
