###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureBlendMode

Get the blend mode used for texture copy operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetTextureBlendMode(SDL_Texture * texture,
                            SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **texture**       | the texture to query                                                |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

