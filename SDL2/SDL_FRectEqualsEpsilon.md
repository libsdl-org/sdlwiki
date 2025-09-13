# SDL_FRectEqualsEpsilon

Returns true if the two rectangles are equal, within some given epsilon.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_FRectEqualsEpsilon(const SDL_FRect *a, const SDL_FRect *b, const float epsilon);
```

## Function Parameters

|                                |             |                                   |
| ------------------------------ | ----------- | --------------------------------- |
| const [SDL_FRect](SDL_FRect) * | **a**       | the first rectangle to test.      |
| const [SDL_FRect](SDL_FRect) * | **b**       | the second rectangle to test.     |
| const float                    | **epsilon** | the epsilon value for comparison. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the rectangles are
equal, [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

