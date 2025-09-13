# SDL_RectEmpty

Returns true if the rectangle has no area.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_RectEmpty(const SDL_Rect *r);
```

## Function Parameters

|                              |       |                        |
| ---------------------------- | ----- | ---------------------- |
| const [SDL_Rect](SDL_Rect) * | **r** | the rectangle to test. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the rectangle is
"empty", [SDL_FALSE](SDL_FALSE) otherwise.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

