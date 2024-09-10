###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetRenderTarget

Set a texture as the current rendering target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_SetRenderTarget(SDL_Renderer *renderer,
                        SDL_Texture *texture);
```

## Function Parameters

|                                |              |                                                                                                                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                                                  |
| [SDL_Texture](SDL_Texture) *   | **texture**  | the targeted texture, which must be created with the [`SDL_TEXTUREACCESS_TARGET`](SDL_TEXTUREACCESS_TARGET) flag, or NULL to render to the window instead of a texture. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Before using this function, you should check the
[`SDL_RENDERER_TARGETTEXTURE`](SDL_RENDERER_TARGETTEXTURE) bit in the flags
of [SDL_RendererInfo](SDL_RendererInfo) to see if render targets are
supported.

The default render target is the window for which the renderer was created.
To stop rendering to a texture and render to the window again, call this
function with a NULL `texture`. This will reset the renderer's viewport,
clipping rectangle, and scaling settings to the state they were in before
setting a non-NULL `texture` target, losing any changes made in the meantime.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetRenderTarget](SDL_GetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

