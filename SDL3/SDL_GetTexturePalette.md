# SDL_GetTexturePalette

Get the palette used by a texture.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Palette * SDL_GetTexturePalette(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                       |
| ---------------------------- | ----------- | --------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query. |

## Return Value

([SDL_Palette](SDL_Palette) *) Returns a pointer to the palette used by the
texture, or NULL if there is no palette used.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_SetTexturePalette](SDL_SetTexturePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

