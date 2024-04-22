###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawPoint

Draw a point on the current rendering target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderDrawPoint(SDL_Renderer * renderer,
                        int x, int y);

```

## Function Parameters

|                  |                               |
| ---------------- | ----------------------------- |
| **renderer**     | the rendering context         |
| **x**            | the x coordinate of the point |
| **y**            | the y coordinate of the point |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_RenderDrawPoint](SDL_RenderDrawPoint)() draws a single point. If you
want to draw multiple, use [SDL_RenderDrawPoints](SDL_RenderDrawPoints)()
instead.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_RenderDrawLine](SDL_RenderDrawLine)
* [SDL_RenderDrawLines](SDL_RenderDrawLines)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
* [SDL_RenderDrawRect](SDL_RenderDrawRect)
* [SDL_RenderDrawRects](SDL_RenderDrawRects)
* [SDL_RenderFillRect](SDL_RenderFillRect)
* [SDL_RenderFillRects](SDL_RenderFillRects)
* [SDL_RenderPresent](SDL_RenderPresent)
* [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

