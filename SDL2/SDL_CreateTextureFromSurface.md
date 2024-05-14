###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateTextureFromSurface

Create a texture from an existing surface.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer * renderer, SDL_Surface * surface);

```

## Function Parameters

|                  |                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                   |
| **surface**      | the [SDL_Surface](SDL_Surface) structure containing pixel data used to fill the texture |

## Return Value

Returns the created texture or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The surface is not modified or freed by this function.

The [SDL_TextureAccess](SDL_TextureAccess) hint for the created texture is
[`SDL_TEXTUREACCESS_STATIC`](SDL_TEXTUREACCESS_STATIC).

The pixel format of the created texture may be different from the pixel
format of the surface. Use [SDL_QueryTexture](SDL_QueryTexture)() to query
the pixel format of the texture.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateTexture](SDL_CreateTexture)
- [SDL_DestroyTexture](SDL_DestroyTexture)
- [SDL_QueryTexture](SDL_QueryTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

