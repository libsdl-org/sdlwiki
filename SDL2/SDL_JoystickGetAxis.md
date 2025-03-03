# SDL_JoystickGetAxis

Get the current state of an axis control on a joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
Sint16 SDL_JoystickGetAxis(SDL_Joystick *joystick,
                           int axis);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |
| int                            | **axis**     | the axis to query; the axis indices start at index 0.                      |

## Return Value

([Sint16](Sint16)) Returns a 16-bit signed integer representing the current
position of the axis or 0 on failure; call [SDL_GetError](SDL_GetError)()
for more information.

## Remarks

SDL makes no promises about what part of the joystick any given axis refers
to. Your game should have some sort of configuration UI to let users
specify what each axis should be bound to. Alternately, SDL's higher-level
Game Controller API makes a great effort to apply order to this lower-level
interface, so you know that a specific axis is the "left thumb stick," etc.

The value returned by [SDL_JoystickGetAxis](SDL_JoystickGetAxis)() is a
signed integer (-32768 to 32767) representing the current position of the
axis. It may be necessary to impose certain tolerances on these values to
account for jitter.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_JoystickNumAxes](SDL_JoystickNumAxes)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

