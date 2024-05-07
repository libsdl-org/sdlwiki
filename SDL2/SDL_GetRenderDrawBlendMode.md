###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRenderDrawBlendMode

Get the blend mode used for drawing operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetRenderDrawBlendMode(SDL_Renderer * renderer,
                               SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **renderer**      | the rendering context                                               |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

