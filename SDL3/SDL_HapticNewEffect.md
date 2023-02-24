###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticNewEffect

Create a new haptic effect on a specified device.

## Syntax

```c
int SDL_HapticNewEffect(SDL_Haptic * haptic,
                        SDL_HapticEffect * effect);

```

## Function Parameters

|                |                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------- |
| **haptic**     | an [SDL_Haptic](SDL_Haptic) device to create the effect on                                          |
| **effect**     | an [SDL_HapticEffect](SDL_HapticEffect) structure containing the properties of the effect to create |

## Return Value

Returns the ID of the effect on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticDestroyEffect](SDL_HapticDestroyEffect)
* [SDL_HapticRunEffect](SDL_HapticRunEffect)
* [SDL_HapticUpdateEffect](SDL_HapticUpdateEffect)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


