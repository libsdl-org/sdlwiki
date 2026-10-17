# SDL_LockTexture

Lock a portion of the texture for **write-only** pixel access.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_LockTexture(SDL_Texture *texture,
                const SDL_Rect *rect,
                void **pixels, int *pitch);
```

## Function Parameters

|                              |             |                                                                                                                      |
| ---------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to lock for access, which was created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING). |
| const [SDL_Rect](SDL_Rect) * | **rect**    | an [SDL_Rect](SDL_Rect) structure representing the area to lock for access; NULL to lock the entire texture.         |
| void **                      | **pixels**  | this is filled in with a pointer to the locked pixels, appropriately offset by the locked area.                      |
| int *                        | **pitch**   | this is filled in with the pitch of the locked pixels; the pitch is the length of one row in bytes.                  |

## Return Value

(bool) Returns true on success or false if the texture is not valid or was
not created with
[`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level.

You must use [SDL_UnlockTexture](SDL_UnlockTexture)() to unlock the pixels
and apply any changes.

*Note on SDL_LockTexture vs SDL_UpdateTexture:*
On the software renderer, you can write directly to the final destination
with SDL_LockTexture, whereas SDL_UpdateTexture will need to make a copy
from your buffer to SDL's.
On the other renderers, it's probably the same (the GLES2 renderer, for
example, literally just calls SDL_UpdateTexture for its SDL_UnlockTexture
implementation)... but if you ever need a software renderer, this is the
thing that would benefit most from texture locking.
But in real life, with actual GPUs, it doesn't really matter a whole lot.


## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockTextureToSurface](SDL_LockTextureToSurface)
- [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

