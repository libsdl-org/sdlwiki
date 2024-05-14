###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SaveBMP_RW

Save a surface to a seekable SDL data stream in BMP format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_SaveBMP_RW
    (SDL_Surface * surface, SDL_RWops * dst, int freedst);

```

## Function Parameters

|                 |                                                                           |
| --------------- | ------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure containing the image to be saved |
| **dst**         | a data stream to save to                                                  |
| **freedst**     | non-zero to close the stream after being written                          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Surfaces with a 24-bit, 32-bit and paletted 8-bit format get saved in the
BMP directly. Other RGB formats with 8-bit or higher get converted to a
24-bit surface or, if they have an alpha mask or a colorkey, to a 32-bit
surface before they are saved. YUV and paletted 1-bit and 4-bit formats are
not supported.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LoadBMP_RW](SDL_LoadBMP_RW)
- [SDL_SaveBMP](SDL_SaveBMP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

