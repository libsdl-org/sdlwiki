###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_UpdateYUVTexture

Update a rectangle within a planar YV12 or IYUV texture with new pixel data.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_UpdateYUVTexture(SDL_Texture *texture,
                         const SDL_Rect *rect,
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

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can use [SDL_UpdateTexture](SDL_UpdateTexture)() as long as your pixel
data is a contiguous block of Y and U/V planes in the proper order, but
this function is available if your pixel data is not contiguous.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_UpdateNVTexture](SDL_UpdateNVTexture)
* [SDL_UpdateTexture](SDL_UpdateTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


