###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderDrawColor

Get the color used for drawing operations (Rect, Line and Clear).

## Syntax

```c
int SDL_GetRenderDrawColor(SDL_Renderer *renderer, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);

```

## Function Parameters

|                  |                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                               |
| **r**            | a pointer filled in with the red value used to draw on the rendering target                                                         |
| **g**            | a pointer filled in with the green value used to draw on the rendering target                                                       |
| **b**            | a pointer filled in with the blue value used to draw on the rendering target                                                        |
| **a**            | a pointer filled in with the alpha value used to draw on the rendering target; usually [`SDL_ALPHA_OPAQUE`](SDL_ALPHA_OPAQUE) (255) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
