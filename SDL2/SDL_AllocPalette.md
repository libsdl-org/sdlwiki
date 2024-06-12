###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AllocPalette

Create a palette structure with the specified number of color entries.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
SDL_Palette* SDL_AllocPalette(int ncolors);
```

## Function Parameters

|     |             |                                                             |
| --- | ----------- | ----------------------------------------------------------- |
| int | **ncolors** | represents the number of color entries in the color palette |

## Return Value

([SDL_Palette](SDL_Palette) *) Returns a new [SDL_Palette](SDL_Palette)
structure on success or NULL on failure (e.g. if there wasn't enough
memory); call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The palette entries are initialized to white.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_FreePalette](SDL_FreePalette)


## Example

```c
SDL_Palette* palette = NULL;

/* ... */

SDL_Init(SDL_INIT_VIDEO);

// Create window and renderer

SDL_Window *window;
SDL_Renderer *renderer;
SDL_CreateWindowAndRenderer(640, 480, 0, &window, &renderer);

// Create new palette with 4 colors

palette = SDL_AllocPalette(4);

if (palette == NULL) printf( "Error: %s\n", SDL_GetError() );

/* ... */

// Set green and blue of the first color in the palette to 0

palette->colors[0].g = 0;
palette->colors[0].b = 0;

// Set render draw color to red

SDL_SetRenderDrawColor(renderer, palette->colors[0].r, palette->colors[0].g, palette->colors[0].b, palette->colors[0].a);

/* ... */

SDL_FreePalette(palette);
palette = NULL;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

