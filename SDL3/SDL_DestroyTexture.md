###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyTexture

Destroy the specified texture.

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

* [SDL_CreateTexture](SDL_CreateTexture.md)
* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
