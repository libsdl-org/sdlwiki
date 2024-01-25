###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenHaptic

Open a haptic device for use.

## Syntax

```c
SDL_Haptic* SDL_OpenHaptic(SDL_HapticID instance_id);

```

## Function Parameters

|                     |                               |
| ------------------- | ----------------------------- |
| **instance_id**     | the haptic device instance ID |

## Return Value

Returns the device identifier or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The index passed as an argument refers to the N'th haptic device on this
system.

When opening a haptic device, its gain will be set to maximum and
autocenter will be disabled. To modify these values use
[SDL_SetHapticGain](SDL_SetHapticGain)() and
[SDL_SetHapticAutocenter](SDL_SetHapticAutocenter)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CloseHaptic](SDL_CloseHaptic)
* [SDL_GetHaptics](SDL_GetHaptics)
* [SDL_OpenHapticFromJoystick](SDL_OpenHapticFromJoystick)
* [SDL_OpenHapticFromMouse](SDL_OpenHapticFromMouse)
* [SDL_PauseHaptic](SDL_PauseHaptic)
* [SDL_SetHapticAutocenter](SDL_SetHapticAutocenter)
* [SDL_SetHapticGain](SDL_SetHapticGain)
* [SDL_StopHapticEffects](SDL_StopHapticEffects)

----
[CategoryAPI](CategoryAPI)

