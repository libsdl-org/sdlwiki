###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetPixelFormatPalette

Set the palette for a pixel format structure.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
int SDL_SetPixelFormatPalette(SDL_PixelFormat * format,
                          SDL_Palette *palette);
```

## Function Parameters

|                                      |             |                                                                            |
| ------------------------------------ | ----------- | -------------------------------------------------------------------------- |
| [SDL_PixelFormat](SDL_PixelFormat) * | **format**  | the [SDL_PixelFormat](SDL_PixelFormat) structure that will use the palette |
| [SDL_Palette](SDL_Palette) *         | **palette** | the [SDL_Palette](SDL_Palette) structure that will be used                 |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AllocPalette](SDL_AllocPalette)
- [SDL_FreePalette](SDL_FreePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

