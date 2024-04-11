###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticStopEffect

Stop the haptic effect on its associated haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_HapticStopEffect(SDL_Haptic * haptic,
                         int effect);

```

## Function Parameters

|                |                                                           |
| -------------- | --------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to stop the effect on |
| **effect**     | the ID of the haptic effect to stop                       |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

*

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_HapticDestroyEffect](SDL_HapticDestroyEffect)
* [SDL_HapticRunEffect](SDL_HapticRunEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

