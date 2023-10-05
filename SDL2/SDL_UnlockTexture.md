###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockTexture

Unlock a texture, uploading the changes to video memory, if needed.

## Syntax

```c
void SDL_UnlockTexture(SDL_Texture * texture);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **texture**     | a texture locked by [SDL_LockTexture](SDL_LockTexture)() |

## Remarks

The memory for the texture area locked, which is pointed to by the pointer
whose address is provided to [SDL_LockTexture](SDL_LockTexture)() as the
pixels parameter, is freed by this function! If you want a copy of the
texture data, keep such one at your application level.

**Warning**: locking and immediately unlocking a texture can result in
corrupted textures, depending on the renderer in use.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LockTexture](SDL_LockTexture)

----
[CategoryAPI](CategoryAPI)

