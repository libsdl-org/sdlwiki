###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetSurfaceBlendMode

Get the blend mode used for blit operations.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_GetSurfaceBlendMode(SDL_Surface * surface,
                            SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **surface**       | the [SDL_Surface](SDL_Surface) structure to query                   |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetSurfaceBlendMode](SDL_SetSurfaceBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

