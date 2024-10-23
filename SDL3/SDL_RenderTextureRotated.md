###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RenderTextureRotated

Copy a portion of the source texture to the current rendering target, with rotation and flipping, at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderTextureRotated(SDL_Renderer *renderer, SDL_Texture *texture,
                         const SDL_FRect *srcrect, const SDL_FRect *dstrect,
                         double angle, const SDL_FPoint *center,
                         SDL_FlipMode flip);
```

## Function Parameters

|                                  |              |                                                                                                                                                  |
| -------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) *   | **renderer** | the renderer which should copy parts of a texture.                                                                                               |
| [SDL_Texture](SDL_Texture) *     | **texture**  | the source texture.                                                                                                                              |
| const [SDL_FRect](SDL_FRect) *   | **srcrect**  | a pointer to the source rectangle, or NULL for the entire texture.                                                                               |
| const [SDL_FRect](SDL_FRect) *   | **dstrect**  | a pointer to the destination rectangle, or NULL for the entire rendering target.                                                                 |
| double                           | **angle**    | an angle in degrees that indicates the rotation that will be applied to dstrect, rotating it in a clockwise direction.                           |
| const [SDL_FPoint](SDL_FPoint) * | **center**   | a pointer to a point indicating the point around which dstrect will be rotated (if NULL, rotation will be done around dstrect.w/2, dstrect.h/2). |
| [SDL_FlipMode](SDL_FlipMode)     | **flip**     | an [SDL_FlipMode](SDL_FlipMode) value stating which flipping actions should be performed on the texture.                                         |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_RenderTexture](SDL_RenderTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

