###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyPalette

Free a palette created with [SDL_CreatePalette](SDL_CreatePalette)().

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
void SDL_DestroyPalette(SDL_Palette *palette);
```

## Function Parameters

|                              |             |                                                       |
| ---------------------------- | ----------- | ----------------------------------------------------- |
| [SDL_Palette](SDL_Palette) * | **palette** | the [SDL_Palette](SDL_Palette) structure to be freed. |

## Thread Safety

It is safe to call this function from any thread, as long as the palette is
not modified or destroyed in another thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreatePalette](SDL_CreatePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

