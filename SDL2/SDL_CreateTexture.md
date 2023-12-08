###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateTexture

Create a texture for a rendering context.

## Syntax

```c
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
                                Uint32 format,
                                int access, int w,
                                int h);

```

## Function Parameters

|                  |                                                                            |
| ---------------- | -------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                      |
| **format**       | one of the enumerated values in [SDL_PixelFormatEnum](SDL_PixelFormatEnum.md) |
| **access**       | one of the enumerated values in [SDL_TextureAccess](SDL_TextureAccess.md)     |
| **w**            | the width of the texture in pixels                                         |
| **h**            | the height of the texture in pixels                                        |

## Return Value

Returns a pointer to the created texture or NULL if no rendering context
was active, the format was unsupported, or the width or height were out of
range; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

You can set the texture scaling method by setting
[`SDL_HINT_RENDER_SCALE_QUALITY`](SDL_HINT_RENDER_SCALE_QUALITY) before
creating the texture.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface.md)
* [SDL_DestroyTexture](SDL_DestroyTexture.md)
* [SDL_QueryTexture](SDL_QueryTexture.md)
* [SDL_UpdateTexture](SDL_UpdateTexture.md)

----
[CategoryAPI](CategoryAPI.md)
