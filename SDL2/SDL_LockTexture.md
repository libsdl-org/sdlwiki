# SDL_LockTexture

Lock a portion of the texture for **write-only** pixel access.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_LockTexture(SDL_Texture * texture,
                    const SDL_Rect * rect,
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

(int) Returns 0 on success or a negative error code if the texture is not
valid or was not created with
[`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

As an optimization, the pixels made available for editing don't necessarily
contain the old texture data. This is a write-only operation, and if you
need to keep a copy of the texture data you should do that at the
application level. If the existing texture contents happen to be in the
locked buffer, it is purely coincidental.

You must use [SDL_UnlockTexture](SDL_UnlockTexture)() to unlock the pixels
and apply any changes.

Every pixel must be initialized by the caller, or uninitialized data will
be uploaded to the texture during unlock.

`pitch` may be larger than the bytes needed for a row of pixels, as there
might be padding included. Use `(y * pitch) + (x * pixel_size_in_bytes)` to
write to the first byte of the pixel at `(x, y)` in the locked texture
area, where `(0, 0)` is the top-left corner of the area.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

