###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateNVTexture

Update a rectangle within a planar NV12 or NV21 texture with new pixels.

## Syntax

```c
int SDL_UpdateNVTexture(SDL_Texture *texture,
                         const SDL_Rect *rect,
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

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can use [SDL_UpdateTexture](SDL_UpdateTexture)() as long as your pixel
data is a contiguous block of NV12/21 planes in the proper order, but this
function is available if your pixel data is not contiguous.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

