###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyPalette

Free a palette created with [SDL_CreatePalette](SDL_CreatePalette)().

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_DestroyPalette(SDL_Palette * palette);

```

## Function Parameters

|                 |                                                      |
| --------------- | ---------------------------------------------------- |
| **palette**     | the [SDL_Palette](SDL_Palette) structure to be freed |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePalette](SDL_CreatePalette)

----
[CategoryAPI](CategoryAPI)

