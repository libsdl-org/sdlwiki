# SDL_SavePNG

Save a surface to a file in PNG format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SavePNG(SDL_Surface *surface, const char *file);
```

## Function Parameters

|                              |             |                                                                            |
| ---------------------------- | ----------- | -------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure containing the image to be saved. |
| const char *                 | **file**    | a file to save to.                                                         |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_LoadPNG](SDL_LoadPNG)
- [SDL_SavePNG_IO](SDL_SavePNG_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

