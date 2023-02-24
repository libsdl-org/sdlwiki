###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawColor

Set the color used for drawing operations (Rect, Line and Clear).

## Syntax

```c
int SDL_SetRenderDrawColor(SDL_Renderer *renderer, Uint8 r, Uint8 g, Uint8 b, Uint8 a);

```

## Function Parameters

|                  |                                                                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                                                                                                             |
| **r**            | the red value used to draw on the rendering target                                                                                                                                                                |
| **g**            | the green value used to draw on the rendering target                                                                                                                                                              |
| **b**            | the blue value used to draw on the rendering target                                                                                                                                                               |
| **a**            | the alpha value used to draw on the rendering target; usually [`SDL_ALPHA_OPAQUE`](SDL_ALPHA_OPAQUE) (255). Use [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode) to specify how the alpha channel is used |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Set the color for drawing or filling rectangles, lines, and points, and for
[SDL_RenderClear](SDL_RenderClear)().

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
SDL_Rect rectangle;

rectangle.x = 0;
rectangle.y = 0;
rectangle.w = 50;
rectangle.h = 50;
SDL_RenderFillRect(renderer, &rectangle);
```

## Related Functions

* [SDL_GetRenderDrawColor](SDL_GetRenderDrawColor)
* [SDL_RenderClear](SDL_RenderClear)
* [SDL_RenderLine](SDL_RenderLine)
* [SDL_RenderLines](SDL_RenderLines)
* [SDL_RenderPoint](SDL_RenderPoint)
* [SDL_RenderPoints](SDL_RenderPoints)
* [SDL_RenderRect](SDL_RenderRect)
* [SDL_RenderRects](SDL_RenderRects)
* [SDL_RenderFillRect](SDL_RenderFillRect)
* [SDL_RenderFillRects](SDL_RenderFillRects)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


