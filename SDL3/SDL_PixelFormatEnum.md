###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PixelFormatEnum

All pixel formats known to SDL.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
typedef enum SDL_PixelFormatEnum
{
    SDL_PIXELFORMAT_UNKNOWN,
    SDL_PIXELFORMAT_INDEX1LSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX1, SDL_BITMAPORDER_4321, 0,
                               1, 0),
    SDL_PIXELFORMAT_INDEX1MSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX1, SDL_BITMAPORDER_1234, 0,
                               1, 0),
    SDL_PIXELFORMAT_INDEX2LSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX2, SDL_BITMAPORDER_4321, 0,
                               2, 0),
    SDL_PIXELFORMAT_INDEX2MSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX2, SDL_BITMAPORDER_1234, 0,
                               2, 0),
    SDL_PIXELFORMAT_INDEX4LSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX4, SDL_BITMAPORDER_4321, 0,
                               4, 0),
    SDL_PIXELFORMAT_INDEX4MSB =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX4, SDL_BITMAPORDER_1234, 0,
                               4, 0),
    SDL_PIXELFORMAT_INDEX8 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX8, 0, 0, 8, 1),
    SDL_PIXELFORMAT_RGB332 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED8, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_332, 8, 1),
    SDL_PIXELFORMAT_XRGB4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_4444, 12, 2),
    SDL_PIXELFORMAT_RGB444 = SDL_PIXELFORMAT_XRGB4444,
    SDL_PIXELFORMAT_XBGR4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XBGR,
                               SDL_PACKEDLAYOUT_4444, 12, 2),
    SDL_PIXELFORMAT_BGR444 = SDL_PIXELFORMAT_XBGR4444,
    SDL_PIXELFORMAT_XRGB1555 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_1555, 15, 2),
    SDL_PIXELFORMAT_RGB555 = SDL_PIXELFORMAT_XRGB1555,
    SDL_PIXELFORMAT_XBGR1555 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XBGR,
                               SDL_PACKEDLAYOUT_1555, 15, 2),
    SDL_PIXELFORMAT_BGR555 = SDL_PIXELFORMAT_XBGR1555,
    SDL_PIXELFORMAT_ARGB4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ARGB,
                               SDL_PACKEDLAYOUT_4444, 16, 2),
    SDL_PIXELFORMAT_RGBA4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_RGBA,
                               SDL_PACKEDLAYOUT_4444, 16, 2),
    SDL_PIXELFORMAT_ABGR4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ABGR,
                               SDL_PACKEDLAYOUT_4444, 16, 2),
    SDL_PIXELFORMAT_BGRA4444 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_BGRA,
                               SDL_PACKEDLAYOUT_4444, 16, 2),
    SDL_PIXELFORMAT_ARGB1555 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ARGB,
                               SDL_PACKEDLAYOUT_1555, 16, 2),
    SDL_PIXELFORMAT_RGBA5551 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_RGBA,
                               SDL_PACKEDLAYOUT_5551, 16, 2),
    SDL_PIXELFORMAT_ABGR1555 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ABGR,
                               SDL_PACKEDLAYOUT_1555, 16, 2),
    SDL_PIXELFORMAT_BGRA5551 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_BGRA,
                               SDL_PACKEDLAYOUT_5551, 16, 2),
    SDL_PIXELFORMAT_RGB565 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_565, 16, 2),
    SDL_PIXELFORMAT_BGR565 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XBGR,
                               SDL_PACKEDLAYOUT_565, 16, 2),
    SDL_PIXELFORMAT_RGB24 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU8, SDL_ARRAYORDER_RGB, 0,
                               24, 3),
    SDL_PIXELFORMAT_BGR24 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU8, SDL_ARRAYORDER_BGR, 0,
                               24, 3),
    SDL_PIXELFORMAT_XRGB8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_8888, 24, 4),
    SDL_PIXELFORMAT_RGBX8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_RGBX,
                               SDL_PACKEDLAYOUT_8888, 24, 4),
    SDL_PIXELFORMAT_XBGR8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XBGR,
                               SDL_PACKEDLAYOUT_8888, 24, 4),
    SDL_PIXELFORMAT_BGRX8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_BGRX,
                               SDL_PACKEDLAYOUT_8888, 24, 4),
    SDL_PIXELFORMAT_ARGB8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ARGB,
                               SDL_PACKEDLAYOUT_8888, 32, 4),
    SDL_PIXELFORMAT_RGBA8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_RGBA,
                               SDL_PACKEDLAYOUT_8888, 32, 4),
    SDL_PIXELFORMAT_ABGR8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ABGR,
                               SDL_PACKEDLAYOUT_8888, 32, 4),
    SDL_PIXELFORMAT_BGRA8888 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_BGRA,
                               SDL_PACKEDLAYOUT_8888, 32, 4),
    SDL_PIXELFORMAT_XRGB2101010 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XRGB,
                               SDL_PACKEDLAYOUT_2101010, 32, 4),
    SDL_PIXELFORMAT_XBGR2101010 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XBGR,
                               SDL_PACKEDLAYOUT_2101010, 32, 4),
    SDL_PIXELFORMAT_ARGB2101010 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ARGB,
                               SDL_PACKEDLAYOUT_2101010, 32, 4),
    SDL_PIXELFORMAT_ABGR2101010 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ABGR,
                               SDL_PACKEDLAYOUT_2101010, 32, 4),
    SDL_PIXELFORMAT_RGB48 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_RGB, 0,
                               48, 6),
    SDL_PIXELFORMAT_BGR48 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_BGR, 0,
                               48, 6),
    SDL_PIXELFORMAT_RGBA64 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_RGBA, 0,
                               64, 8),
    SDL_PIXELFORMAT_ARGB64 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_ARGB, 0,
                               64, 8),
    SDL_PIXELFORMAT_BGRA64 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_BGRA, 0,
                               64, 8),
    SDL_PIXELFORMAT_ABGR64 =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU16, SDL_ARRAYORDER_ABGR, 0,
                               64, 8),
    SDL_PIXELFORMAT_RGB48_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_RGB, 0,
                               48, 6),
    SDL_PIXELFORMAT_BGR48_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_BGR, 0,
                               48, 6),
    SDL_PIXELFORMAT_RGBA64_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_RGBA, 0,
                               64, 8),
    SDL_PIXELFORMAT_ARGB64_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_ARGB, 0,
                               64, 8),
    SDL_PIXELFORMAT_BGRA64_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_BGRA, 0,
                               64, 8),
    SDL_PIXELFORMAT_ABGR64_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF16, SDL_ARRAYORDER_ABGR, 0,
                               64, 8),
    SDL_PIXELFORMAT_RGB96_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_RGB, 0,
                               96, 12),
    SDL_PIXELFORMAT_BGR96_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_BGR, 0,
                               96, 12),
    SDL_PIXELFORMAT_RGBA128_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_RGBA, 0,
                               128, 16),
    SDL_PIXELFORMAT_ARGB128_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_ARGB, 0,
                               128, 16),
    SDL_PIXELFORMAT_BGRA128_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_BGRA, 0,
                               128, 16),
    SDL_PIXELFORMAT_ABGR128_FLOAT =
        SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYF32, SDL_ARRAYORDER_ABGR, 0,
                               128, 16),

    /* Aliases for RGBA byte arrays of color data, for the current platform */
