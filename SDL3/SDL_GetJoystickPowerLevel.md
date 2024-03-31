###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickPowerLevel

Get the battery level of a joystick as [SDL_JoystickPowerLevel](SDL_JoystickPowerLevel).

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_JoystickPowerLevel SDL_GetJoystickPowerLevel(SDL_Joystick *joystick);

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

