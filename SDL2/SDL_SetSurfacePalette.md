###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetSurfacePalette

Set the palette used by a surface.

## Syntax

```c
int SDL_SetSurfacePalette(SDL_Surface * surface,
                          SDL_Palette * palette);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to update |
| **palette**     | the [SDL_Palette](SDL_Palette) structure to use    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

A single palette can be shared with many surfaces.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI)

