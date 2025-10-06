# SDL_LoadPNG

Load a PNG image from a file.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_LoadPNG(const char *file);
```

## Function Parameters

|              |          |                       |
| ------------ | -------- | --------------------- |
| const char * | **file** | the PNG file to load. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a pointer to a new
[SDL_Surface](SDL_Surface) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The new surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)(). Not doing so will result in a
memory leak.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_DestroySurface](SDL_DestroySurface)
- [SDL_LoadPNG_IO](SDL_LoadPNG_IO)
- [SDL_SavePNG](SDL_SavePNG)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

