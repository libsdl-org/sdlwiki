###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockTextureToSurface

Lock a portion of the texture for **write-only** pixel access, and expose it as a SDL surface.

## Syntax

```c
int SDL_LockTextureToSurface(SDL_Texture *texture,
                    const SDL_Rect *rect,
                    SDL_Surface **surface);

```

## Function Parameters

|                 |                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to lock for access, which must be created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING) |
| **rect**        | a pointer to the rectangle to lock for access. If the rect is NULL, the entire texture will be locked                   |
| **surface**     | this is filled in with an SDL surface representing the locked area                                                      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Besides providing an [SDL_Surface](SDL_Surface) instead of raw pixel data,
this function operates like [SDL_LockTexture](SDL_LockTexture).

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level.

You must use [SDL_UnlockTexture](SDL_UnlockTexture)() to unlock the pixels
and apply any changes.

The returned surface is freed internally after calling
[SDL_UnlockTexture](SDL_UnlockTexture)() or
[SDL_DestroyTexture](SDL_DestroyTexture)(). The caller should not free it.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockTexture](SDL_LockTexture)
* [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI)

