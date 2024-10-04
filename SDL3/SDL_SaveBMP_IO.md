###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SaveBMP_IO

Save a surface to a seekable SDL data stream in BMP format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SaveBMP_IO(SDL_Surface *surface, SDL_IOStream *dst, bool closeio);
```

## Function Parameters

|                                |             |                                                                                                      |
| ------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) *   | **surface** | the [SDL_Surface](SDL_Surface) structure containing the image to be saved.                           |
| [SDL_IOStream](SDL_IOStream) * | **dst**     | a data stream to save to.                                                                            |
| bool                           | **closeio** | if true, calls [SDL_CloseIO](SDL_CloseIO)() on `dst` before returning, even in the case of an error. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Surfaces with a 24-bit, 32-bit and paletted 8-bit format get saved in the
BMP directly. Other RGB formats with 8-bit or higher get converted to a
24-bit surface or, if they have an alpha mask or a colorkey, to a 32-bit
surface before they are saved. YUV and paletted 1-bit and 4-bit formats are
not supported.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_LoadBMP_IO](SDL_LoadBMP_IO)
- [SDL_SaveBMP](SDL_SaveBMP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

