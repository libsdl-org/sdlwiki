###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawPoints

Draw multiple points on the current rendering target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_RenderDrawPoints(SDL_Renderer * renderer,
                         const SDL_Point * points,
                         int count);

```

## Function Parameters

|                  |                                                                                 |
| ---------------- | ------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                           |
| **points**       | an array of [SDL_Point](SDL_Point) structures that represent the points to draw |
| **count**        | the number of points to draw                                                    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderDrawLine](SDL_RenderDrawLine)
* [SDL_RenderDrawLines](SDL_RenderDrawLines)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
* [SDL_RenderDrawRect](SDL_RenderDrawRect)
* [SDL_RenderDrawRects](SDL_RenderDrawRects)
* [SDL_RenderFillRect](SDL_RenderFillRect)
* [SDL_RenderFillRects](SDL_RenderFillRects)
* [SDL_RenderPresent](SDL_RenderPresent)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI)

