###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticNumEffectsPlaying

Get the number of effects a haptic device can play at the same time.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_HapticNumEffectsPlaying(SDL_Haptic * haptic);

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

This function is available since SDL 2.0.0.

## See Also

* [SDL_HapticNumEffects](SDL_HapticNumEffects)
* [SDL_HapticQuery](SDL_HapticQuery)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

