###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderFillRect

Fill a rectangle on the current rendering target with the drawing color.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderFillRect(SDL_Renderer * renderer,
                   const SDL_Rect * rect);
```

## Function Parameters

|                                |              |                                                                                                                |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context                                                                                          |
| const [SDL_Rect](SDL_Rect) *   | **rect**     | the [SDL_Rect](SDL_Rect) structure representing the rectangle to fill, or NULL for the entire rendering target |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The current drawing color is set by
[SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)(), and the color's alpha
value is ignored unless blending is enabled with the appropriate call to
[SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RenderDrawLine](SDL_RenderDrawLine)
- [SDL_RenderDrawLines](SDL_RenderDrawLines)
- [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
- [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
- [SDL_RenderDrawRect](SDL_RenderDrawRect)
- [SDL_RenderDrawRects](SDL_RenderDrawRects)
- [SDL_RenderFillRects](SDL_RenderFillRects)
- [SDL_RenderPresent](SDL_RenderPresent)
- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

