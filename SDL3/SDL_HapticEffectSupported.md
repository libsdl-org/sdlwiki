###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticEffectSupported

Check to see if an effect is supported by a haptic device.

## Syntax

```c
int SDL_HapticEffectSupported(SDL_Haptic * haptic,
                              SDL_HapticEffect *
                              effect);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |
| **effect**     | the desired effect to query                  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if effect is supported, [SDL_FALSE](SDL_FALSE.md)
if it isn't, or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticNewEffect](SDL_HapticNewEffect.md)
* [SDL_HapticQuery](SDL_HapticQuery.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
