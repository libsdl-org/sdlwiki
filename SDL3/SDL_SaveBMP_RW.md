###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SaveBMP_RW

Save a surface to a seekable SDL data stream in BMP format.

## Syntax

```c
int SDL_SaveBMP_RW(SDL_Surface *surface, SDL_RWops *dst, SDL_bool freedst);

```

## Function Parameters

|                 |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure containing the image to be saved                                           |
| **dst**         | a data stream to save to                                                                                            |
| **freedst**     | if [SDL_TRUE](SDL_TRUE.md), calls [SDL_RWclose](SDL_RWclose.md)() on `dst` before returning, even in the case of an error |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Surfaces with a 24-bit, 32-bit and paletted 8-bit format get saved in the
BMP directly. Other RGB formats with 8-bit or higher get converted to a
24-bit surface or, if they have an alpha mask or a colorkey, to a 32-bit
surface before they are saved. YUV and paletted 1-bit and 4-bit formats are
not supported.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LoadBMP_RW](SDL_LoadBMP_RW.md)
* [SDL_SaveBMP](SDL_SaveBMP.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
