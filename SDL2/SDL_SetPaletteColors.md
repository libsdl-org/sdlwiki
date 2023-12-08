###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

Returns 0 on success or a negative error code if not all of the colors
could be set; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AllocPalette](SDL_AllocPalette.md)
* [SDL_CreateRGBSurface](SDL_CreateRGBSurface.md)

----
[CategoryAPI](CategoryAPI.md)
