###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPaletteColors

Set a range of colors in a palette.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
int SDL_SetPaletteColors(SDL_Palette * palette,
                         const SDL_Color * colors,
                         int firstcolor, int ncolors);

```

## Function Parameters

|                    |                                                                        |
| ------------------ | ---------------------------------------------------------------------- |
| **palette**        | the [SDL_Palette](SDL_Palette) structure to modify                     |
| **colors**         | an array of [SDL_Color](SDL_Color) structures to copy into the palette |
| **firstcolor**     | the index of the first palette entry to modify                         |
| **ncolors**        | the number of entries to modify                                        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

