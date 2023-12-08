###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticNumEffects

Get the number of effects a haptic device can store.

## Syntax

```c
int SDL_HapticNumEffects(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |

## Return Value

Returns the number of effects the haptic device can store or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

On some platforms this isn't fully supported, and therefore is an
approximation. Always check to see if your created effect was actually
created and do not rely solely on
[SDL_HapticNumEffects](SDL_HapticNumEffects.md)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticNumEffectsPlaying](SDL_HapticNumEffectsPlaying.md)
* [SDL_HapticQuery](SDL_HapticQuery.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
