###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPaletteColors

Set a range of colors in a palette.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
SDL_bool SDL_SetPaletteColors(SDL_Palette *palette, const SDL_Color *colors, int firstcolor, int ncolors);
```

## Function Parameters

|                                |                |                                                                         |
| ------------------------------ | -------------- | ----------------------------------------------------------------------- |
| [SDL_Palette](SDL_Palette) *   | **palette**    | the [SDL_Palette](SDL_Palette) structure to modify.                     |
| const [SDL_Color](SDL_Color) * | **colors**     | an array of [SDL_Color](SDL_Color) structures to copy into the palette. |
| int                            | **firstcolor** | the index of the first palette entry to modify.                         |
| int                            | **ncolors**    | the number of entries to modify.                                        |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Thread Safety

It is safe to call this function from any thread, as long as the palette is
not modified or destroyed in another thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