#if SDL_BYTEORDER == SDL_BIG_ENDIAN
    SDL_PIXELFORMAT_RGBA32 = SDL_PIXELFORMAT_RGBA8888,
    SDL_PIXELFORMAT_ARGB32 = SDL_PIXELFORMAT_ARGB8888,
    SDL_PIXELFORMAT_BGRA32 = SDL_PIXELFORMAT_BGRA8888,
    SDL_PIXELFORMAT_ABGR32 = SDL_PIXELFORMAT_ABGR8888,
    SDL_PIXELFORMAT_RGBX32 = SDL_PIXELFORMAT_RGBX8888,
    SDL_PIXELFORMAT_XRGB32 = SDL_PIXELFORMAT_XRGB8888,
    SDL_PIXELFORMAT_BGRX32 = SDL_PIXELFORMAT_BGRX8888,
    SDL_PIXELFORMAT_XBGR32 = SDL_PIXELFORMAT_XBGR8888,
#else
    SDL_PIXELFORMAT_RGBA32 = SDL_PIXELFORMAT_ABGR8888,
    SDL_PIXELFORMAT_ARGB32 = SDL_PIXELFORMAT_BGRA8888,
    SDL_PIXELFORMAT_BGRA32 = SDL_PIXELFORMAT_ARGB8888,
    SDL_PIXELFORMAT_ABGR32 = SDL_PIXELFORMAT_RGBA8888,
    SDL_PIXELFORMAT_RGBX32 = SDL_PIXELFORMAT_XBGR8888,
    SDL_PIXELFORMAT_XRGB32 = SDL_PIXELFORMAT_BGRX8888,
    SDL_PIXELFORMAT_BGRX32 = SDL_PIXELFORMAT_XRGB8888,
    SDL_PIXELFORMAT_XBGR32 = SDL_PIXELFORMAT_RGBX8888,
