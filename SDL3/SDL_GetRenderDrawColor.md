###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderDrawColor

Get the color used for drawing operations (Rect, Line and Clear).

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetRenderDrawColor(SDL_Renderer *renderer, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
```

## Function Parameters

|                                |              |                                                                                                                                      |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                               |
| Uint8 *                        | **r**        | a pointer filled in with the red value used to draw on the rendering target.                                                         |
| Uint8 *                        | **g**        | a pointer filled in with the green value used to draw on the rendering target.                                                       |
| Uint8 *                        | **b**        | a pointer filled in with the blue value used to draw on the rendering target.                                                        |
| Uint8 *                        | **a**        | a pointer filled in with the alpha value used to draw on the rendering target; usually [`SDL_ALPHA_OPAQUE`](SDL_ALPHA_OPAQUE) (255). |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderDrawColorFloat](SDL_GetRenderDrawColorFloat)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

