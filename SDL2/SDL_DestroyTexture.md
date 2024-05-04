###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyTexture

Destroy the specified texture.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

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

Destroying a texture during the same frame in which it's being utilized flushes the GPU command queue, which is a very slow operation. If you want to destroy a texture that you created for a particular frame, consider calling this after SDL_RenderPresent().

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

