###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockTexture

Unlock a texture, uploading the changes to video memory, if needed.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_UnlockTexture(SDL_Texture *texture);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockTexture](SDL_LockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender)


