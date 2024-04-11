###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderCopyF

Copy a portion of the texture to the current rendering target at subpixel precision.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_RenderCopyF(SDL_Renderer * renderer,
                    SDL_Texture * texture,
                    const SDL_Rect * srcrect,
                    const SDL_FRect * dstrect);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should copy parts of a texture.                               |
| **texture**      | The source texture.                                                              |
| **srcrect**      | A pointer to the source rectangle, or NULL for the entire texture.               |
| **dstrect**      | A pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

