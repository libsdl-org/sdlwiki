###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawColorFloat

Set the color used for drawing operations (Rect, Line and Clear).

## Syntax

```c
int SDL_SetRenderDrawColorFloat(SDL_Renderer *renderer, float r, float g, float b, float a);

```

## Function Parameters

|                  |                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                                                       |
| **r**            | the red value used to draw on the rendering target                                                                                                          |
| **g**            | the green value used to draw on the rendering target                                                                                                        |
| **b**            | the blue value used to draw on the rendering target                                                                                                         |
| **a**            | the alpha value used to draw on the rendering target. Use [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode) to specify how the alpha channel is used |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Set the color for drawing or filling rectangles, lines, and points, and for
[SDL_RenderClear](SDL_RenderClear)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderDrawColorFloat](SDL_GetRenderDrawColorFloat)
* [SDL_RenderClear](SDL_RenderClear)
* [SDL_RenderFillRect](SDL_RenderFillRect)
* [SDL_RenderFillRects](SDL_RenderFillRects)
* [SDL_RenderLine](SDL_RenderLine)
* [SDL_RenderLines](SDL_RenderLines)
* [SDL_RenderPoint](SDL_RenderPoint)
* [SDL_RenderPoints](SDL_RenderPoints)
* [SDL_RenderRect](SDL_RenderRect)
* [SDL_RenderRects](SDL_RenderRects)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI)

