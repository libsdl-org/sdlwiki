###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateYUVTexture

Update a rectangle within a planar YV12 or IYUV texture with new pixel data.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_UpdateYUVTexture(SDL_Texture * texture,
                         const SDL_Rect * rect,
                         const Uint8 *Yplane, int Ypitch,
                         const Uint8 *Uplane, int Upitch,
                         const Uint8 *Vplane, int Vpitch);

```

## Function Parameters

|                 |                                                                                      |
| --------------- | ------------------------------------------------------------------------------------ |
| **texture**     | the texture to update                                                                |
| **rect**        | a pointer to the rectangle of pixels to update, or NULL to update the entire texture |
| **Yplane**      | the raw pixel data for the Y plane                                                   |
| **Ypitch**      | the number of bytes between rows of pixel data for the Y plane                       |
| **Uplane**      | the raw pixel data for the U plane                                                   |
| **Upitch**      | the number of bytes between rows of pixel data for the U plane                       |
| **Vplane**      | the raw pixel data for the V plane                                                   |
| **Vpitch**      | the number of bytes between rows of pixel data for the V plane                       |

## Return Value

Returns 0 on success or -1 if the texture is not valid; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can use [SDL_UpdateTexture](SDL_UpdateTexture)() as long as your pixel
data is a contiguous block of Y and U/V planes in the proper order, but
this function is available if your pixel data is not contiguous.

## Version

This function is available since SDL 2.0.1.

## Related Functions

* [SDL_UpdateTexture](SDL_UpdateTexture)

----
[CategoryAPI](CategoryAPI)

