###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawLines

Draw a series of connected lines on the current rendering target.

## Syntax

```c
int SDL_RenderDrawLines(SDL_Renderer * renderer,
                        const SDL_Point * points,
                        int count);

```

## Function Parameters

|                  |                                                                                   |
| ---------------- | --------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                             |
| **points**       | an array of [SDL_Point](SDL_Point) structures representing points along the lines |
| **count**        | the number of points, drawing count-1 lines                                       |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderDrawLine](SDL_RenderDrawLine)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
* [SDL_RenderDrawRect](SDL_RenderDrawRect)
* [SDL_RenderDrawRects](SDL_RenderDrawRects)
* [SDL_RenderFillRect](SDL_RenderFillRect)
* [SDL_RenderFillRects](SDL_RenderFillRects)
* [SDL_RenderPresent](SDL_RenderPresent)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI)

