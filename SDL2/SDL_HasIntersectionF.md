###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasIntersectionF

Determine whether two rectangles intersect with float precision.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_bool SDL_HasIntersectionF(const SDL_FRect * A,
                              const SDL_FRect * B);

```

## Function Parameters

|           |                                                                       |
| --------- | --------------------------------------------------------------------- |
| **A**     | an [SDL_FRect](SDL_FRect) structure representing the first rectangle  |
| **B**     | an [SDL_FRect](SDL_FRect) structure representing the second rectangle |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there is an intersection,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If either pointer is NULL the function will return [SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 2.0.22.

## See Also

- [SDL_IntersectRect](SDL_IntersectRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

