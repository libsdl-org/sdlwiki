###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTextureBlendMode

Set the blend mode for a texture, used by [SDL_RenderTexture](SDL_RenderTexture)().

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_SetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode blendMode);

```

## Function Parameters

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **texture**       | the texture to update                                          |
| **blendMode**     | the [SDL_BlendMode](SDL_BlendMode) to use for texture blending |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the blend mode is not supported, the closest supported mode is chosen
and this function returns -1.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetTextureBlendMode](SDL_GetTextureBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


