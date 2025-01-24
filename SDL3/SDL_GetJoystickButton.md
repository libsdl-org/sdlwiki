# SDL_GetJoystickButton

Get the current state of a button on a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_GetJoystickButton(SDL_Joystick *joystick, int button);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |
| int                            | **button**   | the button index to get the state from; indices start at index 0.          |

## Return Value

(bool) Returns true if the button is pressed, false otherwise.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

