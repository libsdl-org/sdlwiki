###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfacePalette

Set the palette used by a surface.

## Syntax

```c
int SDL_SetSurfacePalette(SDL_Surface *surface,
                          SDL_Palette *palette);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to update |
| **palette**     | the [SDL_Palette](SDL_Palette.md) structure to use    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

A single palette can be shared with many surfaces.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
