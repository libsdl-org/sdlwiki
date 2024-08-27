###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PremultiplyAlpha

Premultiply the alpha on a block of pixels.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_PremultiplyAlpha(int width, int height, SDL_PixelFormat src_format, const void *src, int src_pitch, SDL_PixelFormat dst_format, void *dst, int dst_pitch, SDL_bool linear);
```

## Function Parameters

|                                    |                |                                                                                                                                                    |
| ---------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| int                                | **width**      | the width of the block to convert, in pixels.                                                                                                      |
| int                                | **height**     | the height of the block to convert, in pixels.                                                                                                     |
| [SDL_PixelFormat](SDL_PixelFormat) | **src_format** | an [SDL_PixelFormat](SDL_PixelFormat) value of the `src` pixels format.                                                                            |
| const void *                       | **src**        | a pointer to the source pixels.                                                                                                                    |
| int                                | **src_pitch**  | the pitch of the source pixels, in bytes.                                                                                                          |
| [SDL_PixelFormat](SDL_PixelFormat) | **dst_format** | an [SDL_PixelFormat](SDL_PixelFormat) value of the `dst` pixels format.                                                                            |
| void *                             | **dst**        | a pointer to be filled in with premultiplied pixel data.                                                                                           |
| int                                | **dst_pitch**  | the pitch of the destination pixels, in bytes.                                                                                                     |
| [SDL_bool](SDL_bool)               | **linear**     | [SDL_TRUE](SDL_TRUE) to convert from sRGB to linear space for the alpha multiplication, [SDL_FALSE](SDL_FALSE) to do multiplication in sRGB space. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This is safe to use with src == dst, but not for other overlapping areas.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

