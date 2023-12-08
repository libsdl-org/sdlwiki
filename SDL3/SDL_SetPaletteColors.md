###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPaletteColors

Set a range of colors in a palette.

## Syntax

```c
int SDL_SetPaletteColors(SDL_Palette * palette,
                         const SDL_Color * colors,
                         int firstcolor, int ncolors);

```

## Function Parameters

|                    |                                                                        |
| ------------------ | ---------------------------------------------------------------------- |
| **palette**        | the [SDL_Palette](SDL_Palette.md) structure to modify                     |
| **colors**         | an array of [SDL_Color](SDL_Color.md) structures to copy into the palette |
| **firstcolor**     | the index of the first palette entry to modify                         |
| **ncolors**        | the number of entries to modify                                        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePalette](SDL_CreatePalette.md)
* [SDL_CreateSurface](SDL_CreateSurface.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryPixels](CategoryPixels.md)
