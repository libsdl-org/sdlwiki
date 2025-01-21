###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTextureColorModFloat

Set an additional color value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetTextureColorModFloat(SDL_Texture *texture, float r, float g, float b);
```

## Function Parameters

|                              |             |                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------ |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                 |
| float                        | **r**       | the red color value multiplied into copy operations.   |
| float                        | **g**       | the green color value multiplied into copy operations. |
| float                        | **b**       | the blue color value multiplied into copy operations.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this texture is rendered, during the copy operation each source color
channel is modulated by the appropriate color value according to the
following formula:

`srcC = srcC * color`

Color modulation is not always supported by the renderer; it will return
false if color modulation is not supported.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTextureColorModFloat](SDL_GetTextureColorModFloat)
- [SDL_SetTextureAlphaModFloat](SDL_SetTextureAlphaModFloat)
- [SDL_SetTextureColorMod](SDL_SetTextureColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

