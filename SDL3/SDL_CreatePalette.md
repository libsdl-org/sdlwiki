###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePalette

Create a palette structure with the specified number of color entries.

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

## Related Functions

* [SDL_DestroyPalette](SDL_DestroyPalette)

----
[CategoryAPI](CategoryAPI)

