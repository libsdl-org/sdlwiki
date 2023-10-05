###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockTexture

Lock a portion of the texture for **write-only** pixel access.

## Syntax

```c
int SDL_LockTexture(SDL_Texture * texture,
                    const SDL_Rect * rect,
                    void **pixels, int *pitch);

```

## Function Parameters

|                 |                                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to lock for access, which was created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING)   |
| **rect**        | an [SDL_Rect](SDL_Rect) structure representing the area to lock for access; NULL to lock the entire texture           |
| **pixels**      | the address of a pointer variable; that variable gets filled the start address of memory for the texture area locked, |
|                 | appropriately offset by the locked area                                                                               |
| **pitch**       | this is filled in with the pitch of the locked pixels; the pitch is the length of one row in bytes                    |

## Return Value

Returns 0 on success or a negative error code if the texture is not valid
or was not created with
[`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

As an optimization, the memory for the texture area locked doesn't receive
the previous unlocked texture area's data. This memory, pointed to by the
pointer whose address is passed as the pixels parameter, might still contain
that data but this would be by chance.

Use [SDL_UnlockTexture](SDL_UnlockTexture)() to unlock the texture area which
lets the memory pointed to by the pointer whose address is passed as the
pixels parameter get uploaded to VRAM.

**Warning**: Utilise every byte of the memory for the texture area that you
lock fully before unlocking it, otherwise the texture might have random
content.

pitch might be unequal the pixel size in bytes * width of the window from
which you created the texture, it might be larger representing that product
plus padding. Content of padding bytes are ignored by further functions. Use
y * pitch + x * pixel size in bytes to write to the first byte of the pixel
at x, y in the texture area locked.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI)

