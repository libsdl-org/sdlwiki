###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertPixelsAndColorspace

Copy a block of pixels of one format and colorspace to another format and colorspace.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
int SDL_ConvertPixelsAndColorspace(int width, int height, SDL_PixelFormat src_format, SDL_Colorspace src_colorspace, SDL_PropertiesID src_properties, const void *src, int src_pitch, SDL_PixelFormat dst_format, SDL_Colorspace dst_colorspace, SDL_PropertiesID dst_properties, void *dst, int dst_pitch);
```

## Function Parameters

|                                      |                    |                                                                                             |
| ------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------- |
| int                                  | **width**          | the width of the block to copy, in pixels.                                                  |
| int                                  | **height**         | the height of the block to copy, in pixels.                                                 |
| [SDL_PixelFormat](SDL_PixelFormat)   | **src_format**     | an [SDL_PixelFormat](SDL_PixelFormat) value of the `src` pixels format.                     |
| [SDL_Colorspace](SDL_Colorspace)     | **src_colorspace** | an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace of the `src` pixels.    |
| [SDL_PropertiesID](SDL_PropertiesID) | **src_properties** | an [SDL_PropertiesID](SDL_PropertiesID) with additional source color properties, or 0.      |
| const void *                         | **src**            | a pointer to the source pixels.                                                             |
| int                                  | **src_pitch**      | the pitch of the source pixels, in bytes.                                                   |
| [SDL_PixelFormat](SDL_PixelFormat)   | **dst_format**     | an [SDL_PixelFormat](SDL_PixelFormat) value of the `dst` pixels format.                     |
| [SDL_Colorspace](SDL_Colorspace)     | **dst_colorspace** | an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace of the `dst` pixels.    |
| [SDL_PropertiesID](SDL_PropertiesID) | **dst_properties** | an [SDL_PropertiesID](SDL_PropertiesID) with additional destination color properties, or 0. |
| void *                               | **dst**            | a pointer to be filled in with new pixel data.                                              |
| int                                  | **dst_pitch**      | the pitch of the destination pixels, in bytes.                                              |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ConvertPixels](SDL_ConvertPixels)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

