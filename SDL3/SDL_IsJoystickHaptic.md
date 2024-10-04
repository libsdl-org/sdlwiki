###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IsJoystickHaptic

Query if a joystick has haptic features.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_IsJoystickHaptic(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                   |
| ------------------------------ | ------------ | ----------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) to test for haptic capabilities. |

## Return Value

(bool) Returns true if the joystick is haptic or false if it isn't.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenHapticFromJoystick](SDL_OpenHapticFromJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

