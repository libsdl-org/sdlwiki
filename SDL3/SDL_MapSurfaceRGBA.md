# SDL_MapSurfaceRGBA

Map an RGBA quadruple to a pixel value for a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
Uint32 SDL_MapSurfaceRGBA(SDL_Surface *surface, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
```

## Function Parameters

|                              |             |                                                      |
| ---------------------------- | ----------- | ---------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to use for the pixel format and palette. |
| Uint8                        | **r**       | the red component of the pixel in the range 0-255.   |
| Uint8                        | **g**       | the green component of the pixel in the range 0-255. |
| Uint8                        | **b**       | the blue component of the pixel in the range 0-255.  |
| Uint8                        | **a**       | the alpha component of the pixel in the range 0-255. |

## Return Value

([Uint32](Uint32)) Returns a pixel value.

## Remarks

This function maps the RGBA color value to the specified pixel format and
returns the pixel value best approximating the given RGBA color value for
the given pixel format.

If the surface pixel format has no alpha component the alpha value will be
ignored (as it will be in formats with a palette).

If the surface has a palette, the index of the closest matching color in
the palette will be returned.

If the pixel format bpp (color depth) is less than 32-bpp then the unused
upper bits of the return value can safely be ignored (e.g., with a 16-bpp
format the return value can be assigned to a [Uint16](Uint16), and
similarly a Uint8 for an 8-bpp format).

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_MapSurfaceRGB](SDL_MapSurfaceRGB)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface), [CategoryPixels](CategoryPixels)


