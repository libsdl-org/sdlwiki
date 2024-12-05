###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTextureBlendMode

Set the blend mode for a texture, used by [SDL_RenderTexture](SDL_RenderTexture)().

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode blendMode);
```

## Function Parameters

|                                |               |                                                                 |
| ------------------------------ | ------------- | --------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) *   | **texture**   | the texture to update.                                          |
| [SDL_BlendMode](SDL_BlendMode) | **blendMode** | the [SDL_BlendMode](SDL_BlendMode) to use for texture blending. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the blend mode is not supported, the closest supported mode is chosen
and this function returns false.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetTextureBlendMode](SDL_GetTextureBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

