###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyTexture

Destroy the specified texture.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_DestroyTexture(SDL_Texture *texture);

```

## Function Parameters

|                 |                        |
| --------------- | ---------------------- |
| **texture**     | the texture to destroy |

## Remarks

Passing NULL or an otherwise invalid texture will set the SDL error message
to "Invalid texture".

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


