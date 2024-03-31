###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticDestroyEffect

Destroy a haptic effect on the device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_HapticDestroyEffect(SDL_Haptic * haptic,
                             int effect);

```

## Function Parameters

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to destroy the effect on |
| **effect**     | the ID of the haptic effect to destroy                       |

## Remarks

This will stop the effect if it's running. Effects are automatically
destroyed when the device is closed.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticNewEffect](SDL_HapticNewEffect)

----
[CategoryAPI](CategoryAPI)

