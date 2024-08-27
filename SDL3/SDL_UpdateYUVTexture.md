###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateYUVTexture

Update a rectangle within a planar YV12 or IYUV texture with new pixel data.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_UpdateYUVTexture(SDL_Texture *texture,
                     const SDL_Rect *rect,
                     const Uint8 *Yplane, int Ypitch,
                     const Uint8 *Uplane, int Upitch,
                     const Uint8 *Vplane, int Vpitch);
```

## Function Parameters

|                              |             |                                                                                       |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to update.                                                                |
| const [SDL_Rect](SDL_Rect) * | **rect**    | a pointer to the rectangle of pixels to update, or NULL to update the entire texture. |
| const Uint8 *                | **Yplane**  | the raw pixel data for the Y plane.                                                   |
| int                          | **Ypitch**  | the number of bytes between rows of pixel data for the Y plane.                       |
| const Uint8 *                | **Uplane**  | the raw pixel data for the U plane.                                                   |
| int                          | **Upitch**  | the number of bytes between rows of pixel data for the U plane.                       |
| const Uint8 *                | **Vplane**  | the raw pixel data for the V plane.                                                   |
| int                          | **Vpitch**  | the number of bytes between rows of pixel data for the V plane.                       |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

You can use [SDL_UpdateTexture](SDL_UpdateTexture)() as long as your pixel
data is a contiguous block of Y and U/V planes in the proper order, but
this function is available if your pixel data is not contiguous.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UpdateNVTexture](SDL_UpdateNVTexture)
- [SDL_UpdateTexture](SDL_UpdateTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

