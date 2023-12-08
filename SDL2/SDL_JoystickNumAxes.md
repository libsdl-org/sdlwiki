###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickNumAxes

Get the number of general axis controls on a joystick.

## Syntax

```c
int SDL_JoystickNumAxes(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick.md) structure containing joystick information |

## Return Value

Returns the number of axis controls/number of axes on success or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

Often, the directional pad on a game controller will either look like 4
separate buttons or a POV hat, and not axes, but all of this is up to the
device and platform.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetAxis](SDL_JoystickGetAxis.md)
* [SDL_JoystickOpen](SDL_JoystickOpen.md)

----
[CategoryAPI](CategoryAPI.md)
