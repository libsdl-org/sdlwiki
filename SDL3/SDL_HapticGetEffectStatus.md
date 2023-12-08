###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticGetEffectStatus

Get the status of the current effect on the specified haptic device.

## Syntax

```c
int SDL_HapticGetEffectStatus(SDL_Haptic * haptic,
                              int effect);

```

## Function Parameters

|                |                                                                       |
| -------------- | --------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query for the effect status on |
| **effect**     | the ID of the haptic effect to query its status                       |

## Return Value

Returns 0 if it isn't playing, 1 if it is playing, or a negative error code
on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Device must support the [SDL_HAPTIC_STATUS](SDL_HAPTIC_STATUS.md) feature.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticRunEffect](SDL_HapticRunEffect.md)
* [SDL_HapticStopEffect](SDL_HapticStopEffect.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
