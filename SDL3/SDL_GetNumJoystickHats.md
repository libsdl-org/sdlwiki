###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetNumJoystickHats

Get the number of POV hats on a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_GetNumJoystickHats(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |

## Return Value

(int) Returns the number of POV hats on success or -1 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickHat](SDL_GetJoystickHat)
- [SDL_GetNumJoystickAxes](SDL_GetNumJoystickAxes)
- [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)
- [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

