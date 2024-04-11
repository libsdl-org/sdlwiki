###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowBrightness

Set the brightness (gamma multiplier) for a given window's display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetWindowBrightness(SDL_Window * window, float brightness);

```

## Function Parameters

|                    |                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| **window**         | the window used to select the display whose brightness will be changed                                   |
| **brightness**     | the brightness (gamma multiplier) value to set where 0.0 is completely dark and 1.0 is normal brightness |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Despite the name and signature, this method sets the brightness of the
entire display, not an individual window. A window is considered to be
owned by the display that contains the window's center pixel. (The index of
this display can be retrieved using
[SDL_GetWindowDisplayIndex](SDL_GetWindowDisplayIndex)().) The brightness
set will not follow the window if it is moved to another display.

Many platforms will refuse to set the display brightness in modern times.
You are better off using a shader to adjust gamma during rendering, or
something similar.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetWindowBrightness](SDL_GetWindowBrightness)
* [SDL_SetWindowGammaRamp](SDL_SetWindowGammaRamp)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

