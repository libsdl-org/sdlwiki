# SDL_UpdateTexture

Update the given texture rectangle with new pixel data.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_UpdateTexture(SDL_Texture *texture, const SDL_Rect *rect, const void *pixels, int pitch);
```

## Function Parameters

|                              |             |                                                                                                          |
| ---------------------------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                                                                   |
| const [SDL_Rect](SDL_Rect) * | **rect**    | an [SDL_Rect](SDL_Rect) structure representing the area to update, or NULL to update the entire texture. |
| const void *                 | **pixels**  | the raw pixel data in the format of the texture.                                                         |
| int                          | **pitch**   | the number of bytes in a row of pixel data, including padding between lines.                             |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The pixel data must be in the pixel format of the texture, which can be
queried using the
[SDL_PROP_TEXTURE_FORMAT_NUMBER](SDL_PROP_TEXTURE_FORMAT_NUMBER) property.

This is a fairly slow function, intended for use with static textures that
do not change often.

If the texture is intended to be updated often, it is preferred to create
the texture as streaming and use the locking functions referenced below.
While this function will work with streaming textures, for optimization
reasons you may not get the pixels back if you lock the texture afterward.

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

- [SDL_LockTexture](SDL_LockTexture)
- [SDL_UnlockTexture](SDL_UnlockTexture)
- [SDL_UpdateNVTexture](SDL_UpdateNVTexture)
- [SDL_UpdateYUVTexture](SDL_UpdateYUVTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

