###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetPaletteColors

Set a range of colors in a palette.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
int SDL_SetPaletteColors(SDL_Palette * palette,
                     const SDL_Color * colors,
                     int firstcolor, int ncolors);
```

## Function Parameters

|                                |                |                                                                        |
| ------------------------------ | -------------- | ---------------------------------------------------------------------- |
| [SDL_Palette](SDL_Palette) *   | **palette**    | the [SDL_Palette](SDL_Palette) structure to modify                     |
| const [SDL_Color](SDL_Color) * | **colors**     | an array of [SDL_Color](SDL_Color) structures to copy into the palette |
| int                            | **firstcolor** | the index of the first palette entry to modify                         |
| int                            | **ncolors**    | the number of entries to modify                                        |

## Return Value

(int) Returns 0 on success or a negative error code if not all of the
colors could be set; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AllocPalette](SDL_AllocPalette)
- [SDL_CreateRGBSurface](SDL_CreateRGBSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

