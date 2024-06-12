###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawLine

Draw a line on the current rendering target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderDrawLine(SDL_Renderer * renderer,
                   int x1, int y1, int x2, int y2);
```

## Function Parameters

|                                |              |                                     |
| ------------------------------ | ------------ | ----------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context               |
| int                            | **x1**       | the x coordinate of the start point |
| int                            | **y1**       | the y coordinate of the start point |
| int                            | **x2**       | the x coordinate of the end point   |
| int                            | **y2**       | the y coordinate of the end point   |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_RenderDrawLine](SDL_RenderDrawLine)() draws the line to include both
end points. If you want to draw multiple, connecting lines use
[SDL_RenderDrawLines](SDL_RenderDrawLines)() instead.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RenderDrawLines](SDL_RenderDrawLines)
- [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
- [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
- [SDL_RenderDrawRect](SDL_RenderDrawRect)
- [SDL_RenderDrawRects](SDL_RenderDrawRects)
- [SDL_RenderFillRect](SDL_RenderFillRect)
- [SDL_RenderFillRects](SDL_RenderFillRects)
- [SDL_RenderPresent](SDL_RenderPresent)
- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

