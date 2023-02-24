###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickAxisInitialState

Get the initial state of an axis control on a joystick.

## Syntax

```c
SDL_bool SDL_GetJoystickAxisInitialState(SDL_Joystick *joystick,
                           int axis, Sint16 *state);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |
| **axis**         | the axis to query; the axis indices start at index 0                      |
| **state**        | Upon return, the initial value is supplied here.                          |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if this axis has any initial value, or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

The state is a value ranging from -32768 to 32767.

The axis indices start at index 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

