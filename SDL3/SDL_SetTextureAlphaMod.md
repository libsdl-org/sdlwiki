###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTextureAlphaMod

Set an additional alpha value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_SetTextureAlphaMod(SDL_Texture *texture, Uint8 alpha);
```

## Function Parameters

|                              |             |                                                         |
| ---------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                  |
| Uint8                        | **alpha**   | the source alpha value multiplied into copy operations. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

When this texture is rendered, during the copy operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * (alpha / 255)`

Alpha modulation is not always supported by the renderer; it will return
[SDL_FALSE](SDL_FALSE) if alpha modulation is not supported.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod)
- [SDL_SetTextureAlphaModFloat](SDL_SetTextureAlphaModFloat)
- [SDL_SetTextureColorMod](SDL_SetTextureColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

