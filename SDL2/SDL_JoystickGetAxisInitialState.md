###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetAxisInitialState

Get the initial state of an axis control on a joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_JoystickGetAxisInitialState(SDL_Joystick *joystick,
                       int axis, Sint16 *state);
```

## Function Parameters

|                                |              |                                                                           |
| ------------------------------ | ------------ | ------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |
| int                            | **axis**     | the axis to query; the axis indices start at index 0                      |
| Sint16 *                       | **state**    | Upon return, the initial value is supplied here.                          |

## Return Value

([SDL_bool](SDL_bool)) Return [SDL_TRUE](SDL_TRUE) if this axis has any
initial value, or [SDL_FALSE](SDL_FALSE) if not.

## Remarks

The state is a value ranging from -32768 to 32767.

The axis indices start at index 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

