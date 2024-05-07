###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetSurfaceAlphaMod

Get the additional alpha value used in blit operations.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_GetSurfaceAlphaMod(SDL_Surface * surface,
                           Uint8 * alpha);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to query |
| **alpha**       | a pointer filled in with the current alpha value  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetSurfaceColorMod](SDL_GetSurfaceColorMod)
- [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

