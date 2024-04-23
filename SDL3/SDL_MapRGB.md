###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MapRGB

Map an RGB triple to an opaque pixel value for a given pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
Uint32 SDL_MapRGB(const SDL_PixelFormat * format,
                  Uint8 r, Uint8 g, Uint8 b);

```

## Function Parameters

|                |                                                                             |
| -------------- | --------------------------------------------------------------------------- |
| **format**     | an [SDL_PixelFormat](SDL_PixelFormat) structure describing the pixel format |
| **r**          | the red component of the pixel in the range 0-255                           |
| **g**          | the green component of the pixel in the range 0-255                         |
| **b**          | the blue component of the pixel in the range 0-255                          |

## Return Value

Returns a pixel value

## Remarks

This function maps the RGB color value to the specified pixel format and
returns the pixel value best approximating the given RGB color value for
the given pixel format.

If the format has a palette (8-bit) the index of the closest matching color
in the palette will be returned.

If the specified pixel format has an alpha component it will be returned as
all 1 bits (fully opaque).

If the pixel format bpp (color depth) is less than 32-bpp then the unused
upper bits of the return value can safely be ignored (e.g., with a 16-bpp
format the return value can be assigned to a Uint16, and similarly a Uint8
for an 8-bpp format).

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetRGB](SDL_GetRGB)
* [SDL_GetRGBA](SDL_GetRGBA)
* [SDL_MapRGBA](SDL_MapRGBA)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)


