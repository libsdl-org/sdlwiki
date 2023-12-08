###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticUnpause

Unpause a haptic device.

## Syntax

```c
int SDL_HapticUnpause(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to unpause |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Call to unpause after [SDL_HapticPause](SDL_HapticPause.md)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticPause](SDL_HapticPause.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
