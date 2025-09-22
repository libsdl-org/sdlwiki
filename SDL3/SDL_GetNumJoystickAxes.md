# SDL_GetNumJoystickAxes

Get the number of general axis controls on a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_GetNumJoystickAxes(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |

## Return Value

(int) Returns the number of axis controls/number of axes on success or -1
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Often, the directional pad on a game controller will either look like 4
separate buttons or a POV hat, and not axes, but all of this is up to the
device and platform.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickAxis](SDL_GetJoystickAxis)
- [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)
- [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)
- [SDL_GetNumJoystickHats](SDL_GetNumJoystickHats)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

