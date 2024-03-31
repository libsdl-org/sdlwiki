###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StopHapticEffect

Stop the haptic effect on its associated haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_StopHapticEffect(SDL_Haptic *haptic, int effect);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RunHapticEffect](SDL_RunHapticEffect)
* [SDL_StopHapticEffects](SDL_StopHapticEffects)

----
[CategoryAPI](CategoryAPI)

