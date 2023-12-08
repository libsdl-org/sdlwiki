###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickHasLED

Query whether a joystick has an LED.

## Syntax

```c
SDL_bool SDL_JoystickHasLED(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **joystick**     | The joystick to query |

## Return Value

Return [SDL_TRUE](SDL_TRUE.md) if the joystick has a modifiable LED,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
