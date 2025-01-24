# SDL_UnlockTexture

Unlock a texture, uploading the changes to video memory, if needed.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_UnlockTexture(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                                                           |
| ---------------------------- | ----------- | --------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | a texture locked by [SDL_LockTexture](SDL_LockTexture)(). |

## Remarks

**Warning**: Please note that [SDL_LockTexture](SDL_LockTexture)() is
intended to be write-only; it will not guarantee the previous contents of
the texture will be provided. You must fully initialize any area of a
texture that you lock before unlocking it, as the pixels might otherwise be
uninitialized memory.

Which is to say: locking and immediately unlocking a texture can result in
corrupted textures, depending on the renderer in use.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockTexture](SDL_LockTexture)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

