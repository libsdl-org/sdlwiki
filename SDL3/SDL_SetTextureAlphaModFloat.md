# SDL_SetTextureAlphaModFloat

Set an additional alpha value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetTextureAlphaModFloat(SDL_Texture *texture, float alpha);
```

## Function Parameters

|                              |             |                                                         |
| ---------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                  |
| float                        | **alpha**   | the source alpha value multiplied into copy operations. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this texture is rendered, during the copy operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * alpha`

Alpha modulation is not always supported by the renderer; it will return
false if alpha modulation is not supported.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTextureAlphaModFloat](SDL_GetTextureAlphaModFloat)
- [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod)
- [SDL_SetTextureColorModFloat](SDL_SetTextureColorModFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

