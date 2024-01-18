###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticEffectSupported

Check to see if an effect is supported by a haptic device.

## Syntax

```c
SDL_bool SDL_HapticEffectSupported(SDL_Haptic *haptic, SDL_HapticEffect *effect);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |
| **effect**     | the desired effect to query                  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the effect is supported or
[SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateHapticEffect](SDL_CreateHapticEffect)
* [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


