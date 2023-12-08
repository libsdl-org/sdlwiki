###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ConvertPixels

Copy a block of pixels of one format to another format.

## Syntax

```c
int SDL_ConvertPixels(int width, int height,
                      Uint32 src_format,
                      const void * src, int src_pitch,
                      Uint32 dst_format,
                      void * dst, int dst_pitch);

```

## Function Parameters

|                    |                                                                                |
| ------------------ | ------------------------------------------------------------------------------ |
| **width**          | the width of the block to copy, in pixels                                      |
| **height**         | the height of the block to copy, in pixels                                     |
| **src_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum.md) value of the `src` pixels format |
| **src**            | a pointer to the source pixels                                                 |
| **src_pitch**      | the pitch of the source pixels, in bytes                                       |
| **dst_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum.md) value of the `dst` pixels format |
| **dst**            | a pointer to be filled in with new pixel data                                  |
| **dst_pitch**      | the pitch of the destination pixels, in bytes                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
