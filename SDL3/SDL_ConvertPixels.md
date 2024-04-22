###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertPixels

Copy a block of pixels of one format to another format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
int SDL_ConvertPixels(int width, int height, SDL_PixelFormatEnum src_format, const void *src, int src_pitch, SDL_PixelFormatEnum dst_format, void *dst, int dst_pitch);

```

## Function Parameters

|                    |                                                                                |
| ------------------ | ------------------------------------------------------------------------------ |
| **width**          | the width of the block to copy, in pixels                                      |
| **height**         | the height of the block to copy, in pixels                                     |
| **src_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `src` pixels format |
| **src**            | a pointer to the source pixels                                                 |
| **src_pitch**      | the pitch of the source pixels, in bytes                                       |
| **dst_format**     | an [SDL_PixelFormatEnum](SDL_PixelFormatEnum) value of the `dst` pixels format |
| **dst**            | a pointer to be filled in with new pixel data                                  |
| **dst_pitch**      | the pitch of the destination pixels, in bytes                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_ConvertPixelsAndColorspace](SDL_ConvertPixelsAndColorspace)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)


