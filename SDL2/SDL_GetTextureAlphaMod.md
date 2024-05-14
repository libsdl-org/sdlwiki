###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureAlphaMod

Get the additional alpha value multiplied into render copy operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetTextureAlphaMod(SDL_Texture * texture,
                           Uint8 * alpha);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **texture**     | the texture to query                             |
| **alpha**       | a pointer filled in with the current alpha value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetTextureColorMod](SDL_GetTextureColorMod)
- [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

