###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Texture

An efficient driver-specific representation of pixel data

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
struct SDL_Texture
{
    SDL_PixelFormat format;     /**< The format of the texture, read-only */
    int w;                      /**< The width of the texture, read-only. */
    int h;                      /**< The height of the texture, read-only. */

    int refcount;               /**< Application reference count, used when freeing texture */
};
```

## Version

This struct is available since SDL 3.1.3.

## See Also

- [SDL_CreateTexture](SDL_CreateTexture)
- [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)
- [SDL_CreateTextureWithProperties](SDL_CreateTextureWithProperties)
- [SDL_DestroyTexture](SDL_DestroyTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRender](CategoryRender)

