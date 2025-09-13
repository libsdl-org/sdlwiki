# SDL_PointInFRect

Returns true if point resides inside a rectangle.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_PointInFRect(const SDL_FPoint *p, const SDL_FRect *r);
```

## Function Parameters

|                                  |       |                        |
| -------------------------------- | ----- | ---------------------- |
| const [SDL_FPoint](SDL_FPoint) * | **p** | the point to test.     |
| const [SDL_FRect](SDL_FRect) *   | **r** | the rectangle to test. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if `p` is contained by
`r`, [SDL_FALSE](SDL_FALSE) otherwise.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

