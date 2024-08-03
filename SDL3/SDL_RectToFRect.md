###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RectToFRect

Convert an [SDL_Rect](SDL_Rect) to [SDL_FRect](SDL_FRect)

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE void SDL_RectToFRect(const SDL_Rect *rect, SDL_FRect *frect);
```

## Function Parameters

|                              |           |                                                                       |
| ---------------------------- | --------- | --------------------------------------------------------------------- |
| const [SDL_Rect](SDL_Rect) * | **rect**  | a pointer to an [SDL_Rect](SDL_Rect).                                 |
| [SDL_FRect](SDL_FRect) *     | **frect** | a pointer filled in with the floating point representation of `rect`. |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

