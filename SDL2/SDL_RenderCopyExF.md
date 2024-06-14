###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderCopyExF

Copy a portion of the source texture to the current rendering target, with rotation and flipping, at subpixel precision.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderCopyExF(SDL_Renderer * renderer,
                SDL_Texture * texture,
                const SDL_Rect * srcrect,
                const SDL_FRect * dstrect,
                const double angle,
                const SDL_FPoint *center,
                const SDL_RendererFlip flip);
```

## Function Parameters

|                                            |              |                                                                                                                                                  |
| ------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) *             | **renderer** | The renderer which should copy parts of a texture.                                                                                               |
| [SDL_Texture](SDL_Texture) *               | **texture**  | The source texture.                                                                                                                              |
| const [SDL_Rect](SDL_Rect) *               | **srcrect**  | A pointer to the source rectangle, or NULL for the entire texture.                                                                               |
| const [SDL_FRect](SDL_FRect) *             | **dstrect**  | A pointer to the destination rectangle, or NULL for the entire rendering target.                                                                 |
| const double                               | **angle**    | An angle in degrees that indicates the rotation that will be applied to dstrect, rotating it in a clockwise direction.                           |
| const [SDL_FPoint](SDL_FPoint) *           | **center**   | A pointer to a point indicating the point around which dstrect will be rotated (if NULL, rotation will be done around dstrect.w/2, dstrect.h/2). |
| const [SDL_RendererFlip](SDL_RendererFlip) | **flip**     | An [SDL_RendererFlip](SDL_RendererFlip) value stating which flipping actions should be performed on the texture.                                 |

## Return Value

(int) Return 0 on success, or -1 on error.

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

