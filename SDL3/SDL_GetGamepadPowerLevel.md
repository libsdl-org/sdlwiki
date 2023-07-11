###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadPowerLevel

Get the battery level of a gamepad, if available.

## Syntax

```c
SDL_JoystickPowerLevel SDL_GetGamepadPowerLevel(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Return Value

Returns the current battery level as
[SDL_JoystickPowerLevel](SDL_JoystickPowerLevel) on success or
[`SDL_JOYSTICK_POWER_UNKNOWN`](SDL_JOYSTICK_POWER_UNKNOWN) if it is unknown

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

