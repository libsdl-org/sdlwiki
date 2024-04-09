###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawColorFloat

Set the color used for drawing operations (Rect, Line and Clear).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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

## See Also

* [SDL_GetRenderDrawColorFloat](SDL_GetRenderDrawColorFloat)
* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

