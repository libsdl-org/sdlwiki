###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IntersectFRect

Calculate the intersection of two rectangles with float precision.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_bool SDL_IntersectFRect(const SDL_FRect * A,
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

This function is available since SDL 2.0.22.

## Related Functions

* [SDL_HasIntersectionF](SDL_HasIntersectionF)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


