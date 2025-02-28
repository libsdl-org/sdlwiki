# SDL_SetRenderTarget

Set a texture as the current rendering target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderTarget(SDL_Renderer *renderer, SDL_Texture *texture);
```

## Function Parameters

|                                |              |                                                                                                                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                                                  |
| [SDL_Texture](SDL_Texture) *   | **texture**  | the targeted texture, which must be created with the [`SDL_TEXTUREACCESS_TARGET`](SDL_TEXTUREACCESS_TARGET) flag, or NULL to render to the window instead of a texture. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The default render target is the window for which the renderer was created.
To stop rendering to a texture and render to the window again, call this
function with a NULL `texture`.

Viewport, cliprect, scale, and logical presentation are unique to each
render target. Get and set functions for these states apply to the current
render target set by this function, and those states persist on each target
when the current render target changes.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderTarget](SDL_GetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

