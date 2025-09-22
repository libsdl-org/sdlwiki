# SDL_GetNumJoystickButtons

Get the number of buttons on a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_GetNumJoystickButtons(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |

## Return Value

(int) Returns the number of buttons on success or -1 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickButton](SDL_GetJoystickButton)
- [SDL_GetNumJoystickAxes](SDL_GetNumJoystickAxes)
- [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)
- [SDL_GetNumJoystickHats](SDL_GetNumJoystickHats)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

