###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticClose

Close a haptic device previously opened with [SDL_HapticOpen](SDL_HapticOpen.md)().

## Syntax

```c
void SDL_HapticClose(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to close |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticOpen](SDL_HapticOpen.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
