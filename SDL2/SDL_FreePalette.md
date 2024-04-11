###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreePalette

Free a palette created with [SDL_AllocPalette](SDL_AllocPalette)().

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_FreePalette(SDL_Palette * palette);

```

## Function Parameters

|                 |                                                      |
| --------------- | ---------------------------------------------------- |
| **palette**     | the [SDL_Palette](SDL_Palette) structure to be freed |

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_AllocPalette](SDL_AllocPalette)


## Example

```c
SDL_Palette* palette = nullptr;

...

SDL_Init(SDL_EVERYTHING);

// Create new palette with 4 colors

palette = SDL_AllocPalette(4);

if (palette == nullptr) printf( "Error: %s\n", SDL_GetError() );

...

// Set green and blue of the first color in the palette to 0

palette->colors[0].g = 0;
palette->colors[0].b = 0;

// Set render draw color to red

SDL_SetRenderDrawColor(renderer, palette->colors[0].r, palette->colors[0].g, palette->colors.b, palette->colors[0].a);

...

SDL_FreePalette(palette);
palette = nullptr;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

