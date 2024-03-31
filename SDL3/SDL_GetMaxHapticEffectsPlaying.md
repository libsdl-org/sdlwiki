###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMaxHapticEffectsPlaying

Get the number of effects a haptic device can play at the same time.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetMaxHapticEffectsPlaying(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                                                      |
| -------------- | -------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query maximum playing effects |

## Return Value

Returns the number of effects the haptic device can play at the same time
or a negative error code on failure; call [SDL_GetError](SDL_GetError)()
for more information.

## Remarks

This is not supported on all platforms, but will always return a value.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetMaxHapticEffects](SDL_GetMaxHapticEffects)
* [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI)

