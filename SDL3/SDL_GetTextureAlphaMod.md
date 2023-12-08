###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureAlphaMod

Get the additional alpha value multiplied into render copy operations.

## Syntax

```c
int SDL_GetTextureAlphaMod(SDL_Texture *texture, Uint8 *alpha);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **texture**     | the texture to query                             |
| **alpha**       | a pointer filled in with the current alpha value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTextureColorMod](SDL_GetTextureColorMod.md)
* [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
