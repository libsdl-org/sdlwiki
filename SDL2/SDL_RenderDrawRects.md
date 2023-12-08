###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawRects

Draw some number of rectangles on the current rendering target.

## Syntax

```c
int SDL_RenderDrawRects(SDL_Renderer * renderer,
                        const SDL_Rect * rects,
                        int count);

```

## Function Parameters

|                  |                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                               |
| **rects**        | an array of [SDL_Rect](SDL_Rect.md) structures representing the rectangles to be drawn |
| **count**        | the number of rectangles                                                            |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderDrawLine](SDL_RenderDrawLine.md)
* [SDL_RenderDrawLines](SDL_RenderDrawLines.md)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint.md)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints.md)
* [SDL_RenderDrawRect](SDL_RenderDrawRect.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)
* [SDL_RenderPresent](SDL_RenderPresent.md)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md)
