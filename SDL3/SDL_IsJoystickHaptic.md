###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsJoystickHaptic

Query if a joystick has haptic features.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_bool SDL_IsJoystickHaptic(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                  |
| ---------------- | ---------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to test for haptic capabilities |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the joystick is haptic or
[SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenHapticFromJoystick](SDL_OpenHapticFromJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

