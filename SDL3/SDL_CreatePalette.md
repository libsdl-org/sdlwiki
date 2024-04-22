###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePalette

Create a palette structure with the specified number of color entries.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
SDL_Palette* SDL_CreatePalette(int ncolors);

```

## Function Parameters

|                 |                                                             |
| --------------- | ----------------------------------------------------------- |
| **ncolors**     | represents the number of color entries in the color palette |

## Return Value

Returns a new [SDL_Palette](SDL_Palette) structure on success or NULL on
failure (e.g. if there wasn't enough memory); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The palette entries are initialized to white.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_DestroyPalette](SDL_DestroyPalette)
* [SDL_SetPaletteColors](SDL_SetPaletteColors)
* [SDL_SetPixelFormatPalette](SDL_SetPixelFormatPalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

