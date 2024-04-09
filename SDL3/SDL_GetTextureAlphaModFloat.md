###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureAlphaModFloat

Get the additional alpha value multiplied into render copy operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetTextureAlphaModFloat(SDL_Texture *texture, float *alpha);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **texture**     | the texture to query                             |
| **alpha**       | a pointer filled in with the current alpha value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod)
* [SDL_GetTextureColorModFloat](SDL_GetTextureColorModFloat)
* [SDL_SetTextureAlphaModFloat](SDL_SetTextureAlphaModFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

