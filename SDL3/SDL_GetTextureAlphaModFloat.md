###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureAlphaModFloat

Get the additional alpha value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetTextureAlphaModFloat(SDL_Texture *texture, float *alpha);
```

## Function Parameters

|                              |             |                                                   |
| ---------------------------- | ----------- | ------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query.                             |
| float *                      | **alpha**   | a pointer filled in with the current alpha value. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod)
- [SDL_GetTextureColorModFloat](SDL_GetTextureColorModFloat)
- [SDL_SetTextureAlphaModFloat](SDL_SetTextureAlphaModFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

