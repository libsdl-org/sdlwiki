###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectUnion

Calculate the union of two rectangles.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_bool SDL_GetRectUnion(const SDL_Rect *A, const SDL_Rect *B, SDL_Rect *result);
```

## Function Parameters

|                              |            |                                                                                       |
| ---------------------------- | ---------- | ------------------------------------------------------------------------------------- |
| const [SDL_Rect](SDL_Rect) * | **A**      | an [SDL_Rect](SDL_Rect) structure representing the first rectangle.                   |
| const [SDL_Rect](SDL_Rect) * | **B**      | an [SDL_Rect](SDL_Rect) structure representing the second rectangle.                  |
| [SDL_Rect](SDL_Rect) *       | **result** | an [SDL_Rect](SDL_Rect) structure filled in with the union of rectangles `A` and `B`. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

