###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderDrawColor

Get the color used for drawing operations (Rect, Line and Clear).

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderDrawColor(SDL_Renderer *renderer, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
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

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetRenderDrawColorFloat](SDL_GetRenderDrawColorFloat)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

