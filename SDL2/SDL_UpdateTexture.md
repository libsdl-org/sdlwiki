###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateTexture

Update the given texture rectangle with new pixel data.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_UpdateTexture(SDL_Texture * texture,
                      const SDL_Rect * rect,
                      const void *pixels, int pitch);

```

## Function Parameters

|                 |                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| **texture**     | the texture to update                                                                                   |
| **rect**        | an [SDL_Rect](SDL_Rect) structure representing the area to update, or NULL to update the entire texture |
| **pixels**      | the raw pixel data in the format of the texture                                                         |
| **pitch**       | the number of bytes in a row of pixel data, including padding between lines                             |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The pixel data must be in the pixel format of the texture. Use
[SDL_QueryTexture](SDL_QueryTexture)() to query the pixel format of the
texture.

This is a fairly slow function, intended for use with static textures that
do not change often.

If the texture is intended to be updated often, it is preferred to create
the texture as streaming and use the locking functions referenced below.
While this function will work with streaming textures, for optimization
reasons you may not get the pixels back if you lock the texture afterward.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_LockTexture](SDL_LockTexture)
* [SDL_UnlockTexture](SDL_UnlockTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


