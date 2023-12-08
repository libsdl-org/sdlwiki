###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureBlendMode

Get the blend mode used for texture copy operations.

## Syntax

```c
int SDL_GetTextureBlendMode(SDL_Texture * texture,
                            SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **texture**       | the texture to query                                                |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode.md) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode.md)

----
[CategoryAPI](CategoryAPI.md)
