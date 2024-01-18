###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHapticEffectStatus

Get the status of the current effect on the specified haptic device.

## Syntax

```c
int SDL_GetHapticEffectStatus(SDL_Haptic *haptic, int effect);

```

## Function Parameters

|                |                                                                       |
| -------------- | --------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query for the effect status on |
| **effect**     | the ID of the haptic effect to query its status                       |

## Return Value

Returns 0 if it isn't playing, 1 if it is playing, or a negative error code
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the [SDL_HAPTIC_STATUS](SDL_HAPTIC_STATUS) feature.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RunHapticEffect](SDL_RunHapticEffect)
* [SDL_StopHapticEffect](SDL_StopHapticEffect)

----
[CategoryAPI](CategoryAPI)

