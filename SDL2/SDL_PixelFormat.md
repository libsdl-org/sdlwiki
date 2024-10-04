###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_PixelFormat

A structure that contains pixel format information.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
typedef struct SDL_PixelFormat
{
    Uint32 format;
    SDL_Palette *palette;
    Uint8 BitsPerPixel;
    Uint8 BytesPerPixel;
    Uint8 padding[2];
    Uint32 Rmask;
    Uint32 Gmask;
    Uint32 Bmask;
    Uint32 Amask;
    Uint8 Rloss;
    Uint8 Gloss;
    Uint8 Bloss;
    Uint8 Aloss;
    Uint8 Rshift;
    Uint8 Gshift;
    Uint8 Bshift;
    Uint8 Ashift;
    int refcount;
    struct SDL_PixelFormat *next;
} SDL_PixelFormat;
```

## Remarks

Everything in the pixel format structure is read-only.

A pixel format has either a palette or masks. If a palette is used `Rmask`,
`Gmask`, `Bmask`, and `Amask` will be 0.

An [SDL_PixelFormat](SDL_PixelFormat) describes the format of the pixel
data stored at the `pixels` field of an [SDL_Surface](SDL_Surface). Every
surface stores an [SDL_PixelFormat](SDL_PixelFormat) in the `format` field.

If you wish to do pixel level modifications on a surface, then
understanding how SDL stores its color information is essential.

For information on modern pixel color spaces, see the following Wikipedia
article: http://en.wikipedia.org/wiki/RGBA_color_space

## See Also

- [SDL_ConvertSurface](SDL_ConvertSurface)
- [SDL_GetRGB](SDL_GetRGB)
- [SDL_GetRGBA](SDL_GetRGBA)
- [SDL_MapRGB](SDL_MapRGB)
- [SDL_MapRGBA](SDL_MapRGBA)
- [SDL_AllocFormat](SDL_AllocFormat)
- [SDL_FreeFormat](SDL_FreeFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryPixels](CategoryPixels)

