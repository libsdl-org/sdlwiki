# SDL_SetTextureColorMod

Set an additional color value multiplied into render copy operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_SetTextureColorMod(SDL_Texture * texture,
                           Uint8 r, Uint8 g, Uint8 b);
```

## Function Parameters

|                              |             |                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------ |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                 |
| Uint8                        | **r**       | the red color value multiplied into copy operations.   |
| Uint8                        | **g**       | the green color value multiplied into copy operations. |
| Uint8                        | **b**       | the blue color value multiplied into copy operations.  |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this texture is rendered, during the copy operation each source color
channel is modulated by the appropriate color value according to the
following formula:

`srcC = srcC * (color / 255)`

Color modulation is not always supported by the renderer; it will return -1
if color modulation is not supported.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetTextureColorMod](SDL_GetTextureColorMod)
- [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

