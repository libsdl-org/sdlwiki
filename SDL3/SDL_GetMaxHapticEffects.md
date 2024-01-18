###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMaxHapticEffects

Get the number of effects a haptic device can store.

## Syntax

```c
int SDL_GetMaxHapticEffects(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |

## Return Value

Returns the number of effects the haptic device can store or a negative
error code on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

On some platforms this isn't fully supported, and therefore is an
approximation. Always check to see if your created effect was actually
created and do not rely solely on
[SDL_GetMaxHapticEffects](SDL_GetMaxHapticEffects)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetMaxHapticEffectsPlaying](SDL_GetMaxHapticEffectsPlaying)
* [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI)

