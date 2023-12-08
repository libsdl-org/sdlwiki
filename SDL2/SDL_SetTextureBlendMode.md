###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextureBlendMode

Set the blend mode for a texture, used by [SDL_RenderCopy](SDL_RenderCopy.md)().

## Syntax

```c
int SDL_SetTextureBlendMode(SDL_Texture * texture,
                            SDL_BlendMode blendMode);

```

## Function Parameters

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **texture**       | the texture to update                                          |
| **blendMode**     | the [SDL_BlendMode](SDL_BlendMode.md) to use for texture blending |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If the blend mode is not supported, the closest supported mode is chosen
and this function returns -1.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetTextureBlendMode](SDL_GetTextureBlendMode.md)
* [SDL_RenderCopy](SDL_RenderCopy.md)

----
[CategoryAPI](CategoryAPI.md)
