# SDL_MapRGBA

Map an RGBA quadruple to a pixel value for a given pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
Uint32 SDL_MapRGBA(const SDL_PixelFormatDetails *format, const SDL_Palette *palette, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
```

## Function Parameters

|                                                          |             |                                                                                            |
| -------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------ |
| const [SDL_PixelFormatDetails](SDL_PixelFormatDetails) * | **format**  | a pointer to [SDL_PixelFormatDetails](SDL_PixelFormatDetails) describing the pixel format. |
| const [SDL_Palette](SDL_Palette) *                       | **palette** | an optional palette for indexed formats, may be NULL.                                      |
| Uint8                                                    | **r**       | the red component of the pixel in the range 0-255.                                         |
| Uint8                                                    | **g**       | the green component of the pixel in the range 0-255.                                       |
| Uint8                                                    | **b**       | the blue component of the pixel in the range 0-255.                                        |
| Uint8                                                    | **a**       | the alpha component of the pixel in the range 0-255.                                       |

## Return Value

([Uint32](Uint32)) Returns a pixel value.

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
format the return value can be assigned to a [Uint16](Uint16), and
similarly a Uint8 for an 8-bpp format).

## Thread Safety

It is safe to call this function from any thread, as long as the palette is
not modified.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetPixelFormatDetails](SDL_GetPixelFormatDetails)
- [SDL_GetRGBA](SDL_GetRGBA)
- [SDL_MapRGB](SDL_MapRGB)
- [SDL_MapSurfaceRGBA](SDL_MapSurfaceRGBA)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

