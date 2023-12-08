###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowGammaRamp

Set the gamma ramp for the display that owns a given window.

## Syntax

```c
int SDL_SetWindowGammaRamp(SDL_Window * window,
                           const Uint16 * red,
                           const Uint16 * green,
                           const Uint16 * blue);

```

## Function Parameters

|                |                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------- |
| **window**     | the window used to select the display whose gamma ramp will be changed                                     |
| **red**        | a 256 element array of 16-bit quantities representing the translation table for the red channel, or NULL   |
| **green**      | a 256 element array of 16-bit quantities representing the translation table for the green channel, or NULL |
| **blue**       | a 256 element array of 16-bit quantities representing the translation table for the blue channel, or NULL  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Set the gamma translation table for the red, green, and blue channels of
the video hardware. Each table is an array of 256 16-bit quantities,
representing a mapping between the input and output for that channel. The
input is the index into the array, and the output is the 16-bit gamma value
at that index, scaled to the output color precision.

Despite the name and signature, this method sets the gamma ramp of the
entire display, not an individual window. A window is considered to be
owned by the display that contains the window's center pixel. (The index of
this display can be retrieved using
[SDL_GetWindowDisplayIndex](SDL_GetWindowDisplayIndex.md)().) The gamma ramp
set will not follow the window if it is moved to another display.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowGammaRamp](SDL_GetWindowGammaRamp.md)

----
[CategoryAPI](CategoryAPI.md)
