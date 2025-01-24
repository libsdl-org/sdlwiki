# SDL_Rect

A rectangle, with the origin at the upper left (using integers).

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
typedef struct SDL_Rect
{
    int x, y;
    int w, h;
} SDL_Rect;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_RectEmpty](SDL_RectEmpty)
- [SDL_RectsEqual](SDL_RectsEqual)
- [SDL_HasRectIntersection](SDL_HasRectIntersection)
- [SDL_GetRectIntersection](SDL_GetRectIntersection)
- [SDL_GetRectAndLineIntersection](SDL_GetRectAndLineIntersection)
- [SDL_GetRectUnion](SDL_GetRectUnion)
- [SDL_GetRectEnclosingPoints](SDL_GetRectEnclosingPoints)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRect](CategoryRect)

