###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureColorMod

Get the additional color value multiplied into render copy operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetTextureColorMod(SDL_Texture * texture,
                       Uint8 * r, Uint8 * g,
                       Uint8 * b);
```

## Function Parameters

|                              |             |                                                         |
| ---------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query.                                   |
| Uint8 *                      | **r**       | a pointer filled in with the current red color value.   |
| Uint8 *                      | **g**       | a pointer filled in with the current green color value. |
| Uint8 *                      | **b**       | a pointer filled in with the current blue color value.  |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod)
- [SDL_SetTextureColorMod](SDL_SetTextureColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

