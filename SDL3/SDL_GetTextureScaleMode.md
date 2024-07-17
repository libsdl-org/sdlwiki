###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_ScaleMode SDL_GetTextureScaleMode(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                       |
| ---------------------------- | ----------- | --------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query. |

## Return Value

([SDL_ScaleMode](SDL_ScaleMode)) Returns the current scale mode.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetTextureScaleMode](SDL_SetTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

