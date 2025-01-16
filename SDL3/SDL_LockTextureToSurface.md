###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_LockTextureToSurface

Lock a portion of the texture for **write-only** pixel access, and expose it as a SDL surface.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_LockTextureToSurface(SDL_Texture *texture, const SDL_Rect *rect, SDL_Surface **surface);
```

## Function Parameters

|                               |             |                                                                                                                          |
| ----------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Texture](SDL_Texture) *  | **texture** | the texture to lock for access, which must be created with [`SDL_TEXTUREACCESS_STREAMING`](SDL_TEXTUREACCESS_STREAMING). |
| const [SDL_Rect](SDL_Rect) *  | **rect**    | a pointer to the rectangle to lock for access. If the rect is NULL, the entire texture will be locked.                   |
| [SDL_Surface](SDL_Surface) ** | **surface** | a pointer to an SDL surface of size **rect**. Don't assume any specific pixel content.                                                     |

## Return Value

(bool) Returns true on success or false on failure; call
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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_LockTexture](SDL_LockTexture)
- [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

