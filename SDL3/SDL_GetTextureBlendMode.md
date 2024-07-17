###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureBlendMode

Get the blend mode used for texture copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_BlendMode SDL_GetTextureBlendMode(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                       |
| ---------------------------- | ----------- | --------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query. |

## Return Value

([SDL_BlendMode](SDL_BlendMode)) Returns the current
[SDL_BlendMode](SDL_BlendMode).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

