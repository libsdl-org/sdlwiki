###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenHaptic

Open a haptic device for use.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_Haptic* SDL_OpenHaptic(SDL_HapticID instance_id);
```

## Function Parameters

|                              |                 |                                |
| ---------------------------- | --------------- | ------------------------------ |
| [SDL_HapticID](SDL_HapticID) | **instance_id** | the haptic device instance ID. |

## Return Value

([SDL_Haptic](SDL_Haptic) *) Returns the device identifier or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The index passed as an argument refers to the N'th haptic device on this
system.

When opening a haptic device, its gain will be set to maximum and
autocenter will be disabled. To modify these values use
[SDL_SetHapticGain](SDL_SetHapticGain)() and
[SDL_SetHapticAutocenter](SDL_SetHapticAutocenter)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CloseHaptic](SDL_CloseHaptic)
- [SDL_GetHaptics](SDL_GetHaptics)
- [SDL_OpenHapticFromJoystick](SDL_OpenHapticFromJoystick)
- [SDL_OpenHapticFromMouse](SDL_OpenHapticFromMouse)
- [SDL_SetHapticAutocenter](SDL_SetHapticAutocenter)
- [SDL_SetHapticGain](SDL_SetHapticGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

