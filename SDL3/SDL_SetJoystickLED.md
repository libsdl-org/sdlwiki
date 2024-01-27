###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickLED

Update a joystick's LED color.

## Syntax

```c
int SDL_SetJoystickLED(SDL_Joystick *joystick, Uint8 red, Uint8 green, Uint8 blue);

```

## Function Parameters

|                  |                                |
| ---------------- | ------------------------------ |
| **joystick**     | The joystick to update         |
| **red**          | The intensity of the red LED   |
| **green**        | The intensity of the green LED |
| **blue**         | The intensity of the blue LED  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

For joysticks with a single color LED, the maximum of the RGB values will
be used as the LED brightness.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

