###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickCurrentPowerLevel

Get the battery level of a joystick as [SDL_JoystickPowerLevel](SDL_JoystickPowerLevel).

## Syntax

```c
SDL_JoystickPowerLevel SDL_JoystickCurrentPowerLevel(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                           |
| ---------------- | ----------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to query |

## Return Value

Returns the current battery level as
[SDL_JoystickPowerLevel](SDL_JoystickPowerLevel) on success or
[`SDL_JOYSTICK_POWER_UNKNOWN`](SDL_JOYSTICK_POWER_UNKNOWN) if it is unknown

## Version

This function is available since SDL 2.0.4.

----
[CategoryAPI](CategoryAPI)

