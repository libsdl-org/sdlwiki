###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureAlphaMod

Get the additional alpha value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_GetTextureAlphaMod(SDL_Texture *texture, Uint8 *alpha);
```

## Function Parameters

|                              |             |                                                   |
| ---------------------------- | ----------- | ------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query.                             |
| Uint8 *                      | **alpha**   | a pointer filled in with the current alpha value. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetTextureAlphaModFloat](SDL_GetTextureAlphaModFloat)
- [SDL_GetTextureColorMod](SDL_GetTextureColorMod)
- [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

