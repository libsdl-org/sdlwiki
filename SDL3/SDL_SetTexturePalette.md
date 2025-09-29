# SDL_SetTexturePalette

Set the palette used by a texture.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetTexturePalette(SDL_Texture *texture, SDL_Palette *palette);
```

## Function Parameters

|                              |             |                                                  |
| ---------------------------- | ----------- | ------------------------------------------------ |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                           |
| [SDL_Palette](SDL_Palette) * | **palette** | the [SDL_Palette](SDL_Palette) structure to use. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Setting the palette keeps an internal reference to the palette, which can
be safely destroyed afterwards.

A single palette can be shared with many textures.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_CreatePalette](SDL_CreatePalette)
- [SDL_GetTexturePalette](SDL_GetTexturePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

