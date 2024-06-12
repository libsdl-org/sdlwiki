###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QueryTexture

Query the attributes of a texture.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_QueryTexture(SDL_Texture * texture,
                 Uint32 * format, int *access,
                 int *w, int *h);
```

## Function Parameters

|                              |             |                                                                                                                                                                                                                                                              |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query                                                                                                                                                                                                                                         |
| Uint32 *                     | **format**  | a pointer filled in with the raw format of the texture; the actual format may differ, but pixel transfers will use this format (one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values). This argument can be NULL if you don't need this information. |
| int *                        | **access**  | a pointer filled in with the actual access to the texture (one of the [SDL_TextureAccess](SDL_TextureAccess) values). This argument can be NULL if you don't need this information.                                                                          |
| int *                        | **w**       | a pointer filled in with the width of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                   |
| int *                        | **h**       | a pointer filled in with the height of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                  |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateTexture](SDL_CreateTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

