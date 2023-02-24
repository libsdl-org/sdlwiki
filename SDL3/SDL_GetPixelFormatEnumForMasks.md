###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPixelFormatEnumForMasks

Convert a bpp value and RGBA masks to an enumerated pixel format.

## Syntax

```c
Uint32 SDL_GetPixelFormatEnumForMasks(int bpp,
                                  Uint32 Rmask,
                                  Uint32 Gmask,
                                  Uint32 Bmask,
                                  Uint32 Amask);

```

## Function Parameters

|               |                                               |
| ------------- | --------------------------------------------- |
| **bpp**       | a bits per pixel value; usually 15, 16, or 32 |
| **Rmask**     | the red mask for the format                   |
| **Gmask**     | the green mask for the format                 |
| **Bmask**     | the blue mask for the format                  |
| **Amask**     | the alpha mask for the format                 |

## Return Value

Returns one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values

## Remarks

This will return [`SDL_PIXELFORMAT_UNKNOWN`](SDL_PIXELFORMAT_UNKNOWN) if
the conversion wasn't possible.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetMasksForPixelFormatEnum](SDL_GetMasksForPixelFormatEnum)

----
[CategoryAPI](CategoryAPI)

