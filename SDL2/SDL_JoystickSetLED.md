###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickSetLED

Update a joystick's LED color.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickSetLED(SDL_Joystick *joystick, Uint8 red, Uint8 green, Uint8 blue);

```

## Function Parameters

|                  |                                |
| ---------------- | ------------------------------ |
| **joystick**     | The joystick to update         |
| **red**          | The intensity of the red LED   |
| **green**        | The intensity of the green LED |
| **blue**         | The intensity of the blue LED  |

## Return Value

Returns 0 on success, -1 if this joystick does not have a modifiable LED

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

