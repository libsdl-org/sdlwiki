###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderTextureRotated

Copy a portion of the source texture to the current rendering target, with rotation and flipping, at subpixel precision.

## Syntax

```c
int SDL_RenderTextureRotated(SDL_Renderer *renderer, SDL_Texture *texture,
                             const SDL_FRect *srcrect, const SDL_FRect *dstrect,
                             const double angle, const SDL_FPoint *center,
                             const SDL_RendererFlip flip);

```

## Function Parameters

|                  |                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **renderer**     | The renderer which should copy parts of a texture.                                                                                               |
| **texture**      | The source texture.                                                                                                                              |
| **srcrect**      | A pointer to the source rectangle, or NULL for the entire texture.                                                                               |
| **dstrect**      | A pointer to the destination rectangle, or NULL for the entire rendering target.                                                                 |
| **angle**        | An angle in degrees that indicates the rotation that will be applied to dstrect, rotating it in a clockwise direction                            |
| **center**       | A pointer to a point indicating the point around which dstrect will be rotated (if NULL, rotation will be done around dstrect.w/2, dstrect.h/2). |
| **flip**         | An [SDL_RendererFlip](SDL_RendererFlip) value stating which flipping actions should be performed on the texture                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

