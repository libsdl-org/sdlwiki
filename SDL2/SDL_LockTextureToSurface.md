###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockTextureToSurface

Lock a portion of the texture for **write-only** pixel access, and expose it as a SDL surface.

## Syntax

```c
int SDL_LockTextureToSurface(SDL_Texture *texture,
                    const SDL_Rect *rect,
                    SDL_Surface **surface);

```

## Function Parameters

|                 |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to lock for access, which was created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING) |
| **rect**        | a pointer to the rectangle to lock for access. If the rect is NULL, the entire texture will be locked               |
| **surface**     | this is filled in with an SDL surface representing the locked area                                                  |

## Return Value

Returns 0 on success, or -1 if the texture is not valid or was not created
with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING)

## Remarks

Besides providing an [SDL_Surface](SDL_Surface.md) instead of raw pixel data,
this function operates like [SDL_LockTexture](SDL_LockTexture.md).

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level.

You must use [SDL_UnlockTexture](SDL_UnlockTexture.md)() to unlock the pixels
and apply any changes.

The returned surface is freed internally after calling
[SDL_UnlockTexture](SDL_UnlockTexture.md)() or
[SDL_DestroyTexture](SDL_DestroyTexture.md)(). The caller should not free it.

## Version

This function is available since SDL 2.0.12.

## Related Functions

* [SDL_LockTexture](SDL_LockTexture.md)
* [SDL_UnlockTexture](SDL_UnlockTexture.md)

----
[CategoryAPI](CategoryAPI.md)
