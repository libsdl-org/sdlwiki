###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticOpened

Check if the haptic device at the designated index has been opened.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_HapticOpened(int device_index);

```

## Function Parameters

|                      |                                  |
| -------------------- | -------------------------------- |
| **device_index**     | the index of the device to query |

## Return Value

Returns 1 if it has been opened, 0 if it hasn't or on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_HapticIndex](SDL_HapticIndex)
* [SDL_HapticOpen](SDL_HapticOpen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

