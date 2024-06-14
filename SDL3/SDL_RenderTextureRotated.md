###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderTextureRotated

Copy a portion of the source texture to the current rendering target, with rotation and flipping, at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_RenderTextureRotated(SDL_Renderer *renderer, SDL_Texture *texture,
                         const SDL_FRect *srcrect, const SDL_FRect *dstrect,
                         const double angle, const SDL_FPoint *center,
                         const SDL_FlipMode flip);
```

## Function Parameters

|                                    |              |                                                                                                                                                  |
| ---------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) *     | **renderer** | the renderer which should copy parts of a texture.                                                                                               |
| [SDL_Texture](SDL_Texture) *       | **texture**  | the source texture.                                                                                                                              |
| const [SDL_FRect](SDL_FRect) *     | **srcrect**  | a pointer to the source rectangle, or NULL for the entire texture.                                                                               |
| const [SDL_FRect](SDL_FRect) *     | **dstrect**  | a pointer to the destination rectangle, or NULL for the entire rendering target.                                                                 |
| const double                       | **angle**    | an angle in degrees that indicates the rotation that will be applied to dstrect, rotating it in a clockwise direction.                           |
| const [SDL_FPoint](SDL_FPoint) *   | **center**   | a pointer to a point indicating the point around which dstrect will be rotated (if NULL, rotation will be done around dstrect.w/2, dstrect.h/2). |
| const [SDL_FlipMode](SDL_FlipMode) | **flip**     | an [SDL_FlipMode](SDL_FlipMode) value stating which flipping actions should be performed on the texture.                                         |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderTexture](SDL_RenderTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

