###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderTexture

Copy a portion of the texture to the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderTexture(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, const SDL_FRect *dstrect);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should copy parts of a texture.                               |
| **texture**      | The source texture.                                                              |
| **srcrect**      | A pointer to the source rectangle, or NULL for the entire texture.               |
| **dstrect**      | A pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

Returns 0 on success, or -1 on error

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

