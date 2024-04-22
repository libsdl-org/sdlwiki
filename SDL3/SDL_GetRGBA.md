###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRGBA

Get RGBA values from a pixel in the specified format.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
void SDL_GetRGBA(Uint32 pixel,
                 const SDL_PixelFormat * format,
                 Uint8 * r, Uint8 * g, Uint8 * b,
                 Uint8 * a);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **pixel**      | a pixel value                                                                      |
| **format**     | an [SDL_PixelFormat](SDL_PixelFormat) structure describing the format of the pixel |
| **r**          | a pointer filled in with the red component                                         |
| **g**          | a pointer filled in with the green component                                       |
| **b**          | a pointer filled in with the blue component                                        |
| **a**          | a pointer filled in with the alpha component                                       |

## Remarks

This function uses the entire 8-bit [0..255] range when converting color
components from pixel formats with less than 8-bits per RGB component
(e.g., a completely white pixel in 16-bit RGB565 format would return [0xff,
0xff, 0xff] not [0xf8, 0xfc, 0xf8]).

If the surface has no alpha component, the alpha will be returned as 0xff
(100% opaque).

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetRGB](SDL_GetRGB)
* [SDL_MapRGB](SDL_MapRGB)
* [SDL_MapRGBA](SDL_MapRGBA)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)


