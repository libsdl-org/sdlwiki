###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreatePalette

Create a palette structure with the specified number of color entries.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
SDL_Palette * SDL_CreatePalette(int ncolors);
```

## Function Parameters

|     |             |                                                              |
| --- | ----------- | ------------------------------------------------------------ |
| int | **ncolors** | represents the number of color entries in the color palette. |

## Return Value

([SDL_Palette](SDL_Palette) *) Returns a new [SDL_Palette](SDL_Palette)
structure on success or NULL on failure (e.g. if there wasn't enough
memory); call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The palette entries are initialized to white.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_DestroyPalette](SDL_DestroyPalette)
- [SDL_SetPaletteColors](SDL_SetPaletteColors)
- [SDL_SetSurfacePalette](SDL_SetSurfacePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

