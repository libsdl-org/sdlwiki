###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertPixelsAndColorspace

Copy a block of pixels of one format and colorspace to another format and colorspace.

## Syntax

```c
int SDL_ConvertPixelsAndColorspace(int width, int height, Uint32 src_format, SDL_Colorspace src_colorspace, const void *src, int src_pitch, Uint32 dst_format, SDL_Colorspace dst_colorspace, void *dst, int dst_pitch);

```

## Function Parameters

|                        |                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **width**              | the width of the block to copy, in pixels                                               |
| **height**             | the height of the block to copy, in pixels                                              |
| **src_format**         | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `src` pixels format          |
| **src_colorspace**     | an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace of the `src` pixels |
| **src**                | a pointer to the source pixels                                                          |
| **src_pitch**          | the pitch of the source pixels, in bytes                                                |
| **dst_format**         | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `dst` pixels format          |
| **dst_colorspace**     | an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace of the `dst` pixels |
| **dst**                | a pointer to be filled in with new pixel data                                           |
| **dst_pitch**          | the pitch of the destination pixels, in bytes                                           |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

