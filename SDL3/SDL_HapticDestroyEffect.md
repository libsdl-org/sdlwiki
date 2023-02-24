###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticDestroyEffect

Destroy a haptic effect on the device.

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticNewEffect](SDL_HapticNewEffect)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


