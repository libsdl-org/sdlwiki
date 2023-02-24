###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PremultiplyAlpha

Premultiply the alpha on a block of pixels.

## Syntax

```c
int SDL_PremultiplyAlpha(int width, int height,
                         Uint32 src_format,
                         const void *src, int src_pitch,
                         Uint32 dst_format,
                         void *dst, int dst_pitch);

```

## Function Parameters

|                    |                                                                                |
| ------------------ | ------------------------------------------------------------------------------ |
| **width**          | the width of the block to convert, in pixels                                   |
| **height**         | the height of the block to convert, in pixels                                  |
| **src_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `src` pixels format |
| **src**            | a pointer to the source pixels                                                 |
| **src_pitch**      | the pitch of the source pixels, in bytes                                       |
| **dst_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `dst` pixels format |
| **dst**            | a pointer to be filled in with premultiplied pixel data                        |
| **dst_pitch**      | the pitch of the destination pixels, in bytes                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is safe to use with src == dst, but not for other overlapping areas.

This function is currently only implemented for
[SDL_PIXELFORMAT_ARGB8888](SDL_PIXELFORMAT_ARGB8888).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

