# SDL_SetRenderTextureAddressMode

Set the texture addressing mode used in [SDL_RenderGeometry](SDL_RenderGeometry)().

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderTextureAddressMode(SDL_Renderer *renderer, SDL_TextureAddressMode u_mode, SDL_TextureAddressMode v_mode);
```

## Function Parameters

|                                                  |              |                                                                                                                                               |
| ------------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *                   | **renderer** | the rendering context.                                                                                                                        |
| [SDL_TextureAddressMode](SDL_TextureAddressMode) | **u_mode**   | the [SDL_TextureAddressMode](SDL_TextureAddressMode) to use for horizontal texture coordinates in [SDL_RenderGeometry](SDL_RenderGeometry)(). |
| [SDL_TextureAddressMode](SDL_TextureAddressMode) | **v_mode**   | the [SDL_TextureAddressMode](SDL_TextureAddressMode) to use for vertical texture coordinates in [SDL_RenderGeometry](SDL_RenderGeometry)().   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_RenderGeometry](SDL_RenderGeometry)
- [SDL_RenderGeometryRaw](SDL_RenderGeometryRaw)
- [SDL_GetRenderTextureAddressMode](SDL_GetRenderTextureAddressMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

