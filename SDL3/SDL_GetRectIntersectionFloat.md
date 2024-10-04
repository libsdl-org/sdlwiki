###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRectIntersectionFloat

Calculate the intersection of two rectangles with float precision.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
bool SDL_GetRectIntersectionFloat(const SDL_FRect *A, const SDL_FRect *B, SDL_FRect *result);
```

## Function Parameters

|                                |            |                                                                                                |
| ------------------------------ | ---------- | ---------------------------------------------------------------------------------------------- |
| const [SDL_FRect](SDL_FRect) * | **A**      | an [SDL_FRect](SDL_FRect) structure representing the first rectangle.                          |
| const [SDL_FRect](SDL_FRect) * | **B**      | an [SDL_FRect](SDL_FRect) structure representing the second rectangle.                         |
| [SDL_FRect](SDL_FRect) *       | **result** | an [SDL_FRect](SDL_FRect) structure filled in with the intersection of rectangles `A` and `B`. |

## Return Value

(bool) Returns true if there is an intersection, false otherwise.

## Remarks

If `result` is NULL then this function will return false.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HasRectIntersectionFloat](SDL_HasRectIntersectionFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

