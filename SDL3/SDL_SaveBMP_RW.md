###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SaveBMP_RW

Save a surface to a seekable SDL data stream in BMP format.

## Syntax

```c
int SDL_SaveBMP_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LoadBMP_RW](SDL_LoadBMP_RW)
* [SDL_SaveBMP](SDL_SaveBMP)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


