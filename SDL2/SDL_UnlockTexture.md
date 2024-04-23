###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockTexture

Unlock a texture, uploading the changes to video memory, if needed.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
void SDL_UnlockTexture(SDL_Texture * texture);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **texture**     | a texture locked by [SDL_LockTexture](SDL_LockTexture)() |

## Remarks

**Warning**: Please note that [SDL_LockTexture](SDL_LockTexture)() is
intended to be write-only; it will not guarantee the previous contents of
the texture will be provided. You must fully initialize any area of a
texture that you lock before unlocking it, as the pixels might otherwise be
uninitialized memory.

Which is to say: locking and immediately unlocking a texture can result in
corrupted textures, depending on the renderer in use.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_LockTexture](SDL_LockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

