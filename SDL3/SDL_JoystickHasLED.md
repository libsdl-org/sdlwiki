###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

Returns [SDL_TRUE](SDL_TRUE) if the joystick has a modifiable LED,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

