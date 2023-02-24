###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyTexture

Destroy the specified texture.

## Syntax

```c
void SDL_DestroyTexture(SDL_Texture * texture);

```

## Function Parameters

|                 |                        |
| --------------- | ---------------------- |
| **texture**     | the texture to destroy |

## Remarks

Passing NULL or an otherwise invalid texture will set the SDL error message
to "Invalid texture".

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)

----
[CategoryAPI](CategoryAPI)