#endif

    SDL_PIXELFORMAT_YV12 =      /**< Planar mode: Y + V + U  (3 planes) */
        SDL_DEFINE_PIXELFOURCC('Y', 'V', '1', '2'),
    SDL_PIXELFORMAT_IYUV =      /**< Planar mode: Y + U + V  (3 planes) */
        SDL_DEFINE_PIXELFOURCC('I', 'Y', 'U', 'V'),
    SDL_PIXELFORMAT_YUY2 =      /**< Packed mode: Y0+U0+Y1+V0 (1 plane) */
        SDL_DEFINE_PIXELFOURCC('Y', 'U', 'Y', '2'),
    SDL_PIXELFORMAT_UYVY =      /**< Packed mode: U0+Y0+V0+Y1 (1 plane) */
        SDL_DEFINE_PIXELFOURCC('U', 'Y', 'V', 'Y'),
    SDL_PIXELFORMAT_YVYU =      /**< Packed mode: Y0+V0+Y1+U0 (1 plane) */
        SDL_DEFINE_PIXELFOURCC('Y', 'V', 'Y', 'U'),
    SDL_PIXELFORMAT_NV12 =      /**< Planar mode: Y + U/V interleaved  (2 planes) */
        SDL_DEFINE_PIXELFOURCC('N', 'V', '1', '2'),
    SDL_PIXELFORMAT_NV21 =      /**< Planar mode: Y + V/U interleaved  (2 planes) */
        SDL_DEFINE_PIXELFOURCC('N', 'V', '2', '1'),
    SDL_PIXELFORMAT_P010 =      /**< Planar mode: Y + U/V interleaved  (2 planes) */
        SDL_DEFINE_PIXELFOURCC('P', '0', '1', '0'),
    SDL_PIXELFORMAT_EXTERNAL_OES =      /**< Android video texture format */
        SDL_DEFINE_PIXELFOURCC('O', 'E', 'S', ' ')
} SDL_PixelFormatEnum;
```

## Remarks

SDL's pixel formats have the following naming convention:

- Names with a list of components and a single bit count, such as RGB24 and
  ABGR32, define a platform-independent encoding into bytes in the order
  specified. For example, in RGB24 data, each pixel is encoded in 3 bytes
  (red, green, blue) in that order, and in ABGR32 data, each pixel is
  encoded in 4 bytes alpha, blue, green, red) in that order. Use these
  names if the property of a format that is important to you is the order
  of the bytes in memory or on disk.
- Names with a bit count per component, such as ARGB8888 and XRGB1555, are
  "packed" into an appropriately-sized integer in the platform's native
  endianness. For example, ARGB8888 is a sequence of 32-bit integers; in
  each integer, the most significant bits are alpha, and the least
  significant bits are blue. On a little-endian CPU such as x86, the least
  significant bits of each integer are arranged first in memory, but on a
  big-endian CPU such as s390x, the most significant bits are arranged
  first. Use these names if the property of a format that is important to
  you is the meaning of each bit position within a native-endianness
  integer.
- In indexed formats such as INDEX4LSB, each pixel is represented by
  encoding an index into the palette into the indicated number of bits,
  with multiple pixels packed into each byte if appropriate. In LSB
  formats, the first (leftmost) pixel is stored in the least-significant
  bits of the byte; in MSB formats, it's stored in the most-significant
  bits. INDEX8 does not need LSB/MSB variants, because each pixel exactly
  fills one byte.

The 32-bit byte-array encodings such as RGBA32 are aliases for the
appropriate 8888 encoding for the current platform. For example, RGBA32 is
an alias for ABGR8888 on little-endian CPUs like x86, or an alias for
RGBA8888 on big-endian CPUs.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

