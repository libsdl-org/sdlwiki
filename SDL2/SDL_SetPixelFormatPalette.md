###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetPixelFormatPalette

Set the palette for a pixel format structure.

## Syntax

```c
int SDL_SetPixelFormatPalette(SDL_PixelFormat * format,
                              SDL_Palette *palette);

```

## Function Parameters

|                 |                                                                            |
| --------------- | -------------------------------------------------------------------------- |
| **format**      | the [SDL_PixelFormat](SDL_PixelFormat.md) structure that will use the palette |
| **palette**     | the [SDL_Palette](SDL_Palette.md) structure that will be used                 |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AllocPalette](SDL_AllocPalette.md)
* [SDL_FreePalette](SDL_FreePalette.md)

----
[CategoryAPI](CategoryAPI.md)
