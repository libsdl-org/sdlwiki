###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HasRectIntersectionFloat

Determine whether two rectangles intersect with float precision.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
bool SDL_HasRectIntersectionFloat(const SDL_FRect *A, const SDL_FRect *B);
```

## Function Parameters

|                                |       |                                                                        |
| ------------------------------ | ----- | ---------------------------------------------------------------------- |
| const [SDL_FRect](SDL_FRect) * | **A** | an [SDL_FRect](SDL_FRect) structure representing the first rectangle.  |
| const [SDL_FRect](SDL_FRect) * | **B** | an [SDL_FRect](SDL_FRect) structure representing the second rectangle. |

## Return Value

(bool) Returns true if there is an intersection, false otherwise.

## Remarks

If either pointer is NULL the function will return false.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRectIntersection](SDL_GetRectIntersection)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

