###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderRects

Draw some number of rectangles on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **renderer**     | The renderer which should draw multiple rectangles. |
| **rects**        | A pointer to an array of destination rectangles.    |
| **count**        | The number of rectangles.                           |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

