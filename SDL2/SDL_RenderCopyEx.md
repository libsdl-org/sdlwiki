###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderCopyEx

Copy a portion of the texture to the current rendering, with optional rotation and flipping.

## Syntax

```c
int SDL_RenderCopyEx(SDL_Renderer * renderer,
                   SDL_Texture * texture,
                   const SDL_Rect * srcrect,
                   const SDL_Rect * dstrect,
                   const double angle,
                   const SDL_Point *center,
                   const SDL_RendererFlip flip);

```

## Function Parameters

|                  |                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                                                                   |
| **texture**      | the source texture                                                                                                                                      |
| **srcrect**      | the source [SDL_Rect](SDL_Rect.md) structure or NULL for the entire texture                                                                                |
| **dstrect**      | the destination [SDL_Rect](SDL_Rect.md) structure or NULL for the entire rendering target                                                                  |
| **angle**        | an angle in degrees that indicates the rotation that will be applied to dstrect, rotating it in a clockwise direction                                   |
| **center**       | a pointer to a point indicating the point around which dstrect will be rotated (if NULL, rotation will be done around `dstrect.w / 2`, `dstrect.h / 2`) |
| **flip**         | a [SDL_RendererFlip](SDL_RendererFlip.md) value stating which flipping actions should be performed on the texture                                          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Copy a portion of the texture to the current rendering target, optionally
rotating it by angle around the given center and also flipping it
top-bottom and/or left-right.

The texture is blended with the destination based on its blend mode set
with [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode.md)().

The texture color is affected based on its color modulation set by
[SDL_SetTextureColorMod](SDL_SetTextureColorMod.md)().

The texture alpha is affected based on its alpha modulation set by
[SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderCopy](SDL_RenderCopy.md)
* [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod.md)
* [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode.md)
* [SDL_SetTextureColorMod](SDL_SetTextureColorMod.md)

----
[CategoryAPI](CategoryAPI.md)
