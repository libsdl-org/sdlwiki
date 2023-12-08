###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawLine

Draw a line on the current rendering target.

## Syntax

```c
int SDL_RenderDrawLine(SDL_Renderer * renderer,
                       int x1, int y1, int x2, int y2);

```

## Function Parameters

|                  |                                     |
| ---------------- | ----------------------------------- |
| **renderer**     | the rendering context               |
| **x1**           | the x coordinate of the start point |
| **y1**           | the y coordinate of the start point |
| **x2**           | the x coordinate of the end point   |
| **y2**           | the y coordinate of the end point   |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

[SDL_RenderDrawLine](SDL_RenderDrawLine.md)() draws the line to include both
end points. If you want to draw multiple, connecting lines use
[SDL_RenderDrawLines](SDL_RenderDrawLines.md)() instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderDrawLines](SDL_RenderDrawLines.md)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint.md)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints.md)
* [SDL_RenderDrawRect](SDL_RenderDrawRect.md)
* [SDL_RenderDrawRects](SDL_RenderDrawRects.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)
* [SDL_RenderPresent](SDL_RenderPresent.md)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md)
