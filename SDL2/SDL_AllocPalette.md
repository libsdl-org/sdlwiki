# SDL_AllocPalette

Create a palette structure with the specified number of color entries.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
SDL_Palette* SDL_AllocPalette(int ncolors);
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

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_FreePalette](SDL_FreePalette)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

