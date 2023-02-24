###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticPause

Pause a haptic device.

## Syntax

```c
int SDL_HapticPause(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to pause |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the `[SDL_HAPTIC_PAUSE](SDL_HAPTIC_PAUSE)` feature.
Call [SDL_HapticUnpause](SDL_HapticUnpause)() to resume playback.

Do not modify the effects nor add new ones while the device is paused. That
can cause all sorts of weird errors.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticUnpause](SDL_HapticUnpause)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


