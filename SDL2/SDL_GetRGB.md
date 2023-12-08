###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRGB

Get RGB values from a pixel in the specified format.

## Syntax

```c
void SDL_GetRGB(Uint32 pixel,
                const SDL_PixelFormat * format,
                Uint8 * r, Uint8 * g, Uint8 * b);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **pixel**      | a pixel value                                                                      |
| **format**     | an [SDL_PixelFormat](SDL_PixelFormat.md) structure describing the format of the pixel |
| **r**          | a pointer filled in with the red component                                         |
| **g**          | a pointer filled in with the green component                                       |
| **b**          | a pointer filled in with the blue component                                        |

## Remarks

This function uses the entire 8-bit [0..255] range when converting color
components from pixel formats with less than 8-bits per RGB component
(e.g., a completely white pixel in 16-bit RGB565 format would return [0xff,
0xff, 0xff] not [0xf8, 0xfc, 0xf8]).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRGBA](SDL_GetRGBA.md)
* [SDL_MapRGB](SDL_MapRGB.md)
* [SDL_MapRGBA](SDL_MapRGBA.md)

----
[CategoryAPI](CategoryAPI.md)
