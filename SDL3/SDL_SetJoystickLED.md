###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetJoystickLED

Update a joystick's LED color.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SetJoystickLED(SDL_Joystick *joystick, Uint8 red, Uint8 green, Uint8 blue);
```

## Function Parameters

|                                |              |                                 |
| ------------------------------ | ------------ | ------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the joystick to update.         |
| Uint8                          | **red**      | the intensity of the red LED.   |
| Uint8                          | **green**    | the intensity of the green LED. |
| Uint8                          | **blue**     | the intensity of the blue LED.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

For joysticks with a single color LED, the maximum of the RGB values will
be used as the LED brightness.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

