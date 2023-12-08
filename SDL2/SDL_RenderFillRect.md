###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderFillRect

Fill a rectangle on the current rendering target with the drawing color.

## Syntax

```c
int SDL_RenderFillRect(SDL_Renderer * renderer,
                       const SDL_Rect * rect);

```

## Function Parameters

|                  |                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                          |
| **rect**         | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to fill, or NULL for the entire rendering target |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The current drawing color is set by
[SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)(), and the color's alpha
value is ignored unless blending is enabled with the appropriate call to
[SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderDrawLine](SDL_RenderDrawLine.md)
* [SDL_RenderDrawLines](SDL_RenderDrawLines.md)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint.md)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints.md)
* [SDL_RenderDrawRect](SDL_RenderDrawRect.md)
* [SDL_RenderDrawRects](SDL_RenderDrawRects.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)
* [SDL_RenderPresent](SDL_RenderPresent.md)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode.md)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md)
