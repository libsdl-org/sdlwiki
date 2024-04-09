###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Palette

A set of indexed colors representing a palette.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_Palette
{
    int ncolors;        /*< number of elements in `colors`. */
    SDL_Color *colors;  /*< an array of colors, `ncolors` long. */
    Uint32 version;     /*< internal use only, do not touch. */
    int refcount;       /*< internal use only, do not touch. */
} SDL_Palette;
```

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_PixelFormat](SDL_PixelFormat)
* [SDL_SetPaletteColors](SDL_SetPaletteColors)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

