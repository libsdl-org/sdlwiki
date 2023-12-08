###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderFillRects

Fill some number of rectangles on the current rendering target with the drawing color at subpixel precision.

## Syntax

```c
int SDL_RenderFillRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **renderer**     | The renderer which should fill multiple rectangles. |
| **rects**        | A pointer to an array of destination rectangles.    |
| **count**        | The number of rectangles.                           |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
