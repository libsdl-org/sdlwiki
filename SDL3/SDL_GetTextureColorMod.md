###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTextureColorMod

Get the additional color value multiplied into render copy operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetTextureColorMod(SDL_Texture *texture, Uint8 *r, Uint8 *g, Uint8 *b);
```

## Function Parameters

|                              |             |                                                         |
| ---------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query.                                   |
| Uint8 *                      | **r**       | a pointer filled in with the current red color value.   |
| Uint8 *                      | **g**       | a pointer filled in with the current green color value. |
| Uint8 *                      | **b**       | a pointer filled in with the current blue color value.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod)
- [SDL_GetTextureColorModFloat](SDL_GetTextureColorModFloat)
- [SDL_SetTextureColorMod](SDL_SetTextureColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

