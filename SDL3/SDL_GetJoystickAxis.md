###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickAxis

Get the current state of an axis control on a joystick.

## Syntax

```c
Sint16 SDL_GetJoystickAxis(SDL_Joystick *joystick,
                           int axis);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |
| **axis**         | the axis to query; the axis indices start at index 0                      |

## Return Value

Returns a 16-bit signed integer representing the current position of the
axis or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

SDL makes no promises about what part of the joystick any given axis refers
to. Your game should have some sort of configuration UI to let users
specify what each axis should be bound to. Alternately, SDL's higher-level
Game Controller API makes a great effort to apply order to this lower-level
interface, so you know that a specific axis is the "left thumb stick," etc.

The value returned by [SDL_GetJoystickAxis](SDL_GetJoystickAxis)() is a
signed integer (-32768 to 32767) representing the current position of the
axis. It may be necessary to impose certain tolerances on these values to
account for jitter.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumJoystickAxes](SDL_GetNumJoystickAxes)

----
[CategoryAPI](CategoryAPI)

