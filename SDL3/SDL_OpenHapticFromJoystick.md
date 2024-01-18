###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenHapticFromJoystick

Open a haptic device for use from a joystick device.

## Syntax

```c
SDL_Haptic* SDL_OpenHapticFromJoystick(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                 |
| ---------------- | --------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to create a haptic device from |

## Return Value

Returns a valid haptic device identifier on success or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

You must still close the haptic device separately. It will not be closed
with the joystick.

When opened from a joystick you should first close the haptic device before
closing the joystick device. If not, on some implementations the haptic
device will also get unallocated and you'll be unable to use force feedback
on that device.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CloseHaptic](SDL_CloseHaptic)
* [SDL_OpenHaptic](SDL_OpenHaptic)
* [SDL_IsJoystickHaptic](SDL_IsJoystickHaptic)

----
[CategoryAPI](CategoryAPI)

