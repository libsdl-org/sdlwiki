###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetAxisInitialState

Get the initial state of an axis control on a joystick.

## Syntax

```c
SDL_bool SDL_JoystickGetAxisInitialState(SDL_Joystick *joystick,
                           int axis, Sint16 *state);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick.md) structure containing joystick information |
| **axis**         | the axis to query; the axis indices start at index 0                      |
| **state**        | Upon return, the initial value is supplied here.                          |

## Return Value

Return [SDL_TRUE](SDL_TRUE.md) if this axis has any initial value, or
[SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

The state is a value ranging from -32768 to 32767.

The axis indices start at index 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI.md)
