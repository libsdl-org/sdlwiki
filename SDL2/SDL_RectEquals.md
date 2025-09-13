# SDL_RectEquals

Returns true if the two rectangles are equal.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_RectEquals(const SDL_Rect *a, const SDL_Rect *b);
```

## Function Parameters

|                              |       |                               |
| ---------------------------- | ----- | ----------------------------- |
| const [SDL_Rect](SDL_Rect) * | **a** | the first rectangle to test.  |
| const [SDL_Rect](SDL_Rect) * | **b** | the second rectangle to test. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the rectangles are
equal, [SDL_FALSE](SDL_FALSE) otherwise.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

