# SDL_FRectEmpty

Returns true if the rectangle has no area.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_FRectEmpty(const SDL_FRect *r);
```

## Function Parameters

|                                |       |                        |
| ------------------------------ | ----- | ---------------------- |
| const [SDL_FRect](SDL_FRect) * | **r** | the rectangle to test. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the rectangle is
"empty", [SDL_FALSE](SDL_FALSE) otherwise.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

