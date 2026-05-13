# SDL_LoadJPG

Load a JPEG image from a file.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_LoadJPG(const char *file);
```

## Function Parameters

|              |          |                       |
| ------------ | -------- | --------------------- |
| const char * | **file** | the JPG file to load. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a pointer to a new
[SDL_Surface](SDL_Surface) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is intended as a convenience function for loading images from trusted
sources. If you want to load arbitrary images you should use libjpeg or
another image loading library designed with security in mind.

The new surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)(). Not doing so will result in a
memory leak.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_DestroySurface](SDL_DestroySurface)
- [SDL_LoadJPG_IO](SDL_LoadJPG_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

