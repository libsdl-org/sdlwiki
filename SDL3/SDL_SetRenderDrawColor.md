# SDL_SetRenderDrawColor

Set the color used for drawing operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderDrawColor(SDL_Renderer *renderer, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
```

## Function Parameters

|                                |              |                                                                                                                                                                                                                    |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                                                                                             |
| Uint8                          | **r**        | the red value used to draw on the rendering target.                                                                                                                                                                |
| Uint8                          | **g**        | the green value used to draw on the rendering target.                                                                                                                                                              |
| Uint8                          | **b**        | the blue value used to draw on the rendering target.                                                                                                                                                               |
| Uint8                          | **a**        | the alpha value used to draw on the rendering target; usually [`SDL_ALPHA_OPAQUE`](SDL_ALPHA_OPAQUE) (255). Use [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode) to specify how the alpha channel is used. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Set the color for drawing or filling rectangles, lines, and points, and for
[SDL_RenderClear](SDL_RenderClear)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderDrawColor](SDL_GetRenderDrawColor)
- [SDL_SetRenderDrawColorFloat](SDL_SetRenderDrawColorFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

