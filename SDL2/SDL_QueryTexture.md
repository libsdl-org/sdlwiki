###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QueryTexture

Query the attributes of a texture.

## Syntax

```c
int SDL_QueryTexture(SDL_Texture * texture,
                     Uint32 * format, int *access,
                     int *w, int *h);

```

## Function Parameters

|                 |                                                                                                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **texture**     | the texture to query                                                                                                                                                                                                                                         |
| **format**      | a pointer filled in with the raw format of the texture; the actual format may differ, but pixel transfers will use this format (one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum.md) values). This argument can be NULL if you don't need this information. |
| **access**      | a pointer filled in with the actual access to the texture (one of the [SDL_TextureAccess](SDL_TextureAccess.md) values). This argument can be NULL if you don't need this information.                                                                          |
| **w**           | a pointer filled in with the width of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                   |
| **h**           | a pointer filled in with the height of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateTexture](SDL_CreateTexture.md)

----
[CategoryAPI](CategoryAPI.md)
