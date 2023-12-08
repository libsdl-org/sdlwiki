###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePalette](SDL_CreatePalette.md)
* [SDL_DestroyPalette](SDL_DestroyPalette.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryPixels](CategoryPixels.md)
