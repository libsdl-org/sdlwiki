###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockTexture

Lock a portion of the texture for **write-only** pixel access.

## Syntax

```c
int SDL_LockTexture(SDL_Texture *texture,
                    const SDL_Rect *rect,
                    void **pixels, int *pitch);

```

## Function Parameters

|                 |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to lock for access, which was created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING) |
| **rect**        | an [SDL_Rect](SDL_Rect.md) structure representing the area to lock for access; NULL to lock the entire texture         |
| **pixels**      | this is filled in with a pointer to the locked pixels, appropriately offset by the locked area                      |
| **pitch**       | this is filled in with the pitch of the locked pixels; the pitch is the length of one row in bytes                  |

## Return Value

Returns 0 on success or a negative error code if the texture is not valid
or was not created with
[`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING); call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level.

You must use [SDL_UnlockTexture](SDL_UnlockTexture.md)() to unlock the pixels
and apply any changes.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_UnlockTexture](SDL_UnlockTexture.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
