###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MapRGBA

Map an RGBA quadruple to a pixel value for a given pixel format.

## Syntax

```c
Uint32 SDL_MapRGBA(const SDL_PixelFormat * format,
                   Uint8 r, Uint8 g, Uint8 b,
                   Uint8 a);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **format**     | an [SDL_PixelFormat](SDL_PixelFormat.md) structure describing the format of the pixel |
| **r**          | the red component of the pixel in the range 0-255                                  |
| **g**          | the green component of the pixel in the range 0-255                                |
| **b**          | the blue component of the pixel in the range 0-255                                 |
| **a**          | the alpha component of the pixel in the range 0-255                                |

## Return Value

Returns a pixel value

## Remarks

This function maps the RGBA color value to the specified pixel format and
returns the pixel value best approximating the given RGBA color value for
the given pixel format.

If the specified pixel format has no alpha component the alpha value will
be ignored (as it will be in formats with a palette).

If the format has a palette (8-bit) the index of the closest matching color
in the palette will be returned.

If the pixel format bpp (color depth) is less than 32-bpp then the unused
upper bits of the return value can safely be ignored (e.g., with a 16-bpp
format the return value can be assigned to a Uint16, and similarly a Uint8
for an 8-bpp format).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRGB](SDL_GetRGB.md)
* [SDL_GetRGBA](SDL_GetRGBA.md)
* [SDL_MapRGB](SDL_MapRGB.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryPixels](CategoryPixels.md)
