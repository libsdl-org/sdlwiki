###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawColor

Set the color used for drawing operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should use `#include <SDL3/SDL.h>`

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
SDL_Renderer *renderer;
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);

SDL_FRect rectangle;
rectangle.x =  0.f;
rectangle.y =  0.f;
rectangle.w = 50.f;
rectangle.h = 50.f;

SDL_RenderFillRect(renderer, &rectangle);
```

## See Also

* [SDL_GetRenderDrawColor](SDL_GetRenderDrawColor)
* [SDL_SetRenderDrawColorFloat](SDL_SetRenderDrawColorFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


