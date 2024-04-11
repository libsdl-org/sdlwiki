###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockTexture

Lock a portion of the texture for **write-only** pixel access.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_LockTexture(SDL_Texture * texture,
                    const SDL_Rect * rect,
                    void **pixels, int *pitch);

```

## Function Parameters

|                 |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to lock for access, which was created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING) |
| **rect**        | an [SDL_Rect](SDL_Rect) structure representing the area to lock for access; NULL to lock the entire texture         |
| **pixels**      | this is filled in with a pointer to the locked pixels, appropriately offset by the locked area                      |
| **pitch**       | this is filled in with the pitch of the locked pixels; the pitch is the length of one row in bytes                  |

## Return Value

Returns 0 on success or a negative error code if the texture is not valid
or was not created with
[`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level.

You must use [SDL_UnlockTexture](SDL_UnlockTexture)() to unlock the pixels
and apply any changes.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

