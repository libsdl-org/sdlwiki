###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowGammaRamp

Get the gamma ramp for a given window's display.

## Syntax

```c
int SDL_GetWindowGammaRamp(SDL_Window * window,
                           Uint16 * red,
                           Uint16 * green,
                           Uint16 * blue);

```

## Function Parameters

|                |                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| **window**     | the window used to select the display whose gamma ramp will be queried                                       |
| **red**        | a 256 element array of 16-bit quantities filled in with the translation table for the red channel, or NULL   |
| **green**      | a 256 element array of 16-bit quantities filled in with the translation table for the green channel, or NULL |
| **blue**       | a 256 element array of 16-bit quantities filled in with the translation table for the blue channel, or NULL  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Despite the name and signature, this method retrieves the gamma ramp of the
entire display, not an individual window. A window is considered to be
owned by the display that contains the window's center pixel. (The index of
this display can be retrieved using
[SDL_GetWindowDisplayIndex](SDL_GetWindowDisplayIndex.md)().)

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetWindowGammaRamp](SDL_SetWindowGammaRamp.md)

----
[CategoryAPI](CategoryAPI.md)
