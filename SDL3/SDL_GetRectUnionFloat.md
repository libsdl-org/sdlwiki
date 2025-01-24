# SDL_GetRectUnionFloat

Calculate the union of two rectangles with float precision.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
bool SDL_GetRectUnionFloat(const SDL_FRect *A, const SDL_FRect *B, SDL_FRect *result);
```

## Function Parameters

|                                |            |                                                                                         |
| ------------------------------ | ---------- | --------------------------------------------------------------------------------------- |
| const [SDL_FRect](SDL_FRect) * | **A**      | an [SDL_FRect](SDL_FRect) structure representing the first rectangle.                   |
| const [SDL_FRect](SDL_FRect) * | **B**      | an [SDL_FRect](SDL_FRect) structure representing the second rectangle.                  |
| [SDL_FRect](SDL_FRect) *       | **result** | an [SDL_FRect](SDL_FRect) structure filled in with the union of rectangles `A` and `B`. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

