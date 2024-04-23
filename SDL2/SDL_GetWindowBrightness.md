###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowBrightness

Get the brightness (gamma multiplier) for a given window's display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
float SDL_GetWindowBrightness(SDL_Window * window);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **window**     | the window used to select the display whose brightness will be queried |

## Return Value

Returns the brightness for the display where 0.0 is completely dark and 1.0
is normal brightness.

## Remarks

Despite the name and signature, this method retrieves the brightness of the
entire display, not an individual window. A window is considered to be
owned by the display that contains the window's center pixel. (The index of
this display can be retrieved using
[SDL_GetWindowDisplayIndex](SDL_GetWindowDisplayIndex)().)

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetWindowBrightness](SDL_SetWindowBrightness)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


