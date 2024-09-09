###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickButton

Get the current state of a button on a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_GetJoystickButton(SDL_Joystick *joystick, int button);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |
| int                            | **button**   | the button index to get the state from; indices start at index 0.          |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the button is
pressed, [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

