# SDL_SavePNG_IO

Save a surface to a seekable SDL data stream in PNG format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SavePNG_IO(SDL_Surface *surface, SDL_IOStream *dst, bool closeio);
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

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_LoadPNG_IO](SDL_LoadPNG_IO)
- [SDL_SavePNG](SDL_SavePNG)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

