###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Rect

A rectangle, with the origin at the upper left (using integers).

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_Rect
{
    int x, y;
    int w, h;
} SDL_Rect;
```

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_RectEmpty](SDL_RectEmpty)
* [SDL_RectsEqual](SDL_RectsEqual)
* [SDL_HasRectIntersection](SDL_HasRectIntersection)
* [SDL_GetRectIntersection](SDL_GetRectIntersection)
* [SDL_GetRectAndLineIntersection](SDL_GetRectAndLineIntersection)
* [SDL_GetRectUnion](SDL_GetRectUnion)
* [SDL_GetRectEnclosingPoints](SDL_GetRectEnclosingPoints)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

