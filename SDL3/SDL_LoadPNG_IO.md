# SDL_LoadPNG_IO

Load a PNG image from a seekable SDL data stream.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_LoadPNG_IO(SDL_IOStream *src, bool closeio);
```

## Function Parameters

|                                |             |                                                                                                      |
| ------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **src**     | the data stream for the surface.                                                                     |
| bool                           | **closeio** | if true, calls [SDL_CloseIO](SDL_CloseIO)() on `src` before returning, even in the case of an error. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a pointer to a new
[SDL_Surface](SDL_Surface) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is intended as a convenience function for loading images from trusted
sources. If you want to load arbitrary images you should use libpng or
another image loading library designed with security in mind.

The new surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)(). Not doing so will result in a
memory leak.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_DestroySurface](SDL_DestroySurface)
- [SDL_LoadPNG](SDL_LoadPNG)
- [SDL_SavePNG_IO](SDL_SavePNG_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

