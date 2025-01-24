# SDL_RenderTexture

Copy a portion of the texture to the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderTexture(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, const SDL_FRect *dstrect);
```

## Function Parameters

|                                |              |                                                                                  |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should copy parts of a texture.                               |
| [SDL_Texture](SDL_Texture) *   | **texture**  | the source texture.                                                              |
| const [SDL_FRect](SDL_FRect) * | **srcrect**  | a pointer to the source rectangle, or NULL for the entire texture.               |
| const [SDL_FRect](SDL_FRect) * | **dstrect**  | a pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderTextureRotated](SDL_RenderTextureRotated)
- [SDL_RenderTextureTiled](SDL_RenderTextureTiled)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

