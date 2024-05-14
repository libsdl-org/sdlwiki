###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPixelFormatPalette

Set the palette for a pixel format structure.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
int SDL_SetPixelFormatPalette(SDL_PixelFormat * format,
                              SDL_Palette *palette);

```

## Function Parameters

|                 |                                                                            |
| --------------- | -------------------------------------------------------------------------- |
| **format**      | the [SDL_PixelFormat](SDL_PixelFormat) structure that will use the palette |
| **palette**     | the [SDL_Palette](SDL_Palette) structure that will be used                 |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

