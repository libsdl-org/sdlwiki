###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHapticFeatures

Get the haptic device's supported features in bitwise manner.

## Syntax

```c
Uint32 SDL_GetHapticFeatures(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |

## Return Value

Returns a list of supported haptic features in bitwise manner (OR'd), or 0
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticEffectSupported](SDL_HapticEffectSupported)
* [SDL_GetMaxHapticEffects](SDL_GetMaxHapticEffects)

----
[CategoryAPI](CategoryAPI)

