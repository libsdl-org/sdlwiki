###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticNumEffectsPlaying

Get the number of effects a haptic device can play at the same time.

## Syntax

```c
int SDL_HapticNumEffectsPlaying(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                                                      |
| -------------- | -------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query maximum playing effects |

## Return Value

Returns the number of effects the haptic device can play at the same time
or a negative error code on failure; call [SDL_GetError](SDL_GetError)()
for more information.

## Remarks

This is not supported on all platforms, but will always return a value.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticNumEffects](SDL_HapticNumEffects)
* [SDL_HapticQuery](SDL_HapticQuery)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


