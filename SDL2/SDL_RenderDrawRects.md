###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawRects

Draw some number of rectangles on the current rendering target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderDrawRects(SDL_Renderer * renderer,
                    const SDL_Rect * rects,
                    int count);
```

## Function Parameters

|                                |              |                                                                                      |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                               |
| const [SDL_Rect](SDL_Rect) *   | **rects**    | an array of [SDL_Rect](SDL_Rect) structures representing the rectangles to be drawn. |
| int                            | **count**    | the number of rectangles.                                                            |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RenderDrawLine](SDL_RenderDrawLine)
- [SDL_RenderDrawLines](SDL_RenderDrawLines)
- [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
- [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
- [SDL_RenderDrawRect](SDL_RenderDrawRect)
- [SDL_RenderFillRect](SDL_RenderFillRect)
- [SDL_RenderFillRects](SDL_RenderFillRects)
- [SDL_RenderPresent](SDL_RenderPresent)
- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

