###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderCopyF

Copy a portion of the texture to the current rendering target at subpixel precision.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderCopyF(SDL_Renderer * renderer,
                SDL_Texture * texture,
                const SDL_Rect * srcrect,
                const SDL_FRect * dstrect);
```

## Function Parameters

|                                |              |                                                                                  |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | The renderer which should copy parts of a texture.                               |
| [SDL_Texture](SDL_Texture) *   | **texture**  | The source texture.                                                              |
| const [SDL_Rect](SDL_Rect) *   | **srcrect**  | A pointer to the source rectangle, or NULL for the entire texture.               |
| const [SDL_FRect](SDL_FRect) * | **dstrect**  | A pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

(int) Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

