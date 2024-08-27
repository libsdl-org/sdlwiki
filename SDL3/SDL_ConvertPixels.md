###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertPixels

Copy a block of pixels of one format to another format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_ConvertPixels(int width, int height, SDL_PixelFormat src_format, const void *src, int src_pitch, SDL_PixelFormat dst_format, void *dst, int dst_pitch);
```

## Function Parameters

|                                    |                |                                                                         |
| ---------------------------------- | -------------- | ----------------------------------------------------------------------- |
| int                                | **width**      | the width of the block to copy, in pixels.                              |
| int                                | **height**     | the height of the block to copy, in pixels.                             |
| [SDL_PixelFormat](SDL_PixelFormat) | **src_format** | an [SDL_PixelFormat](SDL_PixelFormat) value of the `src` pixels format. |
| const void *                       | **src**        | a pointer to the source pixels.                                         |
| int                                | **src_pitch**  | the pitch of the source pixels, in bytes.                               |
| [SDL_PixelFormat](SDL_PixelFormat) | **dst_format** | an [SDL_PixelFormat](SDL_PixelFormat) value of the `dst` pixels format. |
| void *                             | **dst**        | a pointer to be filled in with new pixel data.                          |
| int                                | **dst_pitch**  | the pitch of the destination pixels, in bytes.                          |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_FALSE](SDL_FALSE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ConvertPixelsAndColorspace](SDL_ConvertPixelsAndColorspace)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

