###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateNVTexture

Update a rectangle within a planar NV12 or NV21 texture with new pixels.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_UpdateNVTexture(SDL_Texture * texture,
                         const SDL_Rect * rect,
                         const Uint8 *Yplane, int Ypitch,
                         const Uint8 *UVplane, int UVpitch);

```

## Function Parameters

|                 |                                                                                       |
| --------------- | ------------------------------------------------------------------------------------- |
| **texture**     | the texture to update                                                                 |
| **rect**        | a pointer to the rectangle of pixels to update, or NULL to update the entire texture. |
| **Yplane**      | the raw pixel data for the Y plane.                                                   |
| **Ypitch**      | the number of bytes between rows of pixel data for the Y plane.                       |
| **UVplane**     | the raw pixel data for the UV plane.                                                  |
| **UVpitch**     | the number of bytes between rows of pixel data for the UV plane.                      |

## Return Value

Return 0 on success, or -1 if the texture is not valid.

## Remarks

You can use [SDL_UpdateTexture](SDL_UpdateTexture)() as long as your pixel
data is a contiguous block of NV12/21 planes in the proper order, but this
function is available if your pixel data is not contiguous.

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


